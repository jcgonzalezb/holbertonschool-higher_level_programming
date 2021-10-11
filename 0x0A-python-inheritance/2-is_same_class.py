#!/usr/bin/python3
"""
This project module contains one method that returns True
if the object is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """This is a method that returns True or False.
    Returns:
        True if the object is exactly an instance of the
        specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    elif isinstance(obj, object):
        return False
    else:
        return True
