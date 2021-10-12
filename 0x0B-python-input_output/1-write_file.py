#!/usr/bin/python3
"""
This project module contains one method that writes
a string to a text file (UTF8) and returns the number
of characters written.
"""


def write_file(filename="", text=""):
    """
    This is a method that writes a string to a text
    file (UTF8).
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)
     
    return len(text)
