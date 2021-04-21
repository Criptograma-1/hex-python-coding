#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new = [[row[:] for row in matrix][cow[:] for cow in matrix]]
    for row in range(len(new)):
        for col in range(len(new)):
            new[row][col] *= new[row][col]
    return new
