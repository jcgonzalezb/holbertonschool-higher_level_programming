#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
import json
from models import base
from models import rectangle
Rectangle = rectangle.Rectangle
Base = base.Base
Square = square.Square


class TestBase(unittest.TestCase):
    """This class contains several methods to test the
    base.py file.
    """

    def test_class(self):
        """Test class created is indeed Base"""
        self.assertTrue(Base(100), self.__class__ == Base)
    
    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(77), self.id == 77)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-10), self.id == -10)

    def test_id_not_given(self):
        """Test ids match incremented nb_objects when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
    
    def test_private_attr_access(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Base(50, 50)

