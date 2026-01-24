#!/usr/bin/python3
"""
This module provides a function to print a square using the # character.
"""


def print_square(size):
    """
    Prints a square of size `size` using the # character.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Doctests:
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(1)
    #
    >>> print_square(0)
    <BLANKLINE>
    >>> print_square(-1)
    Traceback (most recent call last):
    ValueError: size must be >= 0
    >>> print_square(2.5)
    Traceback (most recent call last):
    TypeError: size must be an integer
    >>> print_square("4")
    Traceback (most recent call last):
    TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
