#!/usr/bin/python3

"""
This module defines a Square class.
The Square class allows you to create a square with a given size and position.
It includes methods to calculate the area and print the square with the '#'
character, considering the position of the square.
"""


class Square:
    """
    This class defines a square with a given size and position.

    Attributes:
        size (int): The size of the square.
        position (tuple): A tuple of two positive integers specifying
                          the position for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with the given size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): A tuple of two positive
            integers for the position (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive
            integers specifying the position.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the character '#'.
        The position is applied using spaces.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            # Print new lines according to position[1]
            for _ in range(self.__position[1]):
                print("")
            # Print the square with spaces for the position[0]
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
