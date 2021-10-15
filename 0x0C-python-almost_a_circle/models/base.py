#!/usr/bin/python3
"""
Write a class called Base.
"""


class Base:
    """
    class Base in which nb_objects is defined
    as Private class attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization function.
        Attributes:
        id: Number of identification.
        If id is not None, assign the public instance
        attribute id with this argument value. Otherwise,
        increment __nb_objects and assign the new value
        to the public instance attribute id.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
