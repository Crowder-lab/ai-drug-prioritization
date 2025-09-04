#!/usr/bin/env uv run
import re

import pandas as pd
import requests

drug_name = "amantadine"

# Step 1: Fetch data from the FDA API
url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{drug_name}&limit=1000"
response = requests.get(url)
data = response.json().get("results", [])


# Step 2: Extract relevant fields
def extract(entry):
    try:
        return {
            "application_number": entry["openfda"]["application_number"][0],
            "brand_name": entry["openfda"]["brand_name"][0],
            "generic_name": entry["openfda"]["generic_name"][0],
            "route": entry["openfda"]["route"][0],
            "effective_time": int(entry["effective_time"]),
            "pediatric_use": " ".join(entry.get("pediatric_use", [])),
        }
    except (KeyError, IndexError):
        return None


records = [extract(e) for e in data]
df = pd.DataFrame([r for r in records if r is not None])

# Step 3: Filter for exact generic_name == drug name (case-insensitive)
df = df[df["generic_name"].str.lower() == drug_name]

# Step 4: Remove entries without a pediatric_use section
df = df[df["pediatric_use"].str.strip() != ""]


# Step 5: Normalize pediatric_use text
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


df["pediatric_use_normalized"] = df["pediatric_use"].map(normalize)
df["word_tokens"] = df["pediatric_use_normalized"].map(lambda s: set(s.split()))

# Step 6: Keep the most recent label per application number
df = df.sort_values("effective_time", ascending=False)
df = df.drop_duplicates(subset="application_number", keep="first")

# Step 7: Group by route and deduplicate by 3-word difference
final_groups = []

for route, group in df.groupby("route"):
    seen = []
    unique_rows = []

    for _, row in group.iterrows():
        tokens = row["word_tokens"]
        is_duplicate = False

        for seen_tokens in seen:
            if len(tokens.symmetric_difference(seen_tokens)) <= 3:
                is_duplicate = True
                break

        if not is_duplicate:
            seen.append(tokens)
            unique_rows.append(row)

    final_groups.append(pd.DataFrame(unique_rows))

# Step 8: Combine and display final results
result_df = pd.concat(final_groups)
result_df = result_df[["application_number", "brand_name", "route", "effective_time", "pediatric_use"]]

# Output
pd.set_option("display.max_colwidth", None)
print(result_df.to_string(index=False))

# Optional: Save to file and print file location
result_df.to_csv(f"deduplicated_{drug_name}_labels.csv", index=False)
import os

print("\nSaved to:", os.path.abspath("deduplicated_amoxicillin_labels.csv"))
