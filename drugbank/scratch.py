#!/usr/bin/env python3

import xml.etree.ElementTree as ET

looking_for = "Amantadine"
matches = []

namespaces = {"": "http://www.drugbank.ca"}
for _, element in ET.iterparse("database.xml", ["end"]):
    if element.tag[24:] == "drug":
        if not element.find("name", namespaces).text == looking_for:
            continue

        ET.dump(element)
        break
