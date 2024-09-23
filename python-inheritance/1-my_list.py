#!/usr/bin/python3
"""
This module defines the class MyList, which inherits from the built-in list class
and adds a method to print the list in sorted order.

The MyList class provides an additional method `print_sorted`, which prints
the list in ascending order without modifying the original list.
"""

class MyList(list):
    """
    A subclass of the built-in list that provides an additional method to print the list in sorted order.

    Example:
    >>> my_list = MyList([4, 2, 1, 3])
    >>> my_list.print_sorted()
    [1, 2, 3, 4]

    >>> my_list = MyList([20, -5, 0, 15])
    >>> my_list.print_sorted()
    [-5, 0, 15, 20]

    >>> my_list = MyList()
    >>> my_list.print_sorted()
    []
    """
    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.

        Example:
        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        """
        print(sorted(self))
