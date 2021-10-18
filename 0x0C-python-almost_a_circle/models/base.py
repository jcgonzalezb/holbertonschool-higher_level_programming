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
        def from_json_string(json_string):
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        If list_objs is None, save an empty list.
        The filename must be: <Class name>.json - example: Rectangle.json.
        Must use the static method to_json_string (created before).
        Must overwrite the file if it already exists.
        Attributes:
            list_objs: A list of instances who inherits of Base - example:
            list of Rectangle or list of Square instances.
        """
        objects = []
        if list_objs is None or len(list_objs) == 0:
            return list_objs == []
        else:
            for i in list_objs:
                objects.append(cls.to_dictionary(i))

        filename = cls.__name__ + ".json"
        with open(filename, "w") as outfile:
            outfile.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        If json_string is None or empty, return an empty list.
        Otherwise, return the list represented by json_string.

        Attributes:
            json_string: String representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            json_string == []
        else:
            return json.loads(json_string)
