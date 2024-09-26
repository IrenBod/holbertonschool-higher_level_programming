#!/usr/bin/env python3
"""
CountedIterator: A class that counts the number of iterations over an iterable.
"""


class CountedIterator:
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Args:
            iterable: An iterable object to be iterated over.
        """
        self.count = 0
        self.iterator = iter(iterable)

    def __next__(self):
        """
        Returns the next item from the iterable and increments the counter.

        Raises:
            StopIteration: If there are no more items in the iterable.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the current iteration count.

        Returns:
            int: The number of items iterated so far.
        """
        return self.count
