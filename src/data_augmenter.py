#!/usr/bin/env -S uv run
import xml.etree.ElementTree as ET
from typing import Literal

import catboost as cb
import numpy as np
import pandas as pd
from hyrule import flatten
from rdkit import Chem, RDLogger
from tqdm import tqdm

import maplight_gnn


class DrugBank:
    namespaces = {"": "http://www.drugbank.ca"}

    def __init__(self, filename: str, ids: pd.Series, id_types: pd.Series, names: pd.Series):
        self.filename = filename
        self.ids = ids
        self.id_types = id_types
        self.names = names.str.lower()
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

    def get_matches(self, match_type: Literal["id", "name"]):
        check_match = self.check_id_match if match_type == "id" else self.check_name_match
        for _, element in tqdm(ET.iterparse(self.filename, ["end"])):
            if element.tag[24:None:None] != "drug":
                continue

            matches = check_match(element)
            if not matches.any():
                continue

            yield (matches, element)

    def check_id_match(self, element):
        matches = pd.Series(False, index=self.ids.index)

        for id_type, id_func in self.get_ids.items():
            id_val = id_func(element)
            if id_val is None:
                continue

            id_type_matches = self.id_types == id_type
            id_val_matches = self.ids == id_val
            id_full_matches = id_type_matches & id_val_matches
            matches = matches | id_full_matches

        return matches

    def check_name_match(self, element):
        matches = pd.Series(False, index=self.ids.index)

        for names in self.all_names(element):
            matches = matches | self.names.isin(names)

        return matches

    def all_names(self, element):
        generic_names = set()
        brand_names = set()
        main_name = self.name(element)
        generic_names.add(main_name.lower()) if main_name is not None else None
        it = element.find("synonyms", self.namespaces)
        if it is not None:
            for synonym in it.iter():
                generic_names.add(synonym.text.lower()) if synonym is not None and synonym.text is not None else None

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
                prices.append(price.text + price.attrib.get("currency")) if price is not None else None
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
                if external_identifier.findtext("resource", namespaces=self.namespaces) == resource_type:
                    return external_identifier.findtext("identifier", namespaces=self.namespaces)
        return None

    def from_calculated_properties(self, element, kind_type):
        it = element.find("calculated-properties", self.namespaces)
        if it is not None:
            for property in it.iterfind("property", self.namespaces):
                if property.findtext("kind", namespaces=self.namespaces) == kind_type:
                    return property.findtext("value", namespaces=self.namespaces)
        return None


class DataAugmenter:
    def __init__(self, filename, id_col_name, id_type_col_name, name_col_name):
        self.filename = filename
        self.id_col_name = id_col_name
        self.id_type_col_name = id_type_col_name
        self.name_col_name = name_col_name
        self.drug_list = None
        self.admet_models = None

    def add_to_column(self, col_name, analysis_function, matches, element):
        def _hy_anon_var_11(x):
            new_vals = flatten(analysis_function(element))
            x.extend(new_vals) if isinstance(new_vals, list) else x.append(new_vals)
            return x

        self.drug_list.loc[matches, col_name] = self.drug_list.loc[matches, col_name].apply(_hy_anon_var_11)

    def unwrap_list(self, x):
        return (x[0] if len(x) > 0 else None) if isinstance(x, list) else x

    def load_drug_queries(self):
        if self.filename.endswith(".csv"):
            _hy_anon_var_12 = None
            with open(self.filename, "r") as f:
                self.drug_list = pd.read_csv(f)
                _hy_anon_var_12 = None
            _hy_anon_var_16 = _hy_anon_var_12
        else:
            if self.filename.endswith(".json"):
                _hy_anon_var_13 = None
                with open(self.filename, "r") as f:
                    self.drug_list = pd.read_json(f, orient="records")
                    _hy_anon_var_13 = None
                _hy_anon_var_15 = _hy_anon_var_13
            else:
                if True:
                    raise ValueError("Data file must be .csv or .json")
                    _hy_anon_var_14 = None
                else:
                    _hy_anon_var_14 = None
                _hy_anon_var_15 = _hy_anon_var_14
            _hy_anon_var_16 = _hy_anon_var_15
        return self

    def load_admet_models(self, models):
        self.admet_models = dict()
        for name, path in models.items():
            model = cb.CatBoostClassifier()
            model.load_model(path)
            self.admet_models[name] = model
        return self

    def save_drug_info(self, filename):
        if self.drug_list is None:
            raise ValueError("drug_list must be loaded first.")

        with open(filename, "w") as f:
            return self.drug_list.to_json(f, orient="records", indent=2)

    def match_drugbank(self, filename):
        if self.drug_list is None:
            raise ValueError("drug_list is not defined. Call load_drug_queries before match_drugbank.")

        # fmt: off
        id_col      = self.drug_list[self.id_col_name     ].apply(self.unwrap_list)
        id_type_col = self.drug_list[self.id_type_col_name].apply(self.unwrap_list)
        name_col    = self.drug_list[self.name_col_name   ].apply(self.unwrap_list)
        self.drug_list[self.id_col_name]      = id_col
        self.drug_list[self.id_type_col_name] = id_type_col
        self.drug_list[self.name_col_name]    = name_col

        self.all_names_column   = "DrugBank:All Names"
        self.cas_column         = "DrugBank:CAS Registry Number"
        self.fda_column         = "DrugBank:FDA Approved"
        self.indication_column  = "DrugBank:Indication"
        self.mechanism_column   = "DrugBank:Mechanism"
        self.name_column        = "DrugBank:Main Name"
        self.price_column       = "DrugBank:Prices"
        self.smiles_column      = "DrugBank:SMILES"
        self.unii_column        = "DrugBank:UNII"
        self.match_found_column = "DrugBank:Match Found"

        self.drug_list[self.all_names_column]   = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.cas_column]         = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.fda_column]         = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.indication_column]  = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.mechanism_column]   = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.name_column]        = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.price_column]       = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.smiles_column]      = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.unii_column]        = self.drug_list.apply(lambda _: list(), axis=1)
        self.drug_list[self.match_found_column] = False
        # fmt: on

        # match by id since that's more important
        drugbank = DrugBank(filename, id_col, id_type_col, name_col)
        for matches, element in drugbank.get_matches(match_type="id"):
            new_matches = matches & -self.drug_list[self.match_found_column]
            self.drug_list[self.match_found_column] |= new_matches

            # fmt: off
            self.add_to_column(self.all_names_column,  drugbank.all_names,    new_matches, element)
            self.add_to_column(self.cas_column,        drugbank.cas_number,   new_matches, element)
            self.add_to_column(self.fda_column,        drugbank.fda_approval, new_matches, element)
            self.add_to_column(self.indication_column, drugbank.indication,   new_matches, element)
            self.add_to_column(self.mechanism_column,  drugbank.mechanism,    new_matches, element)
            self.add_to_column(self.name_column,       drugbank.name,         new_matches, element)
            self.add_to_column(self.price_column,      drugbank.prices,       new_matches, element)
            self.add_to_column(self.smiles_column,     drugbank.smiles,       new_matches, element)
            self.add_to_column(self.unii_column,       drugbank.unii,         new_matches, element)
            # fmt: on

        # match on name if there wasn't an id match
        drugbank = DrugBank(filename, id_col, id_type_col, name_col)
        for matches, element in drugbank.get_matches(match_type="name"):
            new_matches = matches & -self.drug_list[self.match_found_column]
            self.drug_list[self.match_found_column] |= new_matches

            # fmt: off
            self.add_to_column(self.all_names_column,  drugbank.all_names,    new_matches, element)
            self.add_to_column(self.cas_column,        drugbank.cas_number,   new_matches, element)
            self.add_to_column(self.fda_column,        drugbank.fda_approval, new_matches, element)
            self.add_to_column(self.indication_column, drugbank.indication,   new_matches, element)
            self.add_to_column(self.mechanism_column,  drugbank.mechanism,    new_matches, element)
            self.add_to_column(self.name_column,       drugbank.name,         new_matches, element)
            self.add_to_column(self.price_column,      drugbank.prices,       new_matches, element)
            self.add_to_column(self.smiles_column,     drugbank.smiles,       new_matches, element)
            self.add_to_column(self.unii_column,       drugbank.unii,         new_matches, element)
            # fmt: on

        self.drug_list[self.name_column] = self.drug_list[self.name_column].apply(self.unwrap_list)

    def make_main_name_col(self):
        if self.drug_list is None:
            raise ValueError("drug_list is not defined. Call load_drug_queries before make_main_name_col.")
        if "DrugBank:Main Name" not in self.drug_list.columns:
            raise ValueError("DrugBank data does not exist yet. Run match_drugbank to create it.")

        name_column = self.drug_list[self.name_column].notna()
        self.drug_list["Main Name"] = None
        self.drug_list.loc[-name_column, "Main Name"] = self.drug_list[self.name_col_name]
        self.drug_list.loc[name_column, "Main Name"] = self.drug_list[self.name_column]
        self.drug_list["Main Name"] = self.drug_list["Main Name"].str.lower()

        return print(f"MISSING NAMES: {self.drug_list['Main Name'].isna().sum()}")

    def deduplicate(self):
        if self.drug_list is None:
            raise ValueError("drug-list is not defined. Call load-drug-queries before deduplicate.")
            _hy_anon_var_22 = None
        else:
            _hy_anon_var_22 = None
        if "DrugBank:Main Name" not in self.drug_list.columns:
            raise ValueError("DrugBank data does not exist yet. Run match-drugbank to create it.")
            _hy_anon_var_23 = None
        else:
            _hy_anon_var_23 = None
        if "Main Name" not in self.drug_list.columns:
            raise ValueError("Combined 'Main Name' column does not exist yet. Run make-main-name-col to create it.")
            _hy_anon_var_24 = None
        else:
            _hy_anon_var_24 = None
        name_column = self.drug_list["Main Name"].notna()
        no_name_rows = self.drug_list[-name_column]
        name_rows = self.drug_list[name_column]

        def _hy_anon_var_25(x):
            y = []
            for item in x:
                y.extend(item) if isinstance(item, list) else y.append(item)
            z = set(y)
            z.discard(None)
            return None if len(z) == 0 else z.pop() if len(z) == 1 else z if True else None

        deduplicated_rows = name_rows.groupby("Main Name").agg(_hy_anon_var_25).reset_index()
        merged_list = pd.concat((no_name_rows, deduplicated_rows), ignore_index=True)
        print("DRUGS REMOVED IN DEDUPLICATION:")
        print(
            self.drug_list[-self.drug_list["Main Name"].isin(merged_list["Main Name"])][
                ["Main Name", self.name_col_name, self.all_names_column, self.name_column, self.match_found_column]
            ]
        )
        self.drug_list = merged_list

    def predict_admet(self):
        if self.drug_list is None:
            raise ValueError("drug-list is not defined. Call load-drug-queries before predict-admet.")
            _hy_anon_var_26 = None
        else:
            _hy_anon_var_26 = None
        if self.admet_models is None:
            raise ValueError("admet-models is not defined. Call load-admet-models before predict-admet.")
            _hy_anon_var_27 = None
        else:
            _hy_anon_var_27 = None
        if "DrugBank:SMILES" not in self.drug_list.columns:
            raise ValueError("SMILES data does not exist yet. Run match-drugbank to create it.")
            _hy_anon_var_28 = None
        else:
            _hy_anon_var_28 = None
        RDLogger.DisableLog("rdApp.*")
        self.drug_list[self.smiles_column] = self.drug_list[self.smiles_column].apply(self.unwrap_list)
        smiles_mask = self.drug_list[self.smiles_column].notna()
        smiles = self.drug_list.loc[smiles_mask, self.smiles_column]
        molecules = smiles.apply(Chem.MolFromSmiles)
        # solves this error message:
        # > molfeat.trans.pretrained.dgl_pretrained:graph_featurizer:283 - rdkit.Chem.rdchem.BondType.DATIVE is not in list
        # if this happens again, adjust the lambda appropriately
        no_dative_bond = molecules.apply(
            lambda mol: Chem.rdchem.BondType.DATIVE not in map(lambda bond: bond.GetBondType(), mol.GetBonds())
        )
        molecules_mask = molecules.notna() & no_dative_bond
        fingerprints = self.get_fingerprints(molecules[molecules_mask])
        combined_mask = pd.Series(False, index=self.drug_list.index)
        combined_mask.loc[smiles[molecules_mask].index] = True
        for name, model in self.admet_models.items():
            predictions = model.predict_proba(fingerprints)
            self.drug_list.loc[combined_mask, name] = predictions[slice(None, None), 1]

    def get_fingerprints(self, molecules):
        fingerprints = list()
        fingerprints.append(maplight_gnn.get_morgan_fingerprints(molecules))
        fingerprints.append(maplight_gnn.get_avalon_fingerprints(molecules))
        fingerprints.append(maplight_gnn.get_erg_fingerprints(molecules))
        fingerprints.append(maplight_gnn.get_rdkit_features(molecules))
        fingerprints.append(maplight_gnn.get_gin_supervised_masking(molecules))
        return np.concatenate(fingerprints, axis=1)


if __name__ == "__main__":
    augmenter = (
        DataAugmenter("data/translator_drugs.json", "result_id", "id_type", "result_name")
        .load_drug_queries()
        .load_admet_models(
            {
                "Blood Brain Barrier": "data/admet/bbb_martins-0.916-0.002.dump",
                "P-glycoprotein Inhibition": "data/admet/pgp_broccatelli-0.938-0.0.dump",
                "Human Intestinal Absorption": "data/admet/hia_hou-0.989-0.001.dump",
                "Drug Induced Liver Injury": "data/admet/dili-0.918-0.005.dump",
            }
        )
    )
    _hy_gensym_f_1 = augmenter
    _hy_gensym_f_1.match_drugbank("data/src/drugbank.xml")
    _hy_gensym_f_1.make_main_name_col()
    _hy_gensym_f_1.deduplicate()
    _hy_gensym_f_1.predict_admet()
    _hy_gensym_f_1.save_drug_info("data/translator_drug_list.json")
    _hy_anon_var_29 = _hy_gensym_f_1
