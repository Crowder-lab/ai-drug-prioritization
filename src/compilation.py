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
    cols = ["DrugBank Name", "score", "FDA Approved", "Less than $100", "Less than $1000", "Blood Brain Barrier", "P-glycoprotein Inhibition", "Human Intestinal Absorption", "Drug Induced Liver Injury"]
    translator = pd.read_csv("data/translator_ranked.csv")[cols]
    initial = pd.read_csv("data/ranked.csv")[cols + ["Pediatric Safety", "Screened", "Clinician Recommendation"]]
    initial["score"] -= initial["Pediatric Safety"].fillna(False)
    initial = initial.drop("Pediatric Safety", axis=1)
    return initial, translator


@app.cell
def _(initial, pd, translator):
    combined = pd.concat([initial, translator], ignore_index=True)
    result = (combined
        .drop_duplicates(subset="DrugBank Name", keep="first")
        .sort_values(["score", "DrugBank Name"], ascending=[False, True])
        .reset_index()
    )
    result["FDA Approved"] = result["FDA Approved"].fillna(0).astype(bool)
    result["Screened"] = result["Screened"].fillna(0).astype(bool)
    return (result,)


@app.cell
def _(result):
    result.drop("index", axis=1)
    return


@app.cell
def _(result):
    print(f"Total count: {len(result)}")
    print(f"Good ADMET: {len(result[result['score'] >= 0])}")
    print(f"Above 3: {len(result[result['score'] >= 4])}")
    return


@app.cell
def _(result):
    all_3s = result[result["score"] >= 4]
    all_3s.drop("index", axis=1)
    return


@app.cell
def _(result):
    screened_3s = result[(result["score"] >= 4) & result["Screened"]].reset_index()
    screened_3s.drop("index", axis=1)
    return


@app.cell
def _(result):
    all_screened = result[result["Screened"]].reset_index()
    all_screened.drop("index", axis=1)
    return


if __name__ == "__main__":
    app.run()
