#!/usr/bin/python3
"""
Returns the dictionary description for JSON serialization.
"""
import json


def class_to_json(obj):
    """
    Args:
        obj: instance of a class.
    Returns:
        Dictionary of object's attributes.
    """
    return obj.__dict__
