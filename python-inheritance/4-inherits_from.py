#!/usr/bin/python3
"""
This module defines the function 'inherits_from'.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise.

    Example:
        >>> inherits_from(True, int)
        True
        >>> inherits_from(5, int)
        False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
