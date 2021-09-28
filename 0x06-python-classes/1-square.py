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
        self.__size = size
        """
        Initialization function.
        Args:
            self (int): Used to refer to itself.
            size (int): Size of the square.

        Returns:
            int: The return value. Size value.
        """
    @property
    def size(self):
        """
        Size function.
        Args:
            self (int): Used to refer to itself.

        Returns:
            int: The return value. Size value.
        """
        return self.__size
