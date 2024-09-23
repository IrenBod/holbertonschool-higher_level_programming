#!/usr/bin/python3
"""
Module that defines a lookup function to return the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
