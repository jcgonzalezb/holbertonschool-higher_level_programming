#!/usr/bin/python3
"""
Write a class BaseGeometry.
"""


class BaseGeometry:
    """
    class BaseGeometry in which def area(self) is
    defined as Public instance method. This method
    raises an Exception with the message area()
    is not implemented.

    Methods:
        def area(self):
    """
    def area(self):
        raise Exception('area() is not implemented')
