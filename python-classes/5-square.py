#!/usr/bin/python3
"""
Class square with private instance attribute 'size'

In def __init__
We check if size is an integer and not < 0

In def area
We return the area of the square

"""


class Square:
    """ Class that define a square """
    def __init__(self, size=0):
        """
        'size' for the size of the square to initialize.
        The size is stored as a private attribute.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the 'size' attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the 'size' attribute.

        Parameters:
        value (int): The new size for the square.

        Validation:
        - Checks if the new size is an integer.
          Raises TypeError if it is not.
        - Checks if the new size is >= 0.
          Raises ValueError if it is less than 0.

        Sets the new value of '__size' if all validations pass.
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

    def my_print(self):
        """
        Print the square by printing '#' in the size of 'size'.

        if size == 0 just print a blankline.
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
