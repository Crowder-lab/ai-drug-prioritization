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
def _(pd):
    combined = pd.read_csv("data/ranked.csv")
    cols = ["DrugBank Name", "score", "FDA Approved", "Less than $100", "Less than $1000", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury", "Pediatric Safety"]
    result = combined[cols].sort_values(["score", "DrugBank Name"], ascending=[False, True]).drop_duplicates("DrugBank Name").reset_index()
    return (result,)


@app.cell
def _(result):
    result
    return


@app.cell
def _(result):
    result["Pediatric Safety"].sum()
    return


@app.cell
def _(result):
    result
    return


@app.cell
def _(result):
    intestinal_absorption = result[result["Human Intestinal Absorption"] > 0.5]
    print(len(intestinal_absorption))
    bbb = intestinal_absorption[(intestinal_absorption["Blood Brain Barrier"] > 0.5) | (intestinal_absorption["P-glycoprotein Inhibition"] > 0.5)]
    print(len(bbb))
    return


@app.cell
def _(result):
    score_no_pediatric = result["score"] - result["Pediatric Safety"]
    print(sum(score_no_pediatric >= 4))
    return


@app.cell
def _(result):
    no_pediatric = result[(result["score"] - result["Pediatric Safety"]) >= 4].copy(deep=True)
    no_pediatric["score"] -= no_pediatric["Pediatric Safety"]
    no_pediatric.drop("Pediatric Safety", axis="columns")
    return


@app.cell
def _(result):
    print(sum(result["score"] >= 5))
    return


@app.cell
def _(result):
    good_drugs = result[result["score"] >= 5]
    good_drugs
    return (good_drugs,)


@app.cell
def _(pd):
    original_list = pd.read_json("data/drug_list.json")
    original_list
    return (original_list,)


@app.cell
def _(good_drugs, original_list):
    with_screening = good_drugs.merge(original_list[["DrugBank Name", "Have It", "Screened"]], on="DrugBank Name", how="left")
    with_screening[with_screening["Have It"] == 1]
    return


if __name__ == "__main__":
    app.run()
