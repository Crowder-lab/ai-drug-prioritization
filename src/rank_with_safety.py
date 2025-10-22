#!/usr/bin/env uv run
import json
import re

import pandas as pd


def unwrap_list(x):
    return (x[0] if len(x) > 0 else None) if isinstance(x, list) else x


def is_safe(chatgpt_output):
    correct_regexp = re.compile("<explain>.*</explain>.*<answer>.*</answer>", re.DOTALL)
    answer_regexp = re.compile("<answer>(.*)</answer>", re.DOTALL)
    return (
        # .find() returns -1 if string not found
        re.search(answer_regexp, chatgpt_output)[0].lower().find("yes") != -1
        if re.match(correct_regexp, chatgpt_output)
        else False
    )


def prices_analysis(price_list):
    if isinstance(price_list, str):
        price_list = [price_list]

    if price_list is None or len(price_list) == 0:
        price_list = ["InfUSD"]

    return max(tuple(map(lambda s: float(s.removesuffix("USD")), price_list)))


# open data
with open("data/pubchat/answers.json", "r") as f:
    answers = json.load(f)
with open("data/translator_drug_list.json", "r") as f:
    data = pd.read_json(f)

# set up some columns
data["Clinician Recommendation"] = False
data["Screened"] = False

# process pediatric safety from pubchat
data["Pediatric Safety"] = False
for answer in answers:
    data.loc[data["DrugBank:Main Name"] == answer["name"], "Pediatric Safety"] = is_safe(answer["answer"])


# start scoring!
data["score"] = 0
very_large_number = 1000000000.0

# exclude drugs completely for these
data.loc[(data["Blood Brain Barrier"] < 0.5) & (data["P-glycoprotein Inhibition"] < 0.5), "score"] -= very_large_number
data.loc[data["Human Intestinal Absorption"] < 0.5, "score"] -= very_large_number
data.loc[data["Drug Induced Liver Injury"] > 0.5, "score"] -= very_large_number

# 1: FDA approved
data["score"] += data["DrugBank:FDA Approved"].apply(unwrap_list).fillna(False)

# 1: Cost less than $500
data["Less than $500"] = data["DrugBank:Prices"].apply(prices_analysis) < 500
data["score"] += data["Less than $500"]

# 1: Safe in children
data["score"] += data["Pediatric Safety"]

# sort 'n' save
data.sort_values(by="score", ascending=False, inplace=True)
with open("data/ranked.csv", "w") as f:
    data.to_csv(f, index=False)
