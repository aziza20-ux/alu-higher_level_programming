#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda data: data * data, row)) for row in matrix])
