import xml.etree.ElementTree as ET

import polars as pl
from tqdm import tqdm


def load_drug_list(filename: str) -> pl.DataFrame:
    with open(filename, "r") as file:
        drug_list = pl.read_csv(file)

    return drug_list


def find_drugbank_matches(filename: str, generic_queries: pl.Series, brand_queries: pl.Series) -> list[ET.Element]:
    generic_queries = generic_queries.str.to_lowercase()
    brand_queries = brand_queries.str.to_lowercase()

    matches = []
    namespaces = {"": "http://www.drugbank.ca"}

    for _, element in tqdm(ET.iterparse(filename, ["end"])):
        if element.tag[24:] == "drug":
            # find all possible names for this drug
            generic_names = [name.text.lower()] if (name := element.find("name", namespaces)) is not None else []
            if (synonyms := element.find("synonyms", namespaces)) is not None:
                for synonym in synonyms.iter():
                    if synonym is not None and synonym.text is not None:
                        generic_names.append(synonym.text.lower())
            if generic_queries.is_in(generic_names).any():
                matches.append(element)
                continue

            if (products := element.find("products", namespaces)) is not None:
                brand_names = []
                for product in products.iter():
                    if (name := product.find("name", namespaces)) is not None:
                        brand_names.append(name.text.lower())
                if brand_queries.is_in(brand_names).any():
                    matches.append(element)

    return matches


if __name__ == "__main__":
    namespaces = {"": "http://www.drugbank.ca"}

    drug_list = load_drug_list("data/drug_list.csv")
    matches = find_drugbank_matches(
        "data/drugbank.xml",
        drug_list["Generic Name"],
        drug_list["Brand Name"],
    )
    for match in matches:
        print(match.find("name", namespaces).text.lower())
