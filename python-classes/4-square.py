#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a square with a size, providing:
- A private instance attribute 'size'
with a getter and setter for validation.
- A method to calculate the area of the square.

Attributes:
- size: Must be a non-negative integer.

Methods:
- area(): Returns the current square area.
"""


class Square:
    """Class that defines a square with a size property."""

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
        size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
        int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Validates the new size:
        - Must be an integer, otherwise raises TypeError.
        - Must be >= 0, otherwise raises ValueError.

        Args:
        value (int): The new size to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square (size * size).
        """
        return self.__size * self.__size
