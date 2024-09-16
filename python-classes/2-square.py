#!/usr/bin/python3

"""
This module defines a Square class with a private attribute 'size'.
It includes validation to ensure that the 'size' value is a non-negative integer.
"""

class Square:
    """
    A class that represents a square with a private size attribute.

    Attributes:
        __size (int): The size of one side of the square, which must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a specified size.

        Args:
            size (int, optional): The size of the square's side. Default is 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative number.
        """
        # Assign the size to the private attribute after validating its type and value
        self.__size = size

        # Ensure that the size is an integer, otherwise raise a TypeError
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        # Ensure that the size is not less than 0, otherwise raise a ValueError
        if size < 0:
            raise ValueError("size must be >= 0")
