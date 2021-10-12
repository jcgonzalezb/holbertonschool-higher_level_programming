#!/usr/bin/python3
"""
This project module contains one method that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """This is a method that returns True or False.
    Returns:
        If the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False.
    """

    if ((type(obj) is not a_class) and issubclass(type(obj), a_class)):
        return True
    else:
        return False
