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
        re.search(answer_regexp, chatgpt_output)[0].lower().find("yes") != -1
        if re.match(correct_regexp, chatgpt_output)
        else False
    )


with open("data/pubchat/answers.json", "r") as f:
    answers = json.load(f)
with open("data/drug_list.json", "r") as f:
    initial_data = pd.read_json(f)
with open("data/translator_drug_list.json", "r") as f:
    translator_data = pd.read_json(f)

translator_data["Clinician Recommendation"] = False
translator_data["Screened"] = False
initial_data["Data Source"] = "original"
translator_data["Data Source"] = "translator"

same_cols = list(set.intersection(set(initial_data.columns), set(translator_data.columns)))
data = pd.concat((initial_data[same_cols], translator_data[same_cols]), ignore_index=True)

data["Pediatric Safety"] = False
for answer in answers:
    data.loc[data["DrugBank:Main Name"] == answer["name"], "Pediatric Safety"] = is_safe(answer["answer"])


data["score"] = 0
very_large_number = 1000000000.0

data.loc[(data["Blood Brain Barrier"] < 0.5) & (data["P-glycoprotein Inhibition"] < 0.5), "score"] -= very_large_number
data.loc[data["Human Intestinal Absorption"] < 0.5, "score"] -= very_large_number
data.loc[data["Drug Induced Liver Injury"] > 0.5, "score"] -= very_large_number
data["score"] += data["DrugBank:FDA Approved"].apply(unwrap_list).fillna(False)


def _hy_anon_var_6(l):
    if isinstance(l, str):
        l = [l]

    if l is None or len(l) == 0:
        l = ["InfUSD"]

    return max(tuple(map(lambda s: float(s.removesuffix("USD")), l)))


data["Less than $500"] = data["DrugBank:Prices"].apply(_hy_anon_var_6) < 500
data["score"] += data["Less than $500"]
data["score"] += data["Pediatric Safety"]
data.sort_values(by="score", ascending=False, inplace=True)

with open("data/ranked.csv", "w") as f:
    data.to_csv(f, index=False)
