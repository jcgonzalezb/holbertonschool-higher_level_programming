#!/usr/bin/python3
"""
Task 6.
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
        position

    functions:
        __init__(self, size=0, position=(0, 0))
        def size(self)
        def size(self, value)
        def position(self)
        def position(self, value)
        area(self)
        def my_print(self)

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization function.

        Attributes:
            __size(int): size of a side of the square.
            __position(tuple): position inside a square.

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Size function.
        This fuction has getter property.

        Returns:
            size of a side of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Size function.
        This fuction has setter property.

        Args:
            value: Assign size to value.

        Size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.

        If size is less than 0, raise a ValueError exception
        with the message size must be >= 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
        Position function.
        This fuction has getter property.

        Returns:
            position inside a square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Position function.
        This fuction has setter property.

        Args:
            value: Assign position to value.

        Position must be a tuple of 2 positive integers,
        otherwise raise a TypeError exception with the
        message position must be a tuple of 2 positive integers

        If size is less than 0, raise a ValueError exception
        with the message size must be >= 0.
        """
        if not (type(position) is tuple and
                len(position) == 2 and
                type(position[0]) is int and
                type(position[1]) is int and
                position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        Function that calculates the current square area.

        Returns:
            Current square area.
        """
        return int(self.__size)**2

    def my_print(self):
        """
        Function that prints in stdout the square
        with the character #.

        Returns:
            Square with the character #.
        """
        if self.__size == 0:
            print('')
        else:
            print('\n' * self.__position[1], end='')
            print("\n".join([' ' * self.__position[0] +
                            '#' * self.__size
                             for rows in range(self.__size)]))
