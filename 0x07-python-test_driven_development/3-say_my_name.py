#!/usr/bin/python3
"""
This project module contains one method that prints My
name is <first name> <last name>. First_name and
last_name must be strings.
"""


def say_my_name(first_name, last_name=""):
    """This is a method that prints My name is <first name>
    <last name>. First_name and last_name must be strings.
    Returns:
        A text with the first name and last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
