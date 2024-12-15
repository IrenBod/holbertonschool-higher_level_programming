#!/usr/bin/env python3

class VerboseList(list):
    """A custom list class that provides notifications for item additions and removals."""

    def append(self, item):
        """
        Add an item to the end of the list and notify.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable and notify.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list and notify.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given position and notify.
        If no index is specified, remove and return the last item.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
