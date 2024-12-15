#!/usr/bin/python3
"""
A custom iterator that counts the number of iterations.
"""

class CountedIterator:
    """A custom iterator that tracks the number of items iterated."""

    def __init__(self, iterable=0):
        """
        Initialize the CountedIterator with an iterable.
        
        Args:
        iterable (iterable): The iterable to wrap and iterate over.
        """
        self.iterator = iter(iterable)  # Initialize the iterator from the iterable
        self.counter = 0               # Initialize the counter to zero

    def __next__(self):
        """
        Fetch the next item from the iterator, incrementing the counter.

        Returns:
        The next item from the iterator.

        Raises:
        StopIteration: When there are no more items to iterate.
        """
        try:
            # Fetch the next item and increment the counter
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Retrieve the number of items iterated so far.

        Returns:
        int: The current count of items iterated.
        """
        return self.counter
