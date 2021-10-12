#!/usr/bin/python3
"""
This project module contains one method that writes an
Object to a text file, using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This is a method that writes an Object to a text file,
    using a JSON representation.
    """
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename, sort_keys=True)
