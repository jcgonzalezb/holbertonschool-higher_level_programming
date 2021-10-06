#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains several methods to test the
    6-max_integer.py file.
    """
    def test_00_max_integer(self):
        """This is a method to check correct values
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertAlmostEqual(max_integer([3.6, 4.6, 8.9]), 8.9)
        self.assertAlmostEqual(max_integer([-2, 2, 5, 4]), 5)
        self.assertAlmostEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertAlmostEqual(max_integer([-2, -4, -9, -5]), -2)
        self.assertAlmostEqual(max_integer([(2, 3)]), (2, 3))
        self.assertAlmostEqual(max_integer([[2, 3], [10, 5]]), [10, 5])

    def test_01_max_integer(self):
        """This is a method to check incorrect values
        """
        self.assertRaises(TypeError, max_integer, [1, '2', 4, 2])
        self.assertRaises(TypeError, max_integer, ['a', 1])
        self.assertRaises(TypeError, max_integer, ['2', 1])
        self.assertRaises(TypeError, max_integer, [[12, 32], 13, 4])
        self.assertRaises(TypeError, max_integer, [3 + 5j, 2, 5, 4])
