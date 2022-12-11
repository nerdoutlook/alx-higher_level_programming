#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix.__len__() > 0:
        for i in matrix:
            print("{0}".format(i))
    elif matrix.__len__() <= 0:
        print()
