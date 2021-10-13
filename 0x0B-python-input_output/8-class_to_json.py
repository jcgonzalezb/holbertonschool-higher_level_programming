#!/usr/bin/python3
"""
This project module contains one method that returns the
dictionary description with simple data structure (list,
dictionary, string, integer and boolean) for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    This is a method that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object.
    Args:
        obj: python object
    """
    return obj.__dict__
