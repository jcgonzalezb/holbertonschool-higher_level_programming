#!/usr/bin/python3
"""
This project module contains one method that reads
a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    This is a method that reads a text file (UTF8)
    and prints it to stdout:
    Returns:
        Prints a text file.
    """
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            print(line, end='')
