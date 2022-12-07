#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        sq_matrix.append(list(map(lambda x: x ** 2, row)))

    return sq_matrix
