#!/usr/bin/python3

"""
Class square with private instance attribute 'size'
And check if size is a integer and not < 0
"""


class Square():
    """ Class that define a square """
    def __init__(self, size=0):
        """
        'size' for the size of the square to initialize.
        The size is store as a private attribute.

        The first condition check if size is a integer,
        if not raise a TypeError

        The second condition check if size not < 0,
        if not raise a ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private Attribute ("__")
