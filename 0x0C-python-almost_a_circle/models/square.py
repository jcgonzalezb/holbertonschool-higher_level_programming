#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle. Width, height, x and y
    are defined as private instance attributes.
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)
        area(self)
        display(self)
        __str__(self)
        def update(self, *args)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization function.
        Private instance attributes:
        size: size of a side in square.
        x: x of the square.
        y: y of the square.
        Each with its own public getter and setter.
        Call the super class with id - this super call with use the
        logic of the __init__ of the Base class.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Size function.
        This function has getter property.
        Returns:
            Size of a side in square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size function.
        This function has setter property.

        Args:
            value: size of a side in square.
        The setter should assign (in this order) the width and the
        height - with the same value.
        The setter should have the same value validation as the
        Rectangle for width and height - No need to change the
        exception error message (It should be the one from width).
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Function that prints [Square] (<id>) <x>/<y> - <size>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
               self.size)
