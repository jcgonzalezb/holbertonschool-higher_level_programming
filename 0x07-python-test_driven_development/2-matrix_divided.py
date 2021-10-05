#!/usr/bin/python3
"""
This project module contains one method that divides all
elements of a matrix. The matrix must be a list of lists
of integers or floats. Each row of the matrix must be of
the same size.
"""


def matrix_divided(matrix, div):
    """This is a method that divides all elements of a
    matrix. div must be a number (integer or float).
    div can’t be equal to 0. All elements of the matrix
    should be divided by div, rounded to 2 decimal places.
    Returns:
        A new matrix.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        if not len(matrix[i]) is len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    m_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(m_error)

    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(m_error)

    matrix_divided = []

    for lists in matrix:
        new_list = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(m_error)
            new_list.append(round(i/div, 2))
        matrix_divided.append(new_list)
    return matrix_divided
