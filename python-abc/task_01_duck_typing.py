from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape defining a blueprint for shapes.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape. Accepts radius as a parameter.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape.
    Accepts width and height as parameters.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function to display the area and perimeter of any shape object
    that implements the required methods.
    """
    print("Area: {:.2f}".format(shape.area()))
    print("Perimeter: {:.2f}".format(shape.perimeter()))
