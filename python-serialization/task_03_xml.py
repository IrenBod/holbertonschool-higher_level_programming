#!/usr/bin/python3
"""
This module provides functions to serialize
a Python dictionary to an XML file
and deserialize an XML file back into a Python dictionary.

Functions:
- serialize_to_xml: Serializes a dictionary and saves it as an XML file.
- deserialize_from_xml: Loads data from an XML
file and converts it into a dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save the serialized data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.
    Args:
        filename (str): The XML file to deserialize.
    Returns:
        dict: A Python dictionary with deserialized data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    deserialized_data = {}
    for child in root:
        deserialized_data[child.tag] = child.text
    return deserialized_data


if __name__ == "__main__":

    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"

    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
