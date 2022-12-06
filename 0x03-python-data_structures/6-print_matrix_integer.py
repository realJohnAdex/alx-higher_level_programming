#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat = matrix
    print('\n'.join(' '.join(['{:d}'.format(e) for e in row]) for row in mat))
