#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        square.append([num ** 2 for num in row])
    return square
