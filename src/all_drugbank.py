import marimo

__generated_with = "0.14.10"
app = marimo.App(
    width="medium",
    css_file="/Users/dunb/.config/marimo/default.css",
)


@app.cell
def _():
    import xml.etree.ElementTree as ET

    import catboost as cb
    import marimo as mo
    import numpy as np
    import pandas as pd
    from rdkit import Chem, RDLogger
    from tqdm import tqdm

    import maplight_gnn
    return Chem, ET, RDLogger, cb, maplight_gnn, np, pd, tqdm


@app.cell
def _(Chem, ET, RDLogger, cb, maplight_gnn, np, pd, tqdm):
    class DrugBank:
        namespaces = {"": "http://www.drugbank.ca"}

        def __init__(self, filename: str):
            self.filename = filename
            # self.ids = ids
            # self.id_types = id_types
            # self.names = names.str.lower()
            self.get_ids = {
                "cas-number": self.cas_number,
                "ChEBI": self.chebi,
                "ChEMBL": self.chembl,
                "drugbank-id": self.drugbank,
                "InChIKey": self.inchikey,
                "PubChem Compound": self.pubchem_compound,
                "PubChem Substance": self.pubchem_substance,
                "unii": self.unii,
            }

        def generate_dataframe(self) -> None:
            df_dict = {
                "DrugBank:Main Name": [],
                "DrugBank:Identifiers": [],
                "DrugBank:All Names": [],
                "DrugBank:Type": [],
                "DrugBank:FDA Approved": [],
                "DrugBank:Prices": [],
                "DrugBank:Indication": [],
                "DrugBank:Mechanism": [],
                "DrugBank:SMILES": [],
            }

            for _, element in tqdm(ET.iterparse(self.filename, ["end"])):
                if (element.tag[24:] != "drug") or (element.attrib == {}):
                    continue
                df_dict["DrugBank:Main Name"].append(self.name(element))
                df_dict["DrugBank:Identifiers"].append({k: v(element) for k, v in self.get_ids.items()})
                df_dict["DrugBank:All Names"].append(self.all_names(element))
                df_dict["DrugBank:Type"].append(element.get("type"))
                df_dict["DrugBank:FDA Approved"].append(self.fda_approval(element))
                df_dict["DrugBank:Prices"].append(self.prices(element))
                df_dict["DrugBank:Indication"].append(self.indication(element))
                df_dict["DrugBank:Mechanism"].append(self.mechanism(element))
                df_dict["DrugBank:SMILES"].append(self.smiles(element))

            self.df = pd.DataFrame(df_dict)

        def all_names(self, element):
            generic_names = set()
            brand_names = set()
            main_name = self.name(element)
            generic_names.add(main_name.lower()) if main_name is not None else None
            it = element.find("synonyms", self.namespaces)
            if it is not None:
                for synonym in it.iter():
                    generic_names.add(
                        synonym.text.lower()
                    ) if synonym is not None and synonym.text is not None else None

            it = element.find("products", self.namespaces)
            if it is not None:
                for product in it.iter():
                    brand_name = product.find("name", self.namespaces)
                    brand_names.add(brand_name.text.lower()) if brand_name is not None else None

            generic_names = tuple(filter(lambda s: "\n" not in s, generic_names))
            brand_names = tuple(filter(lambda s: "\n" not in s, brand_names))
            return (generic_names, brand_names)

        def cas_number(self, element):
            it = element.find("cas-number", self.namespaces)
            return it.text if it is not None else None

        def chebi(self, element):
            return self.from_external_identifiers(element, "ChEBI")

        def chembl(self, element):
            return self.from_external_identifiers(element, "ChEMBL")

        def drugbank(self, element):
            it = element.find("drugbank-id", self.namespaces)
            return it.text if it is not None else None

        def fda_approval(self, element):
            it = element.find("groups", self.namespaces)
            return "approved" in tuple(it.itertext()) if it is not None else None

        def inchikey(self, element):
            return self.from_calculated_properties(element, "InChIKey")

        def indication(self, element):
            it = element.find("indication", self.namespaces)
            return it.text if it is not None else None

        def mechanism(self, element):
            it = element.find("mechanism-of-action", self.namespaces)
            return it.text if it is not None else None

        def name(self, element):
            it = element.find("name", self.namespaces)
            return it.text if it is not None else None

        def prices(self, element):
            it = element.find("prices", self.namespaces)
            if it is not None:
                prices = list()
                for price_element in it.iterfind("price", self.namespaces):
                    price = price_element.find("cost", self.namespaces)
                    prices.append(
                        price.text + price.attrib.get("currency")
                    ) if price is not None else None
                return prices
            return None

        def pubchem_compound(self, element):
            return self.from_external_identifiers(element, "PubChem Compound")

        def pubchem_substance(self, element):
            return self.from_external_identifiers(element, "PubChem Substance")

        def smiles(self, element):
            return self.from_calculated_properties(element, "SMILES")

        def unii(self, element):
            it = element.find("unii", self.namespaces)
            return it.text if it is not None else None

        def from_external_identifiers(self, element, resource_type):
            it = element.find("external-identifiers", self.namespaces)
            if it is not None:
                for external_identifier in it.iterfind("external-identifier", self.namespaces):
                    if (
                        external_identifier.findtext("resource", namespaces=self.namespaces)
                        == resource_type
                    ):
                        return external_identifier.findtext("identifier", namespaces=self.namespaces)
            return None

        def from_calculated_properties(self, element, kind_type):
            it = element.find("calculated-properties", self.namespaces)
            if it is not None:
                for property in it.iterfind("property", self.namespaces):
                    if property.findtext("kind", namespaces=self.namespaces) == kind_type:
                        return property.findtext("value", namespaces=self.namespaces)
            return None

        def load_admet_models(self, models):
            self.admet_models = dict()
            for name, path in models.items():
                model = cb.CatBoostClassifier()
                model.load_model(path)
                self.admet_models[name] = model
            return self

        def predict_admet(self):
            RDLogger.DisableLog("rdApp.*")
            smiles_mask = self.df["DrugBank:SMILES"].notna()
            smiles = self.df.loc[smiles_mask, "DrugBank:SMILES"]
            molecules = smiles.apply(Chem.MolFromSmiles)
            # solves this error message:
            # > molfeat.trans.pretrained.dgl_pretrained:graph_featurizer:283 - rdkit.Chem.rdchem.BondType.DATIVE is not in list
            # if this happens again, adjust the lambda appropriately
            no_dative_bond = molecules.apply(
                lambda mol: (
                    Chem.rdchem.BondType.DATIVE
                    not in map(lambda bond: bond.GetBondType(), mol.GetBonds())
                )
                if mol is not None
                else False
            )
            molecules_mask = molecules.notna() & no_dative_bond
            fingerprints = self.get_fingerprints(molecules[molecules_mask])
            combined_mask = pd.Series(False, index=self.df.index)
            combined_mask.loc[smiles[molecules_mask].index] = True
            for name, model in self.admet_models.items():
                predictions = model.predict_proba(fingerprints)
                self.df.loc[combined_mask, name] = predictions[slice(None, None), 1]

        def get_fingerprints(self, molecules):
            fingerprints = list()
            fingerprints.append(maplight_gnn.get_morgan_fingerprints(molecules))
            fingerprints.append(maplight_gnn.get_avalon_fingerprints(molecules))
            fingerprints.append(maplight_gnn.get_erg_fingerprints(molecules))
            fingerprints.append(maplight_gnn.get_rdkit_features(molecules))
            fingerprints.append(maplight_gnn.get_gin_supervised_masking(molecules))
            return np.concatenate(fingerprints, axis=1)
    return (DrugBank,)


@app.cell
def _(DrugBank):
    db = DrugBank("data/src/drugbank.xml")
    db.generate_dataframe()
    db.load_admet_models(
        {
            "Blood Brain Barrier": "data/admet/bbb_martins-0.916-0.002.dump",
            "P-glycoprotein Inhibition": "data/admet/pgp_broccatelli-0.938-0.0.dump",
            "Human Intestinal Absorption": "data/admet/hia_hou-0.989-0.001.dump",
            "Drug Induced Liver Injury": "data/admet/dili-0.918-0.005.dump",
        }
    )
    db.predict_admet()
    db.df.to_csv("data/all_drugbank.csv")
    db.df = db.df[db.df["DrugBank:Type"] == "small molecule"]
    return (db,)


@app.cell
def _(db):
    db.df
    return


@app.cell
def _():
    VERY_LARGE_NUMBER = 1e9


    def prices_analysis(price_list):
        if isinstance(price_list, str):
            price_list = [price_list]

        if price_list is None or len(price_list) == 0:
            price_list = ["InfUSD"]

        return max(tuple(map(lambda s: float(s.removesuffix("USD")), price_list)))
    return VERY_LARGE_NUMBER, prices_analysis


@app.cell
def _(VERY_LARGE_NUMBER, db, prices_analysis):
    db.df["score"] = 0

    db.df.loc[
        (db.df["Blood Brain Barrier"] < 0.5) & (db.df["P-glycoprotein Inhibition"] < 0.5), "score"
    ] -= VERY_LARGE_NUMBER
    db.df.loc[db.df["Human Intestinal Absorption"] < 0.5, "score"] -= VERY_LARGE_NUMBER
    db.df.loc[db.df["Drug Induced Liver Injury"] > 0.5, "score"] -= VERY_LARGE_NUMBER

    # 1: FDA approved
    db.df["score"] += db.df["DrugBank:FDA Approved"].fillna(False)

    # 1: Cost less than $500
    db.df["Less than $500"] = db.df["DrugBank:Prices"].apply(prices_analysis) < 500
    db.df["score"] += db.df["Less than $500"]
    return


@app.cell
def _(db):
    db.df
    return


@app.cell
def _(db):
    intestinal_absorption = db.df[~(db.df["Human Intestinal Absorption"] < 0.5)]
    print("Passes HIA             :", len(intestinal_absorption))
    bbb = intestinal_absorption[
        ~(
            (intestinal_absorption["Blood Brain Barrier"] < 0.5)
            & (intestinal_absorption["P-glycoprotein Inhibition"] < 0.5)
        )
    ]
    print("Passes HIA + BBB       :", len(bbb))
    dili = bbb[~(bbb["Drug Induced Liver Injury"] > 0.5)]
    print("Passes HIA + BBB + DILI:", len(dili))
    return (dili,)


@app.cell
def _(db, dili):
    fda = dili[dili["DrugBank:FDA Approved"]]
    print("ADMET + FDA Approved:", len(fda))
    ltfh = fda[fda["Less than $500"]]
    print("+ Less than $500    :", len(ltfh))
    print("Score of 2          :", len(db.df[db.df["score"] == 2]))
    return


if __name__ == "__main__":
    app.run()
