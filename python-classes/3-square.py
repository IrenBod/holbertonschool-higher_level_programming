#!/usr/bin/python3

"""This script defines a class Square, which represents a geometric square.
It includes methods for validating the size
of the square and calculating its area."""


class Square():
    def __init__(self, size=0):
        """Initialize the square with an optional size parameter
         (default is 0).
        Validate that the size is an integer and greater than
         or equal to 0."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square.
        The area is computed as the square of the size."""
        return self.__size * self.__size
