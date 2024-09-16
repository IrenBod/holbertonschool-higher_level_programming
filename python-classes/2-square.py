#!/usr/bin/python3

"""
Class square with private instance attribute 'size'
And check if size is a integer and not < 0
"""


class Square:
    """A class that represents a square with a private size attribute."""
    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        Args:
        size (int): The size of the square. Default is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
