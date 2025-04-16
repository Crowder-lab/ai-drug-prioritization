#!/usr/bin/env uv run

import pandas as pd

data = pd.read_csv("data/drug_list.csv")
data["score"] = 0

# \infty: crosses blood brain barrier
data = data[data["BloodBrainBarrier"] > 0.5]

# 1: FDA approved
data["score"] += data["FDAApproved"].fillna(False)

# 1: cost less than $100
data["score"] += (
    data["Price"]
    .fillna("Inf")
    .str.split(";")
    .apply(lambda price_list: max(tuple(map(lambda s: float(s.removesuffix("USD")), price_list))))
    < 100
)

# 1: cost less than $1000
data["score"] += (
    data["Price"]
    .fillna("Inf")
    .str.split(";")
    .apply(lambda price_list: max(tuple(map(lambda s: float(s.removesuffix("USD")), price_list))))
    < 1000
)

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
    print("\033[1m" + category.upper() + "\033[0m")
    print(
        unscreened[unscreened["RepurposingCategory"].str.contains(category)].sort_values(by="score", ascending=False)[
            ["CanonicalName", "score"]
        ]
    )
    print()
