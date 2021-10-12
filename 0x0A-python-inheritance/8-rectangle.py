#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle in which Instantiation with width
    and height.
    Methods:
        def __init__(self, width, height).
    """
    def __init__(self, width, height):
        """
        Initialization function.
        Attributes are private.
        Attributes:
            width(int): horizontal side of a rectangle.
            height(int): vertical side of a rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
