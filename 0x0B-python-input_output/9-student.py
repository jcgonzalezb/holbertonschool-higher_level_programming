#!/usr/bin/python3
"""
Write a class Student.
Public instance attributes: first_name, last_name and age.
"""


class Student:
    """
    class Student in which def to_json(self) is
    defined as Public instance method.
    Public instance attributes:
        first_name, last_name and age.
    Methods:
        def __init__(self, first_name, last_name, age):
        def to_json(self):
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

    def to_json(self):
        """
        This is a method that returns the dictionary description
        with simple data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object.
        """
        return self.__dict__
