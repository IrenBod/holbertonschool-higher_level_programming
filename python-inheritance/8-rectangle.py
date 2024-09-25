#!/usr/bin/python3
"""
Module defining the BaseGeometry class
for basic geometric shape operations.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from the BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with a specified width and height.

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
