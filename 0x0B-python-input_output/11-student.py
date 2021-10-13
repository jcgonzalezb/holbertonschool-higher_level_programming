#!/usr/bin/python3
"""
Write a class Student.
Public instance attributes: first_name, last_name and age.
"""


class Student():
    """
    class Student in which def to_json(self) is
    defined as Public instance method.
    Public instance attributes:
        first_name, last_name and age.
    Methods:
        def __init__(self, first_name, last_name, age):
        def to_json(self, attrs=None)
        def reload_from_json(self, json):
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization function.
        Attributes:
            first_name: First name of the student.
            last_name: Last name of the student.
            age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This is a method that returns the dictionary description
        with simple data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object.

        Return:
            Only return dict of attrs given to us
            Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        This is a method that replaces all attributes
        of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute

        Return:
            Only return dict of attrs given to us
            Return entire dict if no attrs given
        """
        for k, v in json.items():
            setattr(self, k, v)
