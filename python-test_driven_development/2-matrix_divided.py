#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The number to divide by.

    Returns:
        list of lists of floats: New matrix with divided values.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is zero.

    Doctests:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix  # original matrix not modified
    [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided([[1,2],[3,4]], 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    >>> matrix_divided([[1,2],[3,4]], "a")
    Traceback (most recent call last):
    TypeError: div must be a number
    >>> matrix_divided([1,2,3], 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1,2],[3,"4"]], 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1,2],[3,4,5]], 2)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)
    return new_matrix
