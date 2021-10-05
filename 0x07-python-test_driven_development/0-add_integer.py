#!/usr/bin/python3
"""
This project module supplies one function that adds 2 integers.
Contains one method that returns an integer which results from
the addition of two integers.
"""


def add_integer(a, b=98):
    """This is a function that adds 2 integers.
    a and b must be integers or floats, otherwise raise
    a TypeError exception with the message a must be an
    integer or b must be an integer.
    Returns:
        An integer: the addition of a and b.
    """
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
