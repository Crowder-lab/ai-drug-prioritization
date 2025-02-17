import xml.etree.ElementTree as ET
from collections.abc import Iterator

import catboost as cb
import pandas as pd
from numpy.typing import NDArray
from tqdm import tqdm

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
        maybe_cas_number = element.find("cas-number", self.namespaces)
        return self.queries == maybe_cas_number.text if maybe_cas_number is not None else None

    def match_names(self, element: ET.Element) -> pd.Series:
        generic_names = set()
        brand_names = set()
        # main name
        maybe_name = element.find("name", self.namespaces)
        if maybe_name is not None:
            generic_names.add(maybe_name.text.lower())
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

        return self.queries[0].isin(generic_names) | self.queries[1].isin(brand_names)

    def match_unii(self, element: ET.Element) -> pd.Series | None:
        maybe_unii = element.find("unii", self.namespaces)
        return self.queries == maybe_unii.text if maybe_unii is not None else None

    def get_matches(self) -> Iterator[ET.Element]:
        for _, element in tqdm(ET.iterparse(self.filename, ["end"])):
            # inverted to reduce nesting
            if element.tag[24:] != "drug":  # ignore the namespace
                continue

            # check to see if our element matches one of our drugs
            matches = self.search_function(element)
            if matches is None or not matches.any():
                continue

            # matches exist
            yield element

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


class DataAugmenter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.drug_list = None

    def load_drug_queries(self) -> pd.DataFrame:
        with open(self.filename, "r") as file:
            self.drug_list = pd.read_csv(file)

        return self.drug_list

    def match_drugbank(self, filename: str, search_type: str, queries: pd.Series | tuple[pd.Series, pd.Series]) -> None:
        if self.drug_list is None:
            raise ValueError("drug_list is not defined. Call load_drug_queries before match_drugbank.")

        # set up constants
        fda_column = "FDA Approved"
        indication_column = "Indication"
        mechanism_column = "Mechanism"
        name_column = "DrugBank Name"
        price_column = "Price"
        smiles_column = "SMILES"

        # create new columns
        self.drug_list[name_column] = None
        self.drug_list[price_column] = self.drug_list.apply(lambda _: [], axis=1)
        self.drug_list[smiles_column] = None

        drugbank = Drugbank(filename, search_type, queries)
        for matching_element in drugbank.get_matches():
            self.drug_list.loc[self.drug_list, fda_column] = drugbank.fda_approval(matching_element)
            self.drug_list.loc[self.drug_list, indication_column] = drugbank.indication(matching_element)
            self.drug_list.loc[self.drug_list, mechanism_column] = drugbank.mechanism(matching_element)
            self.drug_list.loc[self.drug_list, price_column] = self.drug_list.loc[self.drug_list, price_column].apply(
                lambda _: drugbank.prices(matching_element)
            )
            self.drug_list.loc[self.drug_list, smiles_column] = drugbank.smiles(matching_element)

    def predict_bbb(self, model: cb.CatBoostClassifier, smiles: pd.Series) -> NDArray:
        fingerprints = maplight_gnn.get_fingerprints(smiles)
        predictions = model.predict_proba(fingerprints)
        return predictions[:, 1]


if __name__ == "__main__":
    pass
