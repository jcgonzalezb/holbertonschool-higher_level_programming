#!/usr/bin/python3
"""
This project module contains one method that prints
a text with 2 new lines after each of these characters:
., ? and :
"""


def text_indentation(text):
    """This is a method that prints a text with 2 new
    lines after each of these characters: ., ? and :.
    -text must be a string, otherwise raise a TypeError
    exception with the message text must be a string.
    -There should be no space at the beginning or at
    the end of each printed line.

    Returns:
        A text with 2 new lines after each of these
        characters: ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
