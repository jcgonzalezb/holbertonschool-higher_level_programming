#!/usr/bin/python3
"""
Write a class BaseGeometry.
"""


class BaseGeometry:
    """
    class BaseGeometry in which def area(self) and
    def integer_validator(self, name, value) are
    defined as Public instance method.

    Methods:
        def area(self):
        def integer_validator(self, name, value):
        def __init__(self, width, height):
    """


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
        Initialization function.
        Attributes:
            width(int): horizontal side of a rectangle.
            height(int): vertical side of a rectangle.
        """
        self.width = width
        self.height = height

    def width(self):
        """
        width function.
        Returns:
            horizontal side of a rectangle.
        """
        return self.__width

    def height(self):
        """
        height function.
        Returns:
            vertical side of a rectangle.
        """
        return self.__height

    def area(self):
        """
        This method raises an Exception with the
        message area() is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        This method validates value: can assume name is
        always a string.
        If value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer.
        If value is less or equal to 0: raise a ValueError
        exception with the message <name> must be greater than 0.
        """
        if (type(value) is not int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
