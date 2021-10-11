#!/usr/bin/python3
"""
Task 1.
Write a class MyList that inherits from list.
Public instance method: def print_sorted(self).
Prints the list, but sorted (ascending sort).
"""


class MyList(list):
    """
    class MyList in which def print_sorted(self) is
    defined as Public instance method.
    Args:
        list: Super class.
    Methods:
        def print_sorted(self):
    """
    def print_sorted(self):
        """
        Print method.
        Prints the list, but sorted (ascending sort).
        Assume that all the elements of the list will
        be of type int.
        """
        print(sorted(self))
