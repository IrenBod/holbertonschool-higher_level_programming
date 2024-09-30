#!/usr/bin/python3
"""
This module provides a function to load data from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Reads and returns an object from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
