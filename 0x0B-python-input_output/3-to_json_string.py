#!/usr/bin/python3
"""
This project module contains one method that returns
the JSON representation of an object (string).
"""


import json


def to_json_string(my_obj):
    """
    This is a method that returns the JSON representation
    of an object (string).
    """
    return json.dumps(my_obj)
