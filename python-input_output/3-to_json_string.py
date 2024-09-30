#!/usr/bin/python3
"""
Converts a Python object into its JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON string of object.
    """
    return json.dumps(my_obj)
