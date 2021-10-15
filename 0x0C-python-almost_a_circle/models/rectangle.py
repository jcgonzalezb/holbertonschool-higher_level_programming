#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from class Base. Width, height, x and y
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
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization function.
        Private instance attributes:
        __width: Width of the rectangle.
        __height: Height of the rectangle.
        __x: x of the rectangle.
        __y: y of the rectangle.
        Each with its own public getter and setter.
        Call the super class with id - this super call with use the
        logic of the __init__ of the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width function.
        This function has getter property.
        Returns:
            Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width function.
        This function has setter property.

        Args:
            value: Width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Height function.
        This function has getter property.
        Returns:
            Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height function.
        This function has setter property.

        Args:
            value: Height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x function.
        This function has getter property.
        Returns:
            x of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x of the rectangle.
        This function has setter property.

        Args:
            value: x of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y function.
        This function has getter property.
        Returns:
            y of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y of the rectangle.
        This function has setter property.

        Args:
            value: y of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
