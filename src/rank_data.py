#!/usr/bin/env uv run

import pandas as pd

BOLD_TEXT = "\033[1m"
DEFAULT_TEXT = "\033[0m"

data = pd.read_csv("data/drug_list.csv")
data["score"] = 0

# NOTE: what if the drug isn't meant for oral route?
# \infty: is bioavailable
data = data[(data["Bioavailability"] >= 0.5) | data["SMILES"].isna()]

# \infty: crosses blood brain barrier
data = data[(data["BloodBrainBarrier"] >= 0.5) | data["SMILES"].isna()]

# \infty: is absorbed by human intestine
data = data[(data["HumanIntestinalAbsorption"] >= 0.5) | data["SMILES"].isna()]

# 1: FDA approved
data["score"] += data["FDAApproved"].fillna(False)

# 1: cost less than $100
data["Less than $100"] = (
    data["Price"]
    .fillna("Inf")
    .str.split(";")
    .apply(lambda price_list: max(tuple(map(lambda s: float(s.removesuffix("USD")), price_list))))
    < 100
)
data["score"] += data["Less than $100"]

# 1: cost less than $1000
data["Less than $1000"] = (
    data["Price"]
    .fillna("Inf")
    .str.split(";")
    .apply(lambda price_list: max(tuple(map(lambda s: float(s.removesuffix("USD")), price_list))))
    < 1000
)
data["score"] += data["Less than $1000"]

# 0-2: side effect score
data["Side Effect Score"] = 3 - data["EDSideEffectRank"].fillna(2)
data["score"] += data["Side Effect Score"]

# 1-2: safety
data["Safety"] = data["EDPediatricSafety"].fillna(False).astype(int) + data["FDAApproved"].fillna(False).astype(int)
data["score"] += data["Safety"]

# fixes
data["Screened"] = data["Screened"].fillna(False)

# get results
CATEGORIES = (
    "anti-inflammatory",
    "antimicrobial",
    "immunomodulators",
    "increase dopamine signaling",
    "increase gaba signaling",
    "increase neuroplasticity",
    "kinase inhibitor",
    "neuroprotective",
    "protein of interest modulator",
    "symptomatic relief",
)
for category in CATEGORIES:
    unscreened = data[data["Screened"] == False]
    print(BOLD_TEXT + category.upper() + DEFAULT_TEXT)
    print(
        unscreened[unscreened["RepurposingCategory"].str.contains(category)].sort_values(by="score", ascending=False)[
            [
                "CanonicalName",
                "NotInDrugBank",
                "score",
                "FDAApproved",
                "Less than $100",
                "Less than $1000",
                "Side Effect Score",
                "Safety",
            ]
        ]
    )
    print()
