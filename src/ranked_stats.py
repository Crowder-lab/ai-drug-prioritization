import marimo

__generated_with = "0.14.10"
app = marimo.App(
    width="medium",
    css_file="/Users/dunb/.config/marimo/default.css",
)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    original_cols_before_ranking = ["Main Name", "DrugBank:Main Name", "Clinician Recommendation", "DrugBank:Match Found", "DrugBank:FDA Approved", "DrugBank:Prices", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury"]
    translator_cols_before_ranking = ["Main Name", "DrugBank:Main Name", "DrugBank:Match Found", "DrugBank:FDA Approved", "DrugBank:Prices", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury"]
    cols = ["Main Name", "DrugBank:Main Name", "score", "Clinician Recommendation", "DrugBank:FDA Approved", "Less than $500",  "Pediatric Safety", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury", "Data Source"]
    return cols, original_cols_before_ranking, translator_cols_before_ranking


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
def _(original_cols_before_ranking, pd, remove_newlines):
    original_list = pd.read_json("data/drug_list.json")
    for to_be_booled in ("DrugBank:FDA Approved", "Have It", "Screened", "Not In DrugBank", "ED Pediatric Safety"):
        original_list[to_be_booled] = original_list[to_be_booled].fillna(False).astype(bool)
    remaining_original_cols = [column for column in original_list.columns if column not in original_cols_before_ranking]
    remove_newlines(original_list[original_cols_before_ranking + remaining_original_cols])
    return


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
    result = combined[cols].sort_values("Data Source").drop_duplicates("Main Name", keep="first").sort_values(["score", "Main Name"], ascending=[False, True])
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
def _(clin_recs, result):
    the_2s = result["score"] >= 2
    to_check_safety = the_2s | clin_recs
    print(to_check_safety.sum())
    result[to_check_safety]
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
