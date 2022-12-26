#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        object_list = []
        for j in i:
            j = j ** 2
            object_list.append(j)
        new_matrix.append(object_list)
    return(new_matrix)


"""
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
print(square_matrix_simple(matrix))
"""
