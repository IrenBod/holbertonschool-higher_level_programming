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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with width and height.

        Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Returns a string representation of the rectangle.

        If either the width or the height is 0, returns an empty string.
        Convert print_symbol into a string.
        Otherwise, returns a string representation of the rectangle,
        where each line is filled with the '#' character, with the number
        of lines corresponding to the height and the number of '#' characters
        in each line corresponding to the width.

        Returns:
        str: A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        rectangle_lines = []
        for _ in range(self.height):
            rectangle_lines.append(symbol * self.width)
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can recreate the instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Method called when the object is deleted.
        Prints a message indicating the rectangle is being deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the larger area.

        Args:
        rect_1: First rectangle (must be an instance of Rectangle).
        rect_2: Second rectangle (must be an instance of Rectangle).

        Returns:
        Rectangle: The rectangle with the larger area.
        Returns rect_1 if both are equal.

        Raises:
        TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method to create a square-shaped Rectangle.

        Args:
        size (int): The size of the square (default is 0).

        Returns:
        Rectangle: A new Rectangle instance with width and height equal to size.
        """
        return cls(size, size)
