#!/usr/bin/python3

"""
This module defines the Square class.

The Square class represents a square with a size and position, providing:
- A private instance attribute 'size' with a getter and setter for validation.
- A private instance attribute 'position'
with a getter and setter for validation.
- A method to calculate the area of the square.
- A method to print the square with the '#' character, respecting its position.

Attributes:
- size: Must be a non-negative integer.
- position: Must be a tuple of 2 positive integers.

Methods:
- area(): Returns the current square area.
- my_print(): Prints the square to stdout, including offsets for its position.
"""


class Square():
    """Class that defines a square with a size property
    and position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
        size (int): The size of the square (default is 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
        int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Validates the new size:
        - Must be an integer, otherwise raises TypeError.
        - Must be >= 0, otherwise raises ValueError.

        Args:
        value (int): The new size to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square (size * size).
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
            tuple: A tuple of 2 positive integers specifying the position
                where the square should be printed.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers
            indicating the position.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square to stdout using the '#'
        character with position offset.

        If the size of the square is 0, it prints an empty line.
        Otherwise:
        - Adds vertical offset (lines with no content) based on position[1].
        - Prints `size` rows, each starting with spaces based on position[0],
         followed by `size` '#' characters.
        """

        if self.__size != 0:
            if self.position[1] > 0:
                for _ in range(self.position[1]):
                    print()

            for i in range(self.__size):
                print(' ' * self.position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()