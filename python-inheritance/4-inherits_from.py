#!/usr/bin/python3
"""
This module defines the function 'inherits_from'.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
