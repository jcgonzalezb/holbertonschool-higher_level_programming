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
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string):
        create(cls, **dictionary):
        load_from_file(cls):
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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
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
        if list_objs is not None:
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
        if json_string is None or json_string == []:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        You must use the method def update(self, *args, **kwargs).
        To use the update method to assign all attributes, you must create
        a “dummy” instance before:
        Create a Rectangle or Square instance with “dummy” mandatory attributes
        (width, height, size, etc.).
        Call update instance method to this “dummy” instance to apply your real
        values.
        **dictionary must be used as **kwargs of the method update.
        Attributes:
            **dictionary: A double pointer to a dictionary
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        The filename must be: <Class name>.json - example: Rectangle.json.
        If the file doesn’t exist, return an empty list.Otherwise, return
        a list of instances - the type of these instances depends on cls
        (current class using this method).
        You must use the from_json_string and create methods
        """
        filename_2 = cls.__name__ + ".json"
        try:
            with open(filename_2, 'r') as f:
                return [cls.create(**obj)
                        for obj in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
