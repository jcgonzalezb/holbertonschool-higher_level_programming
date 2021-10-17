#!/usr/bin/python3
"""
Write a class called Base.
"""


import json


class Base:
    """
    class Base in which nb_objects is defined
    as Private class attribute.
    Methods:
        def to_json_string(list_dictionaries)
        def save_to_file(cls, list_objs)
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

    @staticmethod
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
            return json.dumps(list_dictionaries, sort_keys=True)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        If list_dictionaries is None or empty, return the string: "[]".
        Otherwise, return the JSON string representation of list_dictionaries.
        The filename must be: <Class name>.json - example: Rectangle.json.
        Must use the static method to_json_string (created before).
        Must overwrite the file if it already exists
        Attributes:
            list_objs: A list of instances who inherits of Base - example:
            list of Rectangle or list of Square instances.
        """
        if list_objs is None:
            return "[]"
        else:
            with open("Rectangle.json", "w") as outfile:
                json.dump(list(list_objs), outfile)
