#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	square_matrix = []
	for row in matrix:
		square_row = [(lambda x: x**2)(x) for x in row]
		square_matrix.append(square_row)

	return square_matrix
