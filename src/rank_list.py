#!/usr/bin/env -S uv run

import json
import os
import re

import pandas as pd


def unwrap_list(x):
    return (x[0] if len(x) > 0 else None) if isinstance(x, list) else x


def remove_newlines(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()

    # Select only object (string) columns
    string_columns = df_copy.select_dtypes(include="object").columns

    # Apply replacement: remove \n and \r
    for col in string_columns:
        df_copy[col] = df_copy[col].astype(str).str.replace(r"[\r\n]+", " ", regex=True)

    return df_copy


def is_safe(chatgpt_output):
    correct_regexp = re.compile("<explain>.*</explain>.*<answer>.*</answer>", re.DOTALL)
    answer_regexp = re.compile("<answer>(.*)</answer>", re.DOTALL)
    return (
        re.search(answer_regexp, chatgpt_output)[0].lower().find("yes") != -1
        if re.match(correct_regexp, chatgpt_output)
        else False
    )


with open(os.path.join("data", "pubchat", "answers.json"), "r") as f:
    answers = json.load(f)

translator_file = os.path.join("data", "augmented_translator_drugs.json")
extra_file = os.path.join("data", "augmented_extra_drugs.json")
if os.path.exists(translator_file):
    if os.path.exists(extra_file):
        with open(extra_file, "r") as f:
            initial_data = pd.read_json(f)
        with open(translator_file, "r") as f:
            translator_data = pd.read_json(f)

        initial_data["Data Source"] = "extra"
        translator_data["Data Source"] = "translator"

        same_cols = list(set.intersection(set(initial_data.columns), set(translator_data.columns)))
        data = pd.concat((initial_data[same_cols], translator_data[same_cols]), ignore_index=True)
    else:
        with open(translator_file, "r") as f:
            data = pd.read_json(f)
        data["Data Source"] = "translator"
else:
    if os.path.exists(extra_file):
        with open(extra_file, "r") as f:
            data = pd.read_json(f)
        data["Data Source"] = "extra"
    else:
        print(f"At least one of these files needs to exist to run:\n\t{translator_file}\n\t{extra_file}")
        exit()


data["Pediatric Safety"] = False
for answer in answers:
    data.loc[data["DrugBank:Main Name"].str.lower() == answer["name"].lower(), "Pediatric Safety"] = is_safe(
        answer["answer"]
    )


data["score"] = 0
very_large_number = 1000000000.0

data.loc[(data["Blood Brain Barrier"] < 0.5) & (data["P-glycoprotein Inhibition"] < 0.5), "score"] -= very_large_number
data.loc[data["Human Intestinal Absorption"] < 0.5, "score"] -= very_large_number
data.loc[data["Drug Induced Liver Injury"] > 0.5, "score"] -= very_large_number
data["score"] += data["DrugBank:FDA Approved"].apply(unwrap_list).fillna(False)


def max_price(l):
    if isinstance(l, str):
        l = [l]

    if l is None or len(l) == 0:
        l = ["InfUSD"]

    return max(tuple(map(lambda s: float(s.removesuffix("USD")), l)))


data["Less than $500"] = data["DrugBank:Prices"].apply(max_price) < 500
data["score"] += data["Less than $500"]
data["score"] += data["Pediatric Safety"]
data.sort_values(by="score", ascending=False, inplace=True)

# print out stats
print(f"Total drugs:\t{len(data)}")
print("")
hia = data[data["Human Intestinal Absorption"] >= 0.5]
print(f"Passes HIA:\t{len(hia)}")
bbb = hia[(hia["Blood Brain Barrier"] >= 0.5) | (hia["P-glycoprotein Inhibition"] >= 0.5)]
print(f"Passes BBB:\t{len(bbb)}")
dili = bbb[bbb["Drug Induced Liver Injury"] < 0.5]
print(f"Passes DILI:\t{len(dili)}")
print("")
fda = dili[dili["DrugBank:FDA Approved"].apply(unwrap_list).astype(bool)]
print(f"FDA approved:\t{len(fda)}")
lt500 = fda[fda["Less than $500"]]
print(f"Less than $500:\t{len(lt500)}")
safe = lt500[lt500["Pediatric Safety"]]
print(f"Child safe:\t{len(safe)}")


with open(os.path.join("data", "ranked.csv"), "w") as f:
    ranked = remove_newlines(data)
    data.to_csv(f, index=False)

with open(os.path.join("data", "threes.csv"), "w") as f:
    threes = remove_newlines(data[data["score"] == 3])
    threes[
        [
            "Main Name",
            "DrugBank:Main Name",
            "score",
            "DrugBank:FDA Approved",
            "Less than $500",
            "Pediatric Safety",
            "Blood Brain Barrier",
            "P-glycoprotein Inhibition",
            "Human Intestinal Absorption",
            "Drug Induced Liver Injury",
            "Data Source",
        ]
    ].to_csv(f, index=False)
