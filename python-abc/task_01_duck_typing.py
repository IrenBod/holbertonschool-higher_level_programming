#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math import pi


# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


# Circle class inheriting Shape
class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize the Circle with a radius.
        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return pi * (self.radius * self.radius)

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return abs((2 * self.radius) * pi)



# Rectangle class inheriting Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


# Standalone function to display shape information
def shape_info(shape):
    """
    Print the area and perimeter of a given shape.
    Args:
        shape (Shape): An object adhering to the Shape interface.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
