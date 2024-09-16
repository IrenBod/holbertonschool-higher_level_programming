#!/usr/bin/python3

"""
This module defines a class Square that represents a square
with a private size attribute. The size attribute must be a
positive integer, and the class checks this upon instantiation.
"""


class Square:
    """A class that represents a square with a private size attribute."""
    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        Args:
            size (int): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        # Private attribute
        self.__size = size
