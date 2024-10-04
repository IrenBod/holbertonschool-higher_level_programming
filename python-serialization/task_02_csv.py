#!/usr/bin/python3
"""
Module to convert a CSV file to JSON format and save it to 'data.json'.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format and save it to 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to read from.
    Returns:
        bool: True if the conversion was successful,
        False if the file is not found.
    """
    try:
        with open(csv_filename, encoding='utf-8') as csvf:
            reader = csv.DictReader(csvf)
            data = list(reader)
        with open('data.json', 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=1)
            return True
    except FileNotFoundError:
        print("CSV file not found")
        return False
