#!/usr/bin/python3
"""
This project module contains one method that prints
a square with the character #.
"""


def print_square(size):
    """Thisxxxxxxt be strings.
    Returns:
        A text wixxxxand last name.
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
