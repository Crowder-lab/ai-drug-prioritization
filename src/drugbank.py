import xml.etree.ElementTree as ET

import catboost as cb
import pandas as pd
from numpy.typing import NDArray
from tqdm import tqdm

import maplight_gnn


def load_drug_list(filename: str) -> pd.DataFrame:
    with open(filename, "r") as file:
        drug_list = pd.read_csv(file)

    return drug_list


def find_drugbank_matches(filename: str, drug_list: pd.DataFrame) -> pd.DataFrame:
    generic_queries = drug_list["Generic Name"].str.lower()
    brand_queries = drug_list["Brand Name"].str.lower()

    namespaces = {"": "http://www.drugbank.ca"}
    drugbank_brand_column = "DrugBank Brand Names"
    drugbank_generic_column = "DrugBank Generic Names"
    bioavailability_column = "Bioavailability"
    price_column = "Price"
    smiles_column = "SMILES"

    list_with_matches = drug_list.copy()
    list_with_matches[drugbank_generic_column] = list_with_matches.apply(lambda _: [], axis=1)
    list_with_matches[drugbank_brand_column] = list_with_matches.apply(lambda _: [], axis=1)
    list_with_matches[bioavailability_column] = None
    list_with_matches[price_column] = list_with_matches.apply(lambda _: [], axis=1)
    list_with_matches[smiles_column] = None

    for _, element in tqdm(ET.iterparse(filename, ["end"])):
        if element.tag[24:] == "drug":  # ignore the namespace
            generic_names = set()
            brand_names = set()
            # main name
            maybe_name = element.find("name", namespaces)
            if maybe_name is not None:
                generic_names.add(maybe_name.text.lower())
            # generic names
            maybe_synonyms = element.find("synonyms", namespaces)
            if maybe_synonyms is not None:
                for maybe_synonym in maybe_synonyms.iter():
                    if maybe_synonym is not None and maybe_synonym.text is not None:
                        generic_names.add(maybe_synonym.text.lower())
            # brand names
            maybe_products = element.find("products", namespaces)
            if maybe_products is not None:
                for maybe_product in maybe_products.iter():
                    maybe_brand_name = maybe_product.find("name", namespaces)
                    if maybe_brand_name is not None:
                        brand_names.add(maybe_brand_name.text.lower())

            # make sure this is a match before doing more work
            matches = generic_queries.isin(generic_names) | brand_queries.isin(brand_names)
            if not matches.any():
                continue

            # filter matches and match types
            generic_names = list(filter(lambda s: "\n" not in s, generic_names))
            brand_names = list(brand_names)

            # fda approval
            maybe_groups = element.find("groups", namespaces)
            is_approved = None
            if maybe_groups is not None:
                is_approved = "approved" in tuple(maybe_groups.itertext())

            # indication
            maybe_indication = element.find("indication", namespaces)
            indication = maybe_indication.text if maybe_indication is not None else None

            # mechanism
            maybe_mechanism = element.find("mechanism-of-action", namespaces)
            mechanism = maybe_mechanism.text if maybe_mechanism is not None else None

            # price
            maybe_prices = element.find("prices", namespaces)
            prices = []
            if maybe_prices is not None:
                for price_element in maybe_prices.iterfind("price", namespaces):
                    maybe_cost = price_element.find("cost", namespaces)
                    if maybe_cost is not None:
                        currency = maybe_cost.attrib.get("currency")
                        cost = maybe_cost.text
                        prices.append(cost + currency)

            # smiles and bioavailability
            maybe_calculated_properties = element.find("calculated-properties", namespaces)
            smiles = None
            bioavailability = None
            if maybe_calculated_properties is not None:
                for property in maybe_calculated_properties.iterfind("property", namespaces):
                    kind = property.findtext("kind", namespaces=namespaces)
                    if kind == "SMILES":
                        smiles = property.findtext("value", namespaces=namespaces)
                    elif kind == "Bioavailability":
                        bioavailability = int(property.findtext("value", namespaces=namespaces))

            list_with_matches.loc[matches, drugbank_generic_column] = list_with_matches.loc[
                matches, drugbank_generic_column
            ].apply(lambda _: generic_names)
            list_with_matches.loc[matches, drugbank_brand_column] = list_with_matches.loc[
                matches, drugbank_brand_column
            ].apply(lambda _: brand_names)
            list_with_matches.loc[matches, "FDA Approved"] = is_approved
            list_with_matches.loc[matches, "Indication"] = indication
            list_with_matches.loc[matches, "Mechanism"] = mechanism
            list_with_matches.loc[matches, price_column] = list_with_matches.loc[matches, price_column].apply(
                lambda _: prices
            )
            list_with_matches.loc[matches, bioavailability_column] = bioavailability
            list_with_matches.loc[matches, smiles_column] = smiles

    return list_with_matches


def predict_bbb(model: cb.CatBoostClassifier, smiles: pd.Series) -> NDArray:
    fingerprints = maplight_gnn.get_fingerprints(smiles)
    predictions = model.predict_proba(fingerprints)
    return predictions[:, 1]


if __name__ == "__main__":
    namespaces = {"": "http://www.drugbank.ca"}

    drug_list = load_drug_list("data/src/drug_list.csv")
    matches = find_drugbank_matches("data/src/drugbank.xml", drug_list)

    # matches = pd.read_json("data/drug_list.json", orient="records")
    smiles_mask = matches["SMILES"].notna()
    smiles = matches["SMILES"][smiles_mask]

    bbb_model = cb.CatBoostClassifier()
    bbb_model.load_model("data/src/bbb_martins-0.916-0.002.dump")
    bbb_data = predict_bbb(bbb_model, smiles)
    bbb_column = "Crosses Blood Brain Barrier"
    matches.loc[smiles_mask, bbb_column] = bbb_data

    matches.to_json("data/drug_list.json", orient="records")
