#!/usr/bin/python3
"""
This module defines a Square class with validation for its size.
"""


class Square():
    """
    A class that defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of one side of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
