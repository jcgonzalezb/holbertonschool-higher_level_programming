#!/usr/bin/python3
"""
This project module supplies one function that adds 2 integers.
"""


def add_integer(a, b=98):
    """This is a function that adds 2 integers."""
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not (isinstance(a, float) or
            isinstance(a, int)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, float) or
            isinstance(b, int)):
        raise TypeError("b must be an integer")

    return a + b
