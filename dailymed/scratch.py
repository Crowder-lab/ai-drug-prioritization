#!/usr/bin/env python3

import xml.etree.ElementTree as ET

NAMESPACES = {"": "urn:hl7-org:v3"}

def process_section(section) -> None:
    ET.dump(section)

if __name__ == "__main__":
    for _, element in ET.iterparse("amantadine_hydrochloride.xml", ["end"]):
        if element.tag[16:] == "component":
            if element.find("./section/title[.='WARNINGS']", NAMESPACES) is not None:
                process_section(element)
            elif element.find("./section/title[.='PRECAUTIONS']", NAMESPACES) is not None:
                process_section(element)
            elif element.find("./section/title[.='ADVERSE REACTIONS']", NAMESPACES) is not None:
                process_section(element)
