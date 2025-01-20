#!/usr/bin/env uv run

import xml.etree.ElementTree as ET

looking_for = "Amantadine"
matches = []

namespaces = {"": "http://www.drugbank.ca"}
for _, element in ET.iterparse("database.xml", ["end"]):
    if element.tag[24:] == f"drug":
        if not element.find("name", namespaces).text == looking_for:
            continue

        ET.dump(element)
        # for child in element.iterfind("./"):
        #     print(child.tag[24:])
