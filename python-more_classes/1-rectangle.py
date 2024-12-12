#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class represents a rectangle with width and height,
providing validation for their values through property getters and setters.

Attributes:
- width: Must be a non-negative integer.
- height: Must be a non-negative integer.

Methods:
- None explicitly defined for functionality beyond initialization and validation.
"""

class Rectangle():
    """Class that defines a rectangle with width and height."""
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with width and height.

        Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        int: The current width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Validates the width to ensure it is a non-negative integer.

        Args:
        value (int): The new width to set.

        Raises:
        TypeError: If width is not an integer.
        ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        int: The current height of the rectangle.
        """
        return self.__hight
    
    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Validates the height to ensure it is a non-negative integer.

        Args:
        value (int): The new height to set.

        Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
