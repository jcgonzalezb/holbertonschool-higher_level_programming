#!/usr/bin/python3
"""
This project module contains one method that returns True
if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """This is a method that returns True or False.
    Returns:
        If the object is an instance of, or if the object
        is an instance of a class that inherited from, the
        specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
