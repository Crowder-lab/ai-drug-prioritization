#!/usr/bin/env uv run
import xml.etree.ElementTree as ET
from collections.abc import Iterator

import catboost as cb
import pandas as pd
from tqdm import tqdm
from typing_extensions import Self

import maplight_gnn


class Drugbank:
    namespaces = {"": "http://www.drugbank.ca"}

    def __init__(self, filename: str, search_type: str, queries: pd.Series | tuple[pd.Series, pd.Series]) -> None:
        search_functions = {"cas": self.match_cas_number, "name": self.match_names, "unii": self.match_unii}

        self.filename = filename

        if search_type in search_functions.keys():
            self.search_function = search_functions[search_type]
        else:
            raise ValueError(f"search_type must be in {search_functions.keys()}")

        if search_type == "name" and len(queries) != 2:
            raise ValueError("Must provide a generic and brand name Series for queries when search_type is 'name'")
        else:
            self.queries = queries

    def match_cas_number(self, element: ET.Element) -> pd.Series | None:
        maybe_cas_number = self.cas_number(element)
        return self.queries == maybe_cas_number if maybe_cas_number is not None else None

    def match_names(self, element: ET.Element) -> pd.Series:
        generic_names, brand_names = self.names(element)
        return self.queries[0].isin(generic_names) | self.queries[1].isin(brand_names)

    def match_unii(self, element: ET.Element) -> pd.Series | None:
        maybe_unii = self.unii(element)
        return self.queries == maybe_unii if maybe_unii is not None else None

    def get_matches(self) -> Iterator[tuple[pd.Series, ET.Element]]:
        for _, element in tqdm(ET.iterparse(self.filename, ["end"])):
            # inverted to reduce nesting
            if element.tag[24:] != "drug":  # ignore the namespace
                continue

            # check to see if our element matches one of our drugs
            matches = self.search_function(element)
            if matches is None or not matches.any():
                continue

            # matches exist
            yield matches, element

    def cas_number(self, element: ET.Element) -> str | None:
        maybe_cas_number = element.find("cas-number", self.namespaces)
        return maybe_cas_number.text if maybe_cas_number is not None else None

    def fda_approval(self, element: ET.Element) -> bool | None:
        maybe_groups = element.find("groups", self.namespaces)
        return "approved" in tuple(maybe_groups.itertext()) if maybe_groups is not None else None

    def indication(self, element: ET.Element) -> str | None:
        maybe_indication = element.find("indication", self.namespaces)
        return maybe_indication.text if maybe_indication is not None else None

    def mechanism(self, element: ET.Element) -> str | None:
        maybe_mechanism = element.find("mechanism-of-action", self.namespaces)
        return maybe_mechanism.text if maybe_mechanism is not None else None

    def name(self, element: ET.Element) -> str | None:
        maybe_name = element.find("name", self.namespaces)
        return maybe_name.text if maybe_name is not None else None

    def names(self, element: ET.Element) -> tuple[tuple[str], tuple[str]]:
        generic_names = set()
        brand_names = set()
        # main name
        maybe_name = self.name(element)
        if maybe_name is not None:
            generic_names.add(maybe_name.lower())
        # generic names
        maybe_synonyms = element.find("synonyms", self.namespaces)
        if maybe_synonyms is not None:
            for maybe_synonym in maybe_synonyms.iter():
                if maybe_synonym is not None and maybe_synonym.text is not None:
                    generic_names.add(maybe_synonym.text.lower())
        # brand names
        maybe_products = element.find("products", self.namespaces)
        if maybe_products is not None:
            for maybe_product in maybe_products.iter():
                maybe_brand_name = maybe_product.find("name", self.namespaces)
                if maybe_brand_name is not None:
                    brand_names.add(maybe_brand_name.text.lower())
        # filter matches and match types
        generic_names = tuple(filter(lambda s: "\n" not in s, generic_names))
        brand_names = tuple(brand_names)

        return generic_names, brand_names

    def prices(self, element: ET.Element) -> list[str] | None:
        maybe_prices = element.find("prices", self.namespaces)
        prices = []
        if maybe_prices is not None:
            for price_element in maybe_prices.iterfind("price", self.namespaces):
                maybe_cost = price_element.find("cost", self.namespaces)
                if maybe_cost is not None:
                    currency = maybe_cost.attrib.get("currency")
                    cost = maybe_cost.text
                    prices.append(cost + currency)
        return prices if len(prices) > 0 else None

    def smiles(self, element: ET.Element) -> str | None:
        maybe_calculated_properties = element.find("calculated-properties", self.namespaces)
        smiles = None
        if maybe_calculated_properties is not None:
            for property in maybe_calculated_properties.iterfind("property", self.namespaces):
                kind = property.findtext("kind", namespaces=self.namespaces)
                if kind == "SMILES":
                    smiles = property.findtext("value", namespaces=self.namespaces)
        return smiles

    def unii(self, element: ET.Element) -> str | None:
        maybe_unii = element.find("unii", self.namespaces)
        return maybe_unii.text if maybe_unii is not None else None


class DataAugmenter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.drug_list = None
        self.admet_model = None

    def load_drug_queries(self) -> Self:
        with open(self.filename, "r") as file:
            self.drug_list = pd.read_csv(file)
        return self

    def load_admet_model(self, filename: str) -> Self:
        self.admet_model = cb.CatBoostClassifier()
        self.admet_model.load_model(filename)
        return self

    def save_drug_info(self, filename: str) -> None:
        if self.drug_list is None:
            raise ValueError("drug_list must be loaded first.")
        with open(filename, "w") as file:
            to_save = self.drug_list[
                [
                    "Canonical Name",
                    "Drug Library Name",
                    "DrugBank Name",
                    "CAS Registry Number",
                    "UNII",
                    "SMILES",
                    "Have It",
                    "Screened",
                    "Repurposing Category",
                    "Repurposing Continued",
                    "Indication",
                    "Mechanism",
                    "Blood Brain Barrier",
                    "FDA Approved",
                    "Price",
                    "Not In DrugBank",
                    "RB Case Reports/Pediatric Safety",
                    "RB Side Effects/Adverse Events",
                    "RB Bioavailability ",
                    "RB Links",
                ]
            ]
            to_save.to_json(file, orient="records")

    def match_drugbank(self, filename: str, search_type: str, queries: pd.Series | tuple[pd.Series, pd.Series]) -> None:
        if self.drug_list is None:
            raise ValueError("drug_list is not defined. Call load_drug_queries before match_drugbank.")

        # set up constants
        cas_column = "CAS Registry Number"
        fda_column = "FDA Approved"
        indication_column = "Indication"
        mechanism_column = "Mechanism"
        name_column = "DrugBank Name"
        price_column = "Price"
        smiles_column = "SMILES"
        unii_column = "UNII"

        # create new columns
        self.drug_list[cas_column] = None
        self.drug_list[fda_column] = None
        self.drug_list[indication_column] = None
        self.drug_list[mechanism_column] = None
        self.drug_list[name_column] = None
        self.drug_list[price_column] = self.drug_list.apply(lambda _: [], axis=1)
        self.drug_list[smiles_column] = None
        self.drug_list[unii_column] = None

        drugbank = Drugbank(filename, search_type, queries)
        for matches, matching_element in drugbank.get_matches():
            self.drug_list.loc[matches, cas_column] = drugbank.cas_number(matching_element)
            self.drug_list.loc[matches, fda_column] = drugbank.fda_approval(matching_element)
            self.drug_list.loc[matches, indication_column] = drugbank.indication(matching_element)
            self.drug_list.loc[matches, mechanism_column] = drugbank.mechanism(matching_element)
            self.drug_list.loc[matches, name_column] = drugbank.name(matching_element)
            self.drug_list.loc[matches, price_column] = self.drug_list.loc[matches, price_column].apply(
                lambda _: drugbank.prices(matching_element)
            )
            self.drug_list.loc[matches, smiles_column] = drugbank.smiles(matching_element)
            self.drug_list.loc[matches, unii_column] = drugbank.unii(matching_element)

    def predict_bbb(self) -> None:
        if self.drug_list is None:
            raise ValueError("drug_list is not defined. Call load_drug_queries before predict_bbb.")
        if self.admet_model is None:
            raise ValueError("admet_model is not defined. Call load_admet_model before predict_bbb.")
        if "SMILES" not in self.drug_list.columns:
            raise ValueError("SMILES data does not exist yet. Run match_drugbank to create it")

        smiles_mask = self.drug_list["SMILES"].notna()
        smiles = self.drug_list["SMILES"][smiles_mask]

        fingerprints = maplight_gnn.get_fingerprints(smiles)
        predictions = self.admet_model.predict_proba(fingerprints)

        self.drug_list.loc[smiles_mask, "Blood Brain Barrier"] = predictions[:, 1]


if __name__ == "__main__":
    # set up augmenter
    augmenter = (
        DataAugmenter("data/src/drug_list.csv")
        .load_drug_queries()
        .load_admet_model("data/src/bbb_martins-0.916-0.002.dump")
    )

    # get data
    augmenter.match_drugbank("data/src/drugbank.xml", "cas", augmenter.drug_list["CAS Registry Number"])
    augmenter.predict_bbb()

    # save it
    augmenter.save_drug_info("data/drug_list.json")
