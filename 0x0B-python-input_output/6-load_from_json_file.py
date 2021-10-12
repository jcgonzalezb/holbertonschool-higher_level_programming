#!/usr/bin/python3
"""
This project module contains one method that creates an
Object from a “JSON file”.
"""


import json


def load_from_json_file(filename):
    """
    This is a method that creates an Object from a “JSON file”.
    """
    with open(filename, 'r') as filename:
        return json.load(filename)
