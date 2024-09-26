#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        print(f"Extended the list with [{len(iterable)}] items.")
        super().extend(iterable)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from list.")
        return item
