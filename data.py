"""
Drug Repurposing Intelligence System
data.py — Curated drug/disease dataset with real biomedical features
"""

DRUGS = [
    {
        "name": "Metformin",
        "approved_for": "Type 2 Diabetes",
        "drug_class": "biguanide",
        "mechanism": "activates AMPK pathway reduces hepatic glucose production improves insulin sensitivity mitochondrial complex I inhibitor anti-inflammatory metabolic regulation",
        "targets": ["AMPK", "mTOR", "IGF1R", "STAT3", "NF-kB"],
        "pathways": ["AMPK signaling", "mTOR pathway", "insulin signaling", "gluconeogenesis", "inflammation"]
    },
    {
        "name": "Sildenafil",
        "approved_for": "Erectile Dysfunction",
        "drug_class": "PDE5 inhibitor",
        "mechanism": "inhibits phosphodiesterase type 5 increases cGMP levels vasodilation smooth muscle relaxation nitric oxide signaling pulmonary vascular",
        "targets": ["PDE5A", "PDE6", "cGMP", "eNOS"],
        "pathways": ["nitric oxide pathway", "cGMP signaling", "vascular smooth muscle", "pulmonary circulation"]
    },
    {
        "name": "Aspirin",
        "approved_for": "Pain and Cardiovascular Prevention",
        "drug_class": "NSAID",
        "mechanism": "irreversible COX-1 COX-2 inhibition anti-inflammatory analgesic antiplatelet prostaglandin synthesis inhibitor acetylates cyclooxygenase",
        "targets": ["COX1", "COX2", "PTGS1", "PTGS2", "NF-kB"],
        "pathways": ["cyclooxygenase pathway", "prostaglandin synthesis", "platelet aggregation", "inflammation", "NF-kB"]
    },
    {
        "name": "Thalidomide",
        "approved_for": "Multiple Myeloma",
        "drug_class": "immunomodulator",
        "mechanism": "TNF-alpha inhibition anti-angiogenic immunomodulatory cereblon binding ubiquitin ligase modulation anti-inflammatory",
        "targets": ["CRBN", "TNF", "VEGF", "bFGF", "IL6"],
        "pathways": ["angiogenesis", "TNF signaling", "ubiquitin proteasome", "immune modulation", "NF-kB"]
    },
    {
        "name": "Rapamycin",
        "approved_for": "Transplant Rejection",
        "drug_class": "mTOR inhibitor",
        "mechanism": "inhibits mTORC1 complex binds FKBP12 autophagy induction cell cycle arrest anti-proliferative immunosuppressive longevity aging",
        "targets": ["mTOR", "FKBP12", "mTORC1", "S6K1", "4EBP1"],
        "pathways": ["mTOR pathway", "PI3K/AKT", "autophagy", "cell cycle", "protein synthesis"]
    },
    {
        "name": "Atorvastatin",
        "approved_for": "Hypercholesterolemia",
        "drug_class": "statin",
        "mechanism": "HMG-CoA reductase inhibitor lowers LDL cholesterol anti-inflammatory pleiotropic effects neuroprotective endothelial function",
        "targets": ["HMGCR", "HMG-CoA", "NPC1L1", "PCSK9"],
        "pathways": ["cholesterol synthesis", "mevalonate pathway", "inflammation", "endothelial function", "neuroinflammation"]
    },
    {
        "name": "Ibuprofen",
        "approved_for": "Pain and Inflammation",
        "drug_class": "NSAID",
        "mechanism": "COX inhibition anti-inflammatory analgesic prostaglandin E2 reduction neuroinflammation inhibitor neuroprotective beta amyloid reduction",
        "targets": ["COX1", "COX2", "PTGS1", "PTGS2"],
        "pathways": ["cyclooxygenase pathway", "neuroinflammation", "prostaglandin synthesis", "amyloid processing"]
    },
    {
        "name": "Methotrexate",
        "approved_for": "Rheumatoid Arthritis",
        "drug_class": "antifolate",
        "mechanism": "dihydrofolate reductase inhibitor anti-proliferative immunosuppressive folate metabolism purine synthesis inhibitor anti-inflammatory",
        "targets": ["DHFR", "TYMS", "ATIC", "ADORA2A"],
        "pathways": ["folate metabolism", "purine synthesis", "cell proliferation", "immune suppression", "inflammation"]
    },
    {
        "name": "Lithium",
        "approved_for": "Bipolar Disorder",
        "drug_class": "mood stabilizer",
        "mechanism": "GSK3 beta inhibition neuroprotective neurogenesis inositol depletion autophagy tau phosphorylation reduction BDNF increase mitochondrial protection",
        "targets": ["GSK3B", "INPP1", "IMPase", "BDNF", "BCL2"],
        "pathways": ["GSK3 signaling", "Wnt pathway", "autophagy", "neurogenesis", "tau phosphorylation"]
    },
    {
        "name": "Propranolol",
        "approved_for": "Hypertension",
        "drug_class": "beta blocker",
        "mechanism": "non-selective beta adrenergic receptor blocker reduces heart rate anti-anxiety anti-proliferative VEGF inhibition angiogenesis reduction",
        "targets": ["ADRB1", "ADRB2", "VEGF", "MAPK", "ERK"],
        "pathways": ["adrenergic signaling", "heart rate control", "angiogenesis", "VEGF signaling", "cell proliferation"]
    },
    {
        "name": "Finasteride",
        "approved_for": "Benign Prostatic Hyperplasia",
        "drug_class": "5-alpha reductase inhibitor",
        "mechanism": "inhibits 5-alpha reductase converts testosterone to DHT anti-androgenic reduces prostate volume anti-proliferative androgen receptor",
        "targets": ["SRD5A1", "SRD5A2", "DHT", "AR"],
        "pathways": ["androgen metabolism", "DHT signaling", "androgen receptor", "cell proliferation", "hormone signaling"]
    },
    {
        "name": "Hydroxychloroquine",
        "approved_for": "Lupus and Malaria",
        "drug_class": "antimalarial",
        "mechanism": "lysosomotropic agent inhibits toll-like receptor signaling anti-inflammatory autophagy inhibitor reduces cytokine production interferon pathway",
        "targets": ["TLR7", "TLR9", "CQ receptor", "IFN pathway"],
        "pathways": ["TLR signaling", "lysosome function", "autophagy", "interferon pathway", "cytokine production"]
    },
    {
        "name": "Doxycycline",
        "approved_for": "Bacterial Infections",
        "drug_class": "tetracycline antibiotic",
        "mechanism": "protein synthesis inhibitor matrix metalloproteinase inhibitor anti-inflammatory anti-angiogenic neuroprotective MMP inhibition collagen",
        "targets": ["MMP2", "MMP9", "30S ribosome", "NF-kB", "VEGF"],
        "pathways": ["protein synthesis", "MMP pathway", "inflammation", "angiogenesis", "extracellular matrix"]
    },
    {
        "name": "Valproic Acid",
        "approved_for": "Epilepsy",
        "drug_class": "HDAC inhibitor",
        "mechanism": "histone deacetylase inhibitor GABA increase sodium channel blocker neuroprotective epigenetic regulation anti-tumor differentiation inducer",
        "targets": ["HDAC1", "HDAC2", "GABA", "SCN1A", "BCL2"],
        "pathways": ["HDAC pathway", "epigenetic regulation", "GABA signaling", "apoptosis", "neuronal signaling"]
    },
    {
        "name": "Losartan",
        "approved_for": "Hypertension",
        "drug_class": "ARB",
        "mechanism": "angiotensin II receptor type 1 blocker anti-fibrotic renal protection TGF-beta inhibition reduces oxidative stress anti-inflammatory",
        "targets": ["AGTR1", "TGF-B1", "ACE2", "AT1R"],
        "pathways": ["renin angiotensin system", "TGF-beta signaling", "fibrosis", "oxidative stress", "inflammation"]
    },
    {
        "name": "Celecoxib",
        "approved_for": "Arthritis Pain",
        "drug_class": "selective COX-2 inhibitor",
        "mechanism": "selective cyclooxygenase 2 inhibitor anti-inflammatory anti-tumor prostaglandin E2 reduction apoptosis induction angiogenesis inhibition",
        "targets": ["COX2", "PTGS2", "PGE2", "BCL2", "VEGF"],
        "pathways": ["COX-2 pathway", "prostaglandin synthesis", "apoptosis", "angiogenesis", "inflammation"]
    },
    {
        "name": "Itraconazole",
        "approved_for": "Fungal Infections",
        "drug_class": "antifungal",
        "mechanism": "Hedgehog pathway inhibitor anti-angiogenic VEGFR inhibition blocks sterol synthesis Wnt pathway inhibitor anti-proliferative",
        "targets": ["Hedgehog", "VEGFR", "CYP51", "Wnt", "mTOR"],
        "pathways": ["Hedgehog signaling", "angiogenesis", "sterol synthesis", "Wnt pathway", "cell proliferation"]
    },
    {
        "name": "Bromocriptine",
        "approved_for": "Parkinson's Disease",
        "drug_class": "dopamine agonist",
        "mechanism": "dopamine D2 receptor agonist prolactin suppressor insulin sensitizer metabolic regulation hypothalamic activity circadian rhythm",
        "targets": ["DRD2", "DRD3", "PRLR", "AMPK"],
        "pathways": ["dopamine signaling", "prolactin pathway", "insulin signaling", "circadian rhythm", "metabolic regulation"]
    },
    {
        "name": "Colchicine",
        "approved_for": "Gout",
        "drug_class": "anti-inflammatory",
        "mechanism": "microtubule polymerization inhibitor NLRP3 inflammasome inhibition anti-inflammatory neutrophil migration inhibitor IL-1 beta reduction",
        "targets": ["Tubulin", "NLRP3", "IL1B", "ICAM1"],
        "pathways": ["microtubule dynamics", "NLRP3 inflammasome", "IL-1 signaling", "neutrophil function", "inflammation"]
    },
    {
        "name": "Ivermectin",
        "approved_for": "Parasitic Infections",
        "drug_class": "antiparasitic",
        "mechanism": "chloride ion channel activator PAK1 inhibitor anti-tumor Wnt signaling inhibitor nuclear transport importin inhibitor anti-viral",
        "targets": ["GluCl", "PAK1", "importin", "Wnt", "P2X4"],
        "pathways": ["chloride channel", "PAK1 signaling", "Wnt pathway", "nuclear transport", "cell proliferation"]
    }
]


DISEASES = [
    {
        "name": "Alzheimer's Disease",
        "category": "neurological",
        "description": "progressive neurodegenerative disorder amyloid beta plaques tau neurofibrillary tangles neuroinflammation oxidative stress cholinergic deficit cognitive decline memory loss",
        "genes": ["APP", "PSEN1", "APOE", "MAPT", "BACE1", "GSK3B", "NF-kB"],
        "pathways": ["amyloid processing", "tau phosphorylation", "neuroinflammation", "cholinergic signaling", "oxidative stress", "mTOR pathway"]
    },
    {
        "name": "Colorectal Cancer",
        "category": "oncology",
        "description": "colorectal adenocarcinoma tumor proliferation angiogenesis COX-2 overexpression Wnt APC mutation microsatellite instability inflammation driven cancer",
        "genes": ["APC", "KRAS", "TP53", "COX2", "VEGF", "EGFR", "mTOR"],
        "pathways": ["Wnt signaling", "angiogenesis", "COX-2 pathway", "cell proliferation", "apoptosis", "MAPK pathway"]
    },
    {
        "name": "Pulmonary Arterial Hypertension",
        "category": "cardiovascular",
        "description": "pulmonary vascular remodeling smooth muscle cell proliferation vasoconstriction nitric oxide deficiency endothelial dysfunction right heart failure",
        "genes": ["BMPR2", "eNOS", "PDE5A", "ET1", "VEGF", "PDGF"],
        "pathways": ["nitric oxide pathway", "cGMP signaling", "vascular smooth muscle", "pulmonary circulation", "angiogenesis"]
    },
    {
        "name": "Pancreatic Cancer",
        "category": "oncology",
        "description": "pancreatic ductal adenocarcinoma KRAS mutation tumor microenvironment hedgehog pathway stromal desmoplasia mTOR activation anti-angiogenic therapy resistance",
        "genes": ["KRAS", "TP53", "SMAD4", "CDKN2A", "Hedgehog", "mTOR", "VEGF"],
        "pathways": ["Hedgehog signaling", "mTOR pathway", "KRAS signaling", "angiogenesis", "cell proliferation", "apoptosis"]
    },
    {
        "name": "Amyotrophic Lateral Sclerosis",
        "category": "neurological",
        "description": "motor neuron degeneration oxidative stress glutamate excitotoxicity mitochondrial dysfunction protein aggregation neuroinflammation GSK3 activation",
        "genes": ["SOD1", "TDP43", "FUS", "GSK3B", "BCL2", "mTOR"],
        "pathways": ["oxidative stress", "GSK3 signaling", "autophagy", "mitochondrial function", "neuroinflammation", "apoptosis"]
    },
    {
        "name": "PCOS",
        "category": "endocrine",
        "description": "polycystic ovary syndrome insulin resistance hyperandrogenism ovarian dysfunction AMPK dysregulation androgen excess inflammation metabolic syndrome",
        "genes": ["INSR", "AR", "SHBG", "AMPK", "IGF1R", "FSH"],
        "pathways": ["insulin signaling", "androgen metabolism", "AMPK signaling", "inflammation", "hormone signaling"]
    },
    {
        "name": "Multiple Sclerosis",
        "category": "autoimmune",
        "description": "demyelinating autoimmune disease neuroinflammation Th17 cells myelin damage CNS inflammation IL-17 TNF-alpha oxidative stress neuroprotection",
        "genes": ["IL17A", "TNF", "NF-kB", "IL6", "TLR signaling", "BDNF"],
        "pathways": ["neuroinflammation", "TNF signaling", "TLR signaling", "Th17 pathway", "oxidative stress", "neuroprotection"]
    },
    {
        "name": "Breast Cancer",
        "category": "oncology",
        "description": "breast tumor hormone receptor positive HER2 VEGF angiogenesis mTOR AKT PI3K estrogen receptor proliferation anti-apoptosis",
        "genes": ["BRCA1", "BRCA2", "HER2", "ESR1", "VEGF", "mTOR", "PIK3CA"],
        "pathways": ["PI3K/AKT", "mTOR pathway", "estrogen signaling", "angiogenesis", "HER2 signaling", "apoptosis"]
    },
    {
        "name": "Parkinson's Disease",
        "category": "neurological",
        "description": "dopaminergic neuron loss substantia nigra alpha synuclein aggregation Lewy bodies mitochondrial dysfunction oxidative stress neuroinflammation GSK3",
        "genes": ["SNCA", "LRRK2", "PARK2", "GSK3B", "PINK1", "DJ1"],
        "pathways": ["dopamine signaling", "autophagy", "GSK3 signaling", "mitochondrial function", "neuroinflammation", "oxidative stress"]
    },
    {
        "name": "Type 2 Diabetes",
        "category": "metabolic",
        "description": "insulin resistance impaired glucose tolerance pancreatic beta cell dysfunction AMPK dysregulation inflammation oxidative stress metabolic disorder HbA1c",
        "genes": ["INSR", "IRS1", "AMPK", "GLUT4", "PCK1", "TNF"],
        "pathways": ["insulin signaling", "AMPK signaling", "gluconeogenesis", "glucose metabolism", "inflammation", "oxidative stress"]
    },
    {
        "name": "Lupus",
        "category": "autoimmune",
        "description": "systemic lupus erythematosus autoimmune TLR activation type I interferon pathway autoantibodies inflammation NF-kB complement activation cytokine",
        "genes": ["TLR7", "TLR9", "IFNAR", "NF-kB", "IL6", "TNF"],
        "pathways": ["TLR signaling", "interferon pathway", "NF-kB", "complement", "cytokine production", "inflammation"]
    },
    {
        "name": "Liver Fibrosis",
        "category": "hepatic",
        "description": "hepatic stellate cell activation TGF-beta collagen deposition oxidative stress inflammation fibrotic remodeling RAAS activation angiotensin",
        "genes": ["TGF-B1", "AGTR1", "SMAD3", "COL1A1", "MMP2", "TIMP1"],
        "pathways": ["TGF-beta signaling", "renin angiotensin system", "fibrosis", "MMP pathway", "oxidative stress", "inflammation"]
    },
    {
        "name": "Ovarian Cancer",
        "category": "oncology",
        "description": "epithelial ovarian tumor VEGF angiogenesis platinum resistance HDAC epigenetic dysregulation PI3K mTOR hormonal androgen receptor signaling",
        "genes": ["BRCA1", "BRCA2", "VEGF", "TP53", "AR", "HDAC1", "mTOR"],
        "pathways": ["angiogenesis", "HDAC pathway", "PI3K/AKT", "mTOR pathway", "androgen receptor", "apoptosis"]
    },
    {
        "name": "COVID-19",
        "category": "infectious",
        "description": "SARS-CoV-2 infection cytokine storm ACE2 receptor entry viral replication TLR signaling immune dysregulation NF-kB inflammatory cascade",
        "genes": ["ACE2", "TMPRSS2", "IL6", "TNF", "NF-kB", "TLR7", "importin"],
        "pathways": ["ACE2 signaling", "TLR signaling", "cytokine production", "NF-kB", "interferon pathway", "nuclear transport"]
    },
    {
        "name": "Cardiac Fibrosis",
        "category": "cardiovascular",
        "description": "cardiac extracellular matrix remodeling TGF-beta fibroblast activation collagen deposition heart failure angiotensin II RAAS oxidative stress",
        "genes": ["TGF-B1", "AGTR1", "COL1A1", "MMP9", "CTGF", "ACE"],
        "pathways": ["TGF-beta signaling", "renin angiotensin system", "fibrosis", "oxidative stress", "cardiac remodeling", "MMP pathway"]
    },
]


KNOWN_POSITIVE_PAIRS = [
    ("Metformin", "Alzheimer's Disease"),
    ("Metformin", "Breast Cancer"),
    ("Metformin", "PCOS"),
    ("Sildenafil", "Pulmonary Arterial Hypertension"),
    ("Aspirin", "Colorectal Cancer"),
    ("Thalidomide", "COVID-19"),
    ("Rapamycin", "Breast Cancer"),
    ("Rapamycin", "Pancreatic Cancer"),
    ("Atorvastatin", "Alzheimer's Disease"),
    ("Ibuprofen", "Alzheimer's Disease"),
    ("Lithium", "Alzheimer's Disease"),
    ("Lithium", "Amyotrophic Lateral Sclerosis"),
    ("Methotrexate", "Lupus"),
    ("Hydroxychloroquine", "COVID-19"),
    ("Hydroxychloroquine", "Lupus"),
    ("Doxycycline", "Pancreatic Cancer"),
    ("Valproic Acid", "Breast Cancer"),
    ("Valproic Acid", "Ovarian Cancer"),
    ("Losartan", "Liver Fibrosis"),
    ("Losartan", "Cardiac Fibrosis"),
    ("Celecoxib", "Colorectal Cancer"),
    ("Celecoxib", "Breast Cancer"),
    ("Itraconazole", "Pancreatic Cancer"),
    ("Bromocriptine", "Type 2 Diabetes"),
    ("Propranolol", "Breast Cancer"),
    ("Finasteride", "PCOS"),
    ("Colchicine", "Cardiac Fibrosis"),
    ("Colchicine", "COVID-19"),
    ("Ivermectin", "Breast Cancer"),
    ("Doxycycline", "Ovarian Cancer"),
]
