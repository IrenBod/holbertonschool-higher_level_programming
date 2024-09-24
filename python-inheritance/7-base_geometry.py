#!/usr/bin/python3
"""
This module defines the class 'BaseGeometry'.
"""


class BaseGeometry():
    """
    A class used to represent basic geometric operations.
    """
    def area(self):
        """
        Raises an Exception with a message indicating that
        the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
