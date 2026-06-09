"""
Drug Repurposing Intelligence System
model.py — ML pipeline: Feature Engineering + Similarity Scoring + Classifier
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

from data import DRUGS, DISEASES, KNOWN_POSITIVE_PAIRS


class DrugRepurposingModel:
    """
    Drug Repurposing ML Model

    Architecture:
    1. TF-IDF semantic similarity (mechanism text <-> disease description)
    2. Jaccard similarity on biological targets/genes overlap
    3. Jaccard similarity on pathway overlap
    4. Drug class - disease category learned prior
    5. Random Forest classifier trained on known repurposing pairs
    """

    def __init__(self):
        self.tfidf = TfidfVectorizer(ngram_range=(1, 2), max_features=500, stop_words='english')
        self.classifier = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42, class_weight='balanced')
        self.scaler = StandardScaler()
        self.drug_df = pd.DataFrame(DRUGS)
        self.disease_df = pd.DataFrame(DISEASES)
        self.drug_vectors = None
        self.disease_vectors = None
        self.is_trained = False

    # ─────────────────────────────────────────────
    # FEATURE ENGINEERING
    # ─────────────────────────────────────────────

    def _jaccard(self, set_a: list, set_b: list) -> float:
        """Jaccard similarity between two lists treated as sets"""
        a = set([x.lower() for x in set_a])
        b = set([x.lower() for x in set_b])
        if not a or not b:
            return 0.0
        return len(a & b) / len(a | b)

    def _build_tfidf_vectors(self):
        """Build TF-IDF vectors for all drug mechanisms and disease descriptions"""
        drug_texts = self.drug_df['mechanism'].tolist()
        disease_texts = self.disease_df['description'].tolist()
        all_texts = drug_texts + disease_texts
        self.tfidf.fit(all_texts)
        self.drug_vectors = self.tfidf.transform(drug_texts)
        self.disease_vectors = self.tfidf.transform(disease_texts)

    def _get_features(self, drug: dict, disease: dict) -> list:
        """
        Extract 5 features for a (drug, disease) pair:
        [semantic_sim, target_gene_overlap, pathway_overlap, class_category_match, combined_score]
        """
        drug_idx = self.drug_df[self.drug_df['name'] == drug['name']].index[0]
        disease_idx = self.disease_df[self.disease_df['name'] == disease['name']].index[0]

        semantic_sim = float(cosine_similarity(
            self.drug_vectors[drug_idx],
            self.disease_vectors[disease_idx]
        )[0][0])

        target_overlap = self._jaccard(drug['targets'], disease['genes'])
        pathway_overlap = self._jaccard(drug['pathways'], disease['pathways'])

        class_category_pairs = {
            ("biguanide", "metabolic"): 0.9,
            ("biguanide", "oncology"): 0.7,
            ("biguanide", "endocrine"): 0.8,
            ("NSAID", "oncology"): 0.7,
            ("NSAID", "neurological"): 0.6,
            ("statin", "neurological"): 0.6,
            ("statin", "cardiovascular"): 0.8,
            ("mTOR inhibitor", "oncology"): 0.85,
            ("HDAC inhibitor", "oncology"): 0.85,
            ("antifolate", "autoimmune"): 0.7,
            ("antimalarial", "autoimmune"): 0.75,
            ("ARB", "hepatic"): 0.7,
            ("ARB", "cardiovascular"): 0.8,
            ("antifungal", "oncology"): 0.65,
            ("beta blocker", "oncology"): 0.6,
            ("PDE5 inhibitor", "cardiovascular"): 0.8,
            ("mood stabilizer", "neurological"): 0.7,
            ("dopamine agonist", "metabolic"): 0.65,
            ("immunomodulator", "autoimmune"): 0.75,
            ("immunomodulator", "infectious"): 0.6,
        }
        class_prior = class_category_pairs.get(
            (drug['drug_class'], disease['category']), 0.3
        )

        combined = 0.35 * semantic_sim + 0.25 * target_overlap + 0.25 * pathway_overlap + 0.15 * class_prior

        return [semantic_sim, target_overlap, pathway_overlap, class_prior, combined]

    # ─────────────────────────────────────────────
    # TRAINING
    # ─────────────────────────────────────────────

    def train(self):
        """Train the Random Forest classifier on known + negative pairs"""
        print("Building TF-IDF vectors...")
        self._build_tfidf_vectors()

        positive_set = set(KNOWN_POSITIVE_PAIRS)
        drug_lookup = {d['name']: d for d in DRUGS}
        disease_lookup = {d['name']: d for d in DISEASES}

        X, y = [], []

        for drug_name, disease_name in KNOWN_POSITIVE_PAIRS:
            features = self._get_features(drug_lookup[drug_name], disease_lookup[disease_name])
            X.append(features)
            y.append(1)

        # Generate 3x negative samples
        np.random.seed(42)
        drug_names = [d['name'] for d in DRUGS]
        disease_names = [d['name'] for d in DISEASES]
        neg_count = 0
        attempts = 0
        while neg_count < len(KNOWN_POSITIVE_PAIRS) * 3 and attempts < 5000:
            attempts += 1
            dn = np.random.choice(drug_names)
            dis = np.random.choice(disease_names)
            if (dn, dis) not in positive_set:
                features = self._get_features(drug_lookup[dn], disease_lookup[dis])
                X.append(features)
                y.append(0)
                neg_count += 1

        X = np.array(X)
        y = np.array(y)
        X_scaled = self.scaler.fit_transform(X)

        cv_scores = cross_val_score(self.classifier, X_scaled, y, cv=5, scoring='roc_auc')
        print(f"Cross-validation AUC: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

        self.classifier.fit(X_scaled, y)
        self.is_trained = True
        print(f"Model trained on {len(y)} pairs ({y.sum()} positive, {(y==0).sum()} negative)")
        return cv_scores.mean()

    # ─────────────────────────────────────────────
    # INFERENCE
    # ─────────────────────────────────────────────

    def predict_for_disease(self, disease_name: str, top_k: int = 5) -> pd.DataFrame:
        """
        Given a disease name, return top-k drug repurposing candidates
        with scores and explanations.
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call .train() first.")

        disease_lookup = {d['name']: d for d in DISEASES}
        if disease_name not in disease_lookup:
            raise ValueError(f"Disease '{disease_name}' not found. Available: {list(disease_lookup.keys())}")

        disease = disease_lookup[disease_name]
        known_for_disease = {pair[0] for pair in KNOWN_POSITIVE_PAIRS if pair[1] == disease_name}

        results = []
        for drug in DRUGS:
            features = self._get_features(drug, disease)
            features_scaled = self.scaler.transform([features])
            prob = self.classifier.predict_proba(features_scaled)[0][1]
            sem, tgt, path, cls, combined = features

            results.append({
                "Drug": drug['name'],
                "Approved For": drug['approved_for'],
                "Drug Class": drug['drug_class'],
                "Repurposing Score": round(prob * 100, 1),
                "Semantic Similarity": round(sem * 100, 1),
                "Target Overlap": round(tgt * 100, 1),
                "Pathway Overlap": round(path * 100, 1),
                "Known Repurposing": "✓ Validated" if drug['name'] in known_for_disease else "",
                "_shared_targets": list(set([t.lower() for t in drug['targets']]) & set([g.lower() for g in disease['genes']])),
                "_shared_pathways": list(set([p.lower() for p in drug['pathways']]) & set([pw.lower() for pw in disease['pathways']])),
                "_drug_class": drug['drug_class'],
                "_drug_targets": drug['targets'],
            })

        df = pd.DataFrame(results).sort_values("Repurposing Score", ascending=False)
        return df.head(top_k)

    def get_feature_importance(self) -> pd.DataFrame:
        """Return feature importance from the Random Forest"""
        features = ["Semantic Similarity", "Target-Gene Overlap", "Pathway Overlap", "Class-Category Prior", "Combined Score"]
        importances = self.classifier.feature_importances_
        return pd.DataFrame({"Feature": features, "Importance": importances}).sort_values("Importance", ascending=False)

    def get_full_heatmap_data(self) -> pd.DataFrame:
        """Return drug x disease repurposing probability matrix for heatmap"""
        if not self.is_trained:
            raise RuntimeError("Model not trained.")

        disease_lookup = {d['name']: d for d in DISEASES}
        records = []
        for disease in DISEASES:
            for drug in DRUGS:
                features = self._get_features(drug, disease)
                features_scaled = self.scaler.transform([features])
                prob = self.classifier.predict_proba(features_scaled)[0][1]
                records.append({
                    "Disease": disease['name'],
                    "Drug": drug['name'],
                    "Score": round(prob * 100, 1)
                })
        return pd.DataFrame(records).pivot(index="Disease", columns="Drug", values="Score")


if __name__ == "__main__":
    model = DrugRepurposingModel()
    auc = model.train()

    print("\n" + "="*60)
    print("TOP REPURPOSING CANDIDATES for Alzheimer's Disease")
    print("="*60)
    results = model.predict_for_disease("Alzheimer's Disease")
    print(results[["Drug", "Approved For", "Repurposing Score", "Semantic Similarity", "Target Overlap", "Pathway Overlap", "Known Repurposing"]].to_string(index=False))

    print("\n" + "="*60)
    print("TOP REPURPOSING CANDIDATES for Breast Cancer")
    print("="*60)
    results2 = model.predict_for_disease("Breast Cancer")
    print(results2[["Drug", "Approved For", "Repurposing Score", "Semantic Similarity", "Target Overlap", "Pathway Overlap", "Known Repurposing"]].to_string(index=False))

    print("\n" + "="*60)
    print("FEATURE IMPORTANCE")
    print("="*60)
    print(model.get_feature_importance().to_string(index=False))
