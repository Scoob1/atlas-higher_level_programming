#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squares = []
    for row in matrix:
        squares_row = []
        for element in row:
            squares_row.append(element ** 2)
        squares.append(squares_row)
    return squares
