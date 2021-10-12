#!/usr/bin/python3
"""
This project module contains one method that returns the
list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    This is a method that returns the list of
    available attributes and methods of an object.
    Returns:
        Returns a list object.
    """
    return dir(obj)
