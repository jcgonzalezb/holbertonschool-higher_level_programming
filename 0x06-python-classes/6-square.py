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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__position[1] > 0:
            print('')
        else:
            pass

        if self.__size == 0:
            print('')
        else:
            for i in range(1, self.__size+1):
                for j in range(1, self.__size+1):
                    print("#", end="")
                print()
