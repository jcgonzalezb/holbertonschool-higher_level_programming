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

    def update(self, *args, **kwargs):
        """
        This function assigns an argument to each attribute and
        assigns a key/value argument to attributes.
        **kwargs can be thought of as a double pointer to a
        dictionary: key/value (keyworded arguments).
        Each key in this dictionary represents an attribute to
        the instance.
        **kwargs must be skipped if *args exists and is not empty.
        Each key in this dictionary represents an attribute to the instance.
        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.size = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        if "id" in kwargs:
            self.id = kwargs.get("id")
        if "size" in kwargs:
            self.width = kwargs.get("size")
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
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
