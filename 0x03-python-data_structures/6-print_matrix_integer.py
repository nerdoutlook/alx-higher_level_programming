#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, j, k in matrix:
        try:
            print("{} {} {}".format(i, j, k))
        except ValueError as ve:
            pass

