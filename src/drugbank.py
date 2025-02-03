import re
import xml.etree.ElementTree as ET

import polars as pl
from tqdm import tqdm


def load_drug_list(filename: str) -> pl.DataFrame:
    with open(filename, "r") as file:
        drug_list = pl.read_csv(file)

    return drug_list


def price_to_dollars_per_mg(description: str, cost: str) -> float | None:
    amount_expression = re.compile(r"([0-9]+)\s*mg\s*")
    maybe_mg = amount_expression.search(description)
    if maybe_mg is None:
        return None
    else:
        return float(cost) / float(maybe_mg.groups()[0])


def find_drugbank_matches(filename: str, drug_list: pl.DataFrame) -> pl.DataFrame:
    generic_queries = drug_list["Generic Name"].str.to_lowercase()
    brand_queries = drug_list["Brand Name"].str.to_lowercase()

    namespaces = {"": "http://www.drugbank.ca"}
    drugbank_generic_column = "DrugBank Generic Names"
    drugbank_brand_column = "DrugBank Brand Names"

    list_with_matches = drug_list.with_columns(
        [
            pl.lit([]).cast(pl.List(str)).alias(drugbank_generic_column),
            pl.lit([]).cast(pl.List(str)).alias(drugbank_brand_column),
            pl.lit([]).cast(pl.List(float)).alias("Price (USD/mg)"),
        ]
    )
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
            matches = generic_queries.is_in(generic_names) | brand_queries.is_in(brand_names)
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
                    description = ""
                    cost = ""
                    currency = ""
                    unit = ""
                    for price_sub_element in price_element.iter():
                        if price_sub_element.tag[24:] == "description":
                            description = price_sub_element.text
                        elif price_sub_element.tag[24:] == "cost":
                            currency = price_sub_element.attrib.get("currency")
                            if currency != "USD":
                                break
                            cost = price_sub_element.text
                        elif price_sub_element[24:] == "unit":
                            unit = price_sub_element.text
                            if unit not in ("tablet", "capsule"):
                                break

                    if (dollars_per_mg := price_to_dollars_per_mg(description, cost)) is not None:
                        prices.append(dollars_per_mg)

            list_with_matches = list_with_matches.with_columns(
                [
                    pl.when(matches)
                    .then(generic_names)
                    .otherwise(drugbank_generic_column)
                    .alias(drugbank_generic_column),
                    pl.when(matches).then(brand_names).otherwise(drugbank_brand_column).alias(drugbank_brand_column),
                    pl.when(matches).then(is_approved).otherwise("FDA Approved").alias("FDA Approved"),
                    pl.when(matches)
                    .then(pl.lit(indication))  # need lit because string value interpreted as column name
                    .otherwise("Indication")
                    .alias("Indication"),
                    pl.when(matches).then(pl.lit(mechanism)).otherwise("Mechanism").alias("Mechanism"),
                    pl.when(matches).then(prices).otherwise("Price (USD/mg)").alias("Price (USD/mg)"),
                ]
            )

    return list_with_matches


if __name__ == "__main__":
    namespaces = {"": "http://www.drugbank.ca"}

    drug_list = load_drug_list("data/drug_list.csv")
    matches = find_drugbank_matches("data/drugbank.xml", drug_list)
    matches.write_json("data/drug_list.json")
