#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    for row in matrix:
        for i, element in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element))
            if len(row) > 0:
                print()
