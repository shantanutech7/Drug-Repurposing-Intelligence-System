# Drug Repurposing Intelligence System
### ML-powered discovery of existing drugs for new diseases

---

## What It Does
Identifies existing FDA-approved drugs that may work for diseases they weren't designed for — using biomedical feature engineering and a trained ML classifier.

## ML Architecture

```
Drug Features                    Disease Features
─────────────────                ─────────────────────
mechanism text  ──┐          ┌── description text
targets list    ──┤          ├── associated genes
pathways list   ──┤          ├── affected pathways
drug class      ──┘          └── disease category
        │                               │
        └─────── Feature Extraction ────┘
                        │
         ┌──────────────┼──────────────┐
         │              │              │
    TF-IDF          Jaccard       Class-Category
    Cosine          Overlap          Prior
    Similarity    (targets+paths)  (lookup table)
         │              │              │
         └──────────────┴──────────────┘
                        │
              Random Forest Classifier
              (trained on 30 validated pairs
               + 90 random negatives)
                        │
               Repurposing Score (0–100%)
```

## Dataset
- 20 drugs with real mechanisms, targets, pathways
- 15 diseases with gene/pathway associations
- 30 known validated repurposing pairs as positive examples

## Model Performance
- Cross-validation AUC: **0.89 ± 0.14**
- All 4 validated Alzheimer's drugs correctly ranked in top 5
- All 5 validated Breast Cancer drugs correctly ranked in top 5

## Setup

```bash
pip install -r requirements.txt
```

## Run

**Test model in terminal:**
```bash
python model.py
```

**Launch Streamlit app:**
```bash
streamlit run app.py
```

## File Structure

```
drug_repurposing/
├── data.py        # Drug/disease dataset + known pairs
├── model.py       # ML pipeline (run standalone to test)
├── app.py         # Streamlit UI with visualizations
├── requirements.txt
└── README.md
```

## Next Steps to Scale
- Connect DrugBank API for 10,000+ drugs
- Connect OpenTargets for gene-disease associations
- Add GNN (Graph Neural Network) for drug-target-disease graph
- Add PubMed abstract NLP for real-time evidence scoring
- Add molecular fingerprint similarity (SMILES strings)
