#!/usr/bin/python3
"""
This project module contains one method that returns
an object (Python data structure) represented by a
JSON string.
"""


import json


def to_json_string(my_obj):
    """
    This is a method that returns an object (Python
    data structure) represented by a JSON string.
    """
    return json.dumps(my_obj, sort_keys=True)
