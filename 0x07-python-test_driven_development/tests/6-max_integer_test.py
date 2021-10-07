#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains several methods to test the
    6-max_integer.py file.
    """
    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_00_ints_floats(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 2]), 4)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([3.6, 4.6, 8.9]), 8.9)
        self.assertEqual(max_integer([3.6, 4.6, -8.9]), 4.6)
        self.assertEqual(max_integer([-2, 2, 5, 4]), 5)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-2, -4, -9, -5]), -2)
        self.assertEqual(max_integer([{2}, {3}, {4}]), {2})
        self.assertEqual(max_integer([{3, 9}, {4}, {5}]), {9, 3})

    def test_01_lists_tuples(self):
        self.assertEqual(max_integer([(2, 3)]), (2, 3))
        self.assertEqual(max_integer([[2, 3]]), [2, 3])
        self.assertEqual(max_integer([[2, 3], [10, 5]]), [10, 5])
        self.assertEqual(max_integer([(2, 3), (10, 5)]), (10, 5))

    def test_02_None(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([None]), None)

    def test_03_strings(self):
        self.assertEqual(max_integer(["a"]), 'a')
        self.assertEqual(max_integer(["abcopxyz"]), 'abcopxyz')
        self.assertEqual(max_integer("abcopxyz"), 'z')
        self.assertEqual(max_integer(["a", "b", "x", "y", "z"]), 'z')
        self.assertEqual(max_integer(["abx", "y", "z"]), 'z')
        self.assertEqual(max_integer(("12459")), '9')
        self.assertEqual(max_integer(["124", "5", "6", "79"]), '79')
        self.assertEqual(max_integer(("124", "5", "6", "79")), '79')

    def test_04_errors(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2', 4, 2])
        with self.assertRaises(TypeError):
            max_integer(['a', 1])
        with self.assertRaises(TypeError):
            max_integer([[12, 32], 13, 4])
        with self.assertRaises(TypeError):
            max_integer([3 + 5j, 2, 5, 4])
        with self.assertRaises(TypeError):
            max_integer({124, 5, 6, 79})
        with self.assertRaises(TypeError):
            max_integer({124, 5}, 6, 79)
        with self.assertRaises(TypeError):
            max_integer([{124, 5}, [6, 2], -79, {12, 56}])
        with self.assertRaises(TypeError):
            max_integer([{124}, [6, 2], -6.1, "str", (12, 56)])
        with self.assertRaises(TypeError):
            max_integer([None, True])

if __name__ == "__main__":
    unittest.main()
