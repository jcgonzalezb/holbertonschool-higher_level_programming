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
        width: Width of the rectangle.
        height: Height of the rectangle.
        x: x of the rectangle.
        y: y of the rectangle.
        Each with its own public getter and setter.
        Call the super class with id - this super call with use the
        logic of the __init__ of the Base class.
        """
        super().__init__(id, x, y)
        self.size = size
        self.height = size
        self.width = size

    def x(self):
        """
        x function.
        This function has getter property.
        Returns:
            x of the rectangle.
        """
        return super().x()

    def y(self):
        """
        y function.
        This function has getter property.
        Returns:
            y of the rectangle.
        """
        return super().y()

    def height(self):
        """
        Height function.
        This function has getter property.
        Returns:
            Height of the rectangle.
        """
        super().height()

    def width(self):
        """
        Width function.
        This function has getter property.
        Returns:
            Width of the rectangle.
        """
        return super().width

    @property
    def size(self):
        """
        Width function.
        This function has getter property.
        Returns:
            Width of the rectangle.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the width function.
        This function has setter property.

        Args:
            value: Width of the rectangle.
        Width must be an integer, otherwise raise a TypeError
        exception with the message width must be an integer.
        If width is under or equals 0, raise a ValueError exception
        with the message width must be > 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
    
    def __str__(self):
        """
        Function that prints [Square] (<id>) <x>/<y> - <size>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
               self.size)
