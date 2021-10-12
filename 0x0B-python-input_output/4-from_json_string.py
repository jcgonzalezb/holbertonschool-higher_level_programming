#!/usr/bin/python3
"""
This project module contains one method that returns
an object (Python data structure) represented by a
JSON string.
"""


import json


def from_json_string(my_str):
    """
    This is a method that returns an object
    (Python data structure) represented by a JSON string.
    """
    return json.loads(my_str)
