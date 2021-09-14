#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_m = []
        for rows in matrix:
            new_m.append(list(map(lambda x: x**2, rows)))
        return new_m
    return None
