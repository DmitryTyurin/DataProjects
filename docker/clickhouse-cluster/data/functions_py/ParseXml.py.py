#!/usr/bin/python3

import xml.etree.ElementTree as ET
import json
from html import unescape
import sys


def parse_element(element):
    """Парсит элемент XML и возвращает словарь с данными."""
    if element is None:
        return None

    result = {}
    if element.items():
        result.update({k.split("}")[1]: unescape(v) for k, v in element.items()})
    if element.text:
        result["text"] = element.text

    return result if result else None


def parse_xml(xml_string):
    """Парсит XML строку и возвращает данные в виде словаря."""
    try:
        root = ET.fromstring(xml_string.replace("&", "&amp;"))
    except Exception as ex:
        pass

    data = {}

    for path, key, data_type in mapping:
        try:
            if data_type == "Array":
                elements = root.findall(path, namespaces)
                if elements:
                    data[key] = [
                        parse_element(el) for el in elements if parse_element(el)
                    ]

            elif data_type in ["String", "Tuple"]:
                element = root.find(path, namespaces)
                parsed_element = parse_element(element)
                if parsed_element:
                    data[key] = (
                        parsed_element
                        if data_type == "Tuple"
                        else parsed_element.get("text", "")
                    )

        except Exception as ex:
            pass

    return data


if __name__ == "__main__":
    for line in sys.stdin:
        value = json.loads(line)["value"]
        data = {}
        try:
            data = parse_xml(value)
        except Exception as ex:
            data = ""
        result = {"result": data}
        print(json.dumps(result), end="\n")
        sys.stdout.flush()
