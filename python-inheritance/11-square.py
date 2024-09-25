#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from the Rectangle class.

    Attributes:
        __size (int): The size of the square (length of its sides).
    """

    def __init__(self, size):
        """
        Initializes a square with a specified size.

        Args:
            size (int): The size of the square (both width and height).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return super().area()

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        str: The string representation in the format
        [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
