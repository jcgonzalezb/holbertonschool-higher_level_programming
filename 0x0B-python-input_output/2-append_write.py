#!/usr/bin/python3
"""
This project module contains one method that appends
a string at the end of a text file (UTF8) and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    This is a method that writes a string to a text
    file (UTF8).
    Returns:
        The number of characters added.
    """
    with open(filename, 'a', encoding='utf8') as f:
        nb_characters = f.write(''.join(text))

    return nb_characters
