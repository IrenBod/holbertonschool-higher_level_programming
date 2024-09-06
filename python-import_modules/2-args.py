#!/usr/bin/python3
import sys

if __name__ == "__main__":
    nb_args = len(sys.argv) - 1
    if nb_args == 0:
        print(f"{nb_args} arguments.")
    elif nb_args == 1:
        print(f"{nb_args} argument:")
    else:
        print(f"{nb_args} arguments:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
