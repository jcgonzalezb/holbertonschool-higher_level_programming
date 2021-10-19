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
        area(self)
        display(self)
        __str__(self)
        update(self, *args)
        to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
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
        Width must be an integer, otherwise raise a TypeError
        exception with the message width must be an integer.
        If width is under or equals 0, raise a ValueError exception
        with the message width must be > 0.
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
        Height must be an integer, otherwise raise a TypeError
        exception with the message height must be an integer.
        If height is under or equals 0, raise a ValueError exception
        with the message height must be > 0.
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
        x must be an integer, otherwise raise a TypeError
        exception with the message x must be an integer.
        If x is under 0, raise a ValueError exception
        with the message x must be >= 0.
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
        y must be an integer, otherwise raise a TypeError
        exception with the message y must be an integer.
        If y is under 0, raise a ValueError exception
        with the message y must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This function returns area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Function that prints in stdout the rectangle
        with the character #.
        Returns:
            Rectangle with the character #.
        """
        if self.width == 0:
            print('')
        elif self.height == 0:
            print('')
        else:
            print('\n' * self.__y +
                  '\n'.join([' ' * self.__x +
                            '#' * self.width for rows in range(self.height)]))

    def __str__(self):
        """
        Function that prints [Rectangle] <width>/<height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
               self.width, self.height)

    def update(self, *args, **kwargs):
        """
        This function assigns an argument to each attribute and
        assigns a key/value argument to attributes.

        **kwargs can be thought of as a double pointer to a
        dictionary: key/value.
        Each key in this dictionary represents an attribute to
        the instance.
        **kwargs must be skipped if *args exists and is not empty.

        Args:
            1st argument should be the id attribute.
            2nd argument should be the width attribute.
            3rd argument should be the height attribute.
            4th argument should be the x attribute.
            5th argument should be the y attribute.
        """
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        if "id" in kwargs:
            self.id = kwargs.get("id")
        if "width" in kwargs:
            self.width = kwargs.get("width")
        if "height" in kwargs:
            self.height = kwargs.get("height")
        if "x" in kwargs:
            self.x = kwargs.get("x")
        if "y" in kwargs:
            self.y = kwargs.get("y")

    def to_dictionary(self):
        """
        This function returns the dictionary representation
        of a Rectangle.
        This dictionary must contain: id, width, height, x, y.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
