#!/usr/bin/python3
"""
This module contains a function to check if an object is an instance
of a specified class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of a class or its subclass.

    This function checks if the given object `obj` is an instance of the
    specified class `a_class` or a subclass of it.

    Args:
        obj: The object to be checked.
        a_class: The class or tuple of classes to check against.

    Returns:
        bool: True if `obj` is an instance of
        `a_class` or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
