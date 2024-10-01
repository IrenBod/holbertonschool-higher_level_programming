#!/usr/bin/python3
"""Script to add command-line arguments to a list and save them as JSON."""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Write an object to a text file in JSON format."""


filename = "add_item.json"

try:
    with open(filename, 'r', encoding="utf-8") as f:
        items = json.load(f)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])

with open(filename, 'w', encoding="utf-8") as f:
    json.dump(items, f)
