#!/usr/bin/python3

"""
This module defines a class Square
that validates and calculates
the area of a square.
"""


class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of one side of the
        square, which must be a non-negative integer.

    Methods:
        area(): Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a specified size.

        Args:
            size (int, optional): The size of
            the square's side. Default is 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative number.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square, which
            is the square of the size attribute.
        """
        return self.__size * self.__size
