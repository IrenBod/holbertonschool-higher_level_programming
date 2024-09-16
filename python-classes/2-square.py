#!/usr/bin/python3
# Definition of the Square class
class Square:
    """
    A class that represents a square with a private size attribute.
    """
    def __init__(self, size=0):
        """
        Initializes a square with an optional size.
        
        Args:
            size (int): The size of the square. Default is 0.
        
        Exceptions:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size >= 0
        if size < 0:
            raise ValueError("size must be >=0")
        # Set the private attribute __size
        self.__size = size
