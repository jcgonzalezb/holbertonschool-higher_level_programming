#!/usr/bin/python3
"""
Write a class called Base.
"""


class Base:
    """
    class Base in which nb_objects is defined
    as Private class attribute.
    Methods:
        def to_json_string(list_dictionaries)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization function.
        If id is not None, assign the public instance
        attribute id with this argument value. Otherwise,
        increment __nb_objects and assign the new value
        to the public instance attribute id.
        Attributes:
            id: Number of identification.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        If list_dictionaries is None or empty, return the string: "[]".
        Otherwise, return the JSON string representation of list_dictionaries.
        Attributes:
            list_dictionaries: A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return list_dictionaries
