#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
import json
from models import base
from models import rectangle
Rectangle = rectangle.Rectangle
Base = base.Base


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

    def test_to_json_string(self):
        """Test dict given translates into JSON string"""
        d0 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d1 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        strd01 = Base.to_json_string([d0, d1])
        self.assertTrue(type(d0) == dict)
        self.assertTrue(type(strd01) == str)
        self.assertTrue(strd01,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

    def test_none_to_json_string(self):
        """Test no dict given translates into JSON string of empty dict"""
        d2 = None
        strd2 = Base.to_json_string([d2])
        self.assertTrue(type(strd2) == str)
        self.assertTrue(strd2, "[]")

    def test_empty_to_json_string(self):
        """Test empty dict given translates into JSON string of empty dict"""
        d3 = dict()
        strd3 = Base.to_json_string([d3])
        self.assertTrue(len(d3) == 0)
        self.assertTrue(type(strd3) == str)
        self.assertTrue(strd3, "[]")
