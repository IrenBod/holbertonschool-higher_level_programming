#!/usr/bin/python3
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    with open(filename, 'r', encoding="utf-8") as f:
        items = json.load(f)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])

with open(filename, 'w', encoding="utf-8") as f:
    json.dump(items,f)