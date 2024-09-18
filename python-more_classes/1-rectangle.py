#!/usr/bin/python3

"""
This module defines a Rectangle class.

The Rectangle class allows you to create a rectangle with specified
width and height, and provides basic operations such as getting
and setting the width and height with proper error handling.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Args:
            width (int): The width of the rectangle
            (must be a non-negative integer).
            height (int): The height of the rectangle
            (must be a non-negative integer).
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle
            (must be a non-negative integer).

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle
            (must be a non-negative integer).

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
