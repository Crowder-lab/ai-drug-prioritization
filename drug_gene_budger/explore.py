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
    results = pd.read_excel("drug_gene_budger/DGB_results_MAPK8IP3.xlsx", sheet_name="l1000_results_up")
    results.sort_values("Fold Change", ascending=False).reset_index()
    return (results,)


@app.cell
def _(results):
    combined = results.groupby("Drug Name").agg(lambda x: set(x))
    combined["Max Fold Change"] = combined["Fold Change"].apply(lambda s: max(s))
    combined = combined.sort_values("Max Fold Change", ascending=False).reset_index()
    combined
    return


if __name__ == "__main__":
    app.run()
