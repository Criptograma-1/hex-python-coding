#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        cont = 0
        for elem in row:
            cont += 1
            if cont < len(row):
                print("{:d}".format(elem), end=(" "))
            else:
                print("{:d}".format(elem), end=(""))
        print()
