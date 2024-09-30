#!/usr/bin/python3
"""
Writes text to a file.
"""


def write_file(filename="", text=""):
    """Writes text to filename and returns
    the number of characters.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
