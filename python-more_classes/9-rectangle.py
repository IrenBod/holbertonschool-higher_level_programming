#!/usr/bin/python3
"""
This module defines a Rectangle class.

The Rectangle class allows you to create a rectangle with specified
width and height, and provides methods to calculate the area and perimeter.
It also defines a way to print the rectangle using the '#' character.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increase the number of instances

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

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
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle,
            or 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        If the width or height is 0, returns an empty string. Otherwise,
        returns a rectangle made of the character '#'.

        Returns:
            str: The rectangle as a string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            rect.append(str(self.print_symbol) * self.width)
        return "\n".join(rect)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to
        recreate an instance of the object using eval().

        Returns:
            str: A string in the format 'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.

        Prints:
            Bye rectangle...
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1  # Reduce the number of copies

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles based on their
        area and returns the largest one.
        If both have the same area, returns rect_1.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 or rect_2 are not instances of Rectangle.

        Returns:
            Rectangle: The rectangle with the largest area, or rect_1 if equal.
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
        Creates a new Rectangle instance where width == height == size.

        Args:
            size (int): The size of the square (both width and height).

        Returns:
            Rectangle: A new instance of
            Rectangle where width == height == size.
        """
        return cls(size, size)
