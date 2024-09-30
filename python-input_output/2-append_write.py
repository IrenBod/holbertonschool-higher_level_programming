#!/usr/bin/python3
"""
Appends text to a file.
"""


def append_write(filename="", text=""):
    """Appends text to filename and returns
    the number of characters.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
