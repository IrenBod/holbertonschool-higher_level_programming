#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            continue
        for i, element in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element))
