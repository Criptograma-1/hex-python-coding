#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            list.append(row, matrix[i][j] ** 2)
        list.append(new, row)
    return new
