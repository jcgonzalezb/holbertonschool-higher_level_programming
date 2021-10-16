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
        self.__height = size
        self.__width = size
        super().__init__(id, x, y)
        super().__init__(height, width)
        super().height()
        super().width()