#!/usr/bin/python3
"""
This project module contains one method that prints
a square with the character #.
"""


def print_square(size):
    """This is a method that prints a square with
    the character #.
    -size is the size length of the square.
    -size must be an integer, otherwise raise a
    TypeError exception with the message size must
    be an integer.
    -if size is less than 0, raise a ValueError
    exception with the message size must be >= 0.
    -if size is a float and is less than 0, raise
    a TypeError exception with the message size
    must be an integer.

    Returns:
        A square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(1, size+1):
        for j in range(1, size+1):
            print("#", end="")
        print()
