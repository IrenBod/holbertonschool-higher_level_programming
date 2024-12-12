#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class represents a rectangle with width and height,
providing validation for their values through property getters and setters.

Attributes:
- width: Must be a non-negative integer.
- height: Must be a non-negative integer.
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
        return self.__height

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

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: The area of the rectangle (width * height).
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
         Returns 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle
        using the '#' character.

        Returns:
        str: The rectangle as lines of '#' characters.
         Returns an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])
