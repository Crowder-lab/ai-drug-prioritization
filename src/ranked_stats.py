import marimo

__generated_with = "0.17.0"
app = marimo.App(
    width="medium",
    css_file="/Users/dunb/.config/marimo/default.css",
)


@app.cell
def _():
    import json

    import pandas as pd
    return json, pd


@app.cell
def _():
    original_cols_before_ranking = ["Main Name", "DrugBank:Main Name", "Clinician Recommendation", "DrugBank:Match Found", "DrugBank:FDA Approved", "DrugBank:Prices", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury"]
    translator_cols_before_ranking = ["Main Name", "DrugBank:Main Name", "DrugBank:Match Found", "DrugBank:FDA Approved", "DrugBank:Prices", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury"]
    cols = ["Main Name", "DrugBank:Main Name", "score", "Clinician Recommendation", "DrugBank:FDA Approved", "Less than $500",  "Pediatric Safety", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury"]
    return cols, translator_cols_before_ranking


@app.cell
def _(pd):
    def remove_newlines(df: pd.DataFrame) -> pd.DataFrame:
        df_copy = df.copy()

        # Select only object (string) columns
        string_columns = df_copy.select_dtypes(include='object').columns

        # Apply replacement: remove \n and \r
        for col in string_columns:
            df_copy[col] = df_copy[col].astype(str).str.replace(r'[\r\n]+', ' ', regex=True)

        return df_copy
    return (remove_newlines,)


@app.cell
def _(pd, remove_newlines, translator_cols_before_ranking):
    translator_list = pd.read_json("data/translator_drug_list.json")
    for to_be_booled_2 in ("DrugBank:FDA Approved",):
        translator_list[to_be_booled_2] = translator_list[to_be_booled_2].fillna(False).astype(bool)
    remaining_translator_cols = [column for column in translator_list.columns if column not in translator_cols_before_ranking]
    remove_newlines(translator_list[translator_cols_before_ranking + remaining_translator_cols])
    return


@app.cell
def _(cols, pd):
    combined = pd.read_csv("data/ranked.csv")
    result = combined[cols].sort_values(["score", "Main Name"], ascending=[False, True])
    result["DrugBank:FDA Approved"] = result["DrugBank:FDA Approved"].fillna(False).astype(bool)
    return (result,)


@app.cell
def _(result):
    clin_recs = result["Clinician Recommendation"]
    result.reset_index()
    return (clin_recs,)


@app.cell
def _(result):
    intestinal_absorption = result[(result["Human Intestinal Absorption"] > 0.5) | result["DrugBank:Main Name"].isna()]
    print("Passes HIA             :", len(intestinal_absorption))
    bbb = intestinal_absorption[(intestinal_absorption["Blood Brain Barrier"] > 0.5) | (intestinal_absorption["P-glycoprotein Inhibition"] > 0.5) | intestinal_absorption["DrugBank:Main Name"].isna()]
    print("Passes HIA + BBB       :", len(bbb))
    dili = bbb[(bbb["Drug Induced Liver Injury"] > 0.5) | bbb["DrugBank:Main Name"].isna()]
    print("Passes HIA + BBB + DILI:", len(dili))
    return


@app.cell
def _(result):
    ((result["score"] >= 1) & result["DrugBank:FDA Approved"] & result["Less than $500"]).sum()
    return


@app.cell
def _(clin_recs, result):
    the_2s = result["score"] >= 2
    to_check_safety = the_2s | clin_recs
    print(to_check_safety.sum())
    result[to_check_safety]
    return (to_check_safety,)


@app.cell
def _(json, result, to_check_safety):
    with open("data/pubchat/answers.json", "r") as f:
        pubchat = json.load(f)
    pubchat_names = set(map(lambda output: output["name"].strip().lower(), pubchat))
    for name in result[to_check_safety]["DrugBank:Main Name"]:
        if name.strip().lower() not in pubchat_names:
            print(f"ERROR: {name} missing from PubChat results")
    return


@app.cell
def _(clin_recs, result):
    post_pediatric_2s = (result["score"] - result["Pediatric Safety"]) >= 2
    post_pediatric_safety_check = post_pediatric_2s | clin_recs
    print(post_pediatric_safety_check.sum())
    post_pediatric_result = result.copy(deep=True)
    post_pediatric_result["score"] -= post_pediatric_result["Pediatric Safety"]
    post_pediatric_result
    return


@app.cell
def _(clin_recs, result):
    the_3s = result["score"] >= 3
    to_be_clinician_ranked = the_3s | clin_recs
    print(to_be_clinician_ranked.sum())
    result[to_be_clinician_ranked]
    return


if __name__ == "__main__":
    app.run()