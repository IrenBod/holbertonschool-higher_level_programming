#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    A class used to represent a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle
        (must be a positive integer).
        __height (int): The height of the rectangle
        (must be a positive integer).
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height,
        validated as positive integers.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation in the
            format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
