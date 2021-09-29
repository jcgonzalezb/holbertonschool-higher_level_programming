#!/usr/bin/python3
"""
Task 4.
Write a class Square that defines a square.
Private instance attribute: size and public
attribute area.
"""


class Square:
    """
    class Square in which size is defined as
    Private instance attribute.

    Args:
        size (int): size of a side in square

    functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initialization function.

        Attributes:
            __size(int): size of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Initialization function.

        Attributes:
            __size(int): size of a side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Size function.

        Attributes:
            __size(int): size of a side of the square.

        Size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.

        If size is less than 0, raise a ValueError exception
        with the message size must be >= 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Function that calculates the current square area.

        Returns:
            Current square area.
        """
        return int(self.__size)**2
