#!/usr/bin/python3
"""
Reads and prints a UTF8 text file.
"""


def read_file(filename=""):
    """Prints the content of a file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
