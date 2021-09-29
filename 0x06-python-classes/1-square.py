#!/usr/bin/python3
"""
Task 1. 1-square.py
Write a class Square that defines a square.
Private instance attribute: size
"""


class Square:
    """
    class Square in which size is defined as
    Private instance attribute.
    """
    def __init__(self, size="0"):
        """
        Initialization function.

        Attributes:
            size: Size of a side of the square.
        """
        self.__size = size
