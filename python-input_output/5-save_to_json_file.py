#!/usr/bin/python3
"""Save an object to a text file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file in JSON representation.

    Args:
        my_obj: The object to be serialized into JSON.
        filename: The name of the file to save the JSON data.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
