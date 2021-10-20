#!/usr/bin/python3
"""Unittest for square.py

-> Tested using python3 -m unittest tests/test_models/test_square.py
"""
import unittest
import json
from contextlib import redirect_stdout
from io import StringIO
from os import chdir, getcwd, remove
from models import base
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """This class contains several methods to test the
    square.py file.
    """
    def test_class(self):
        """Test class created is indeed Base"""
        self.assertTrue(Square(4, 5, 6, 1), self.__class__ == Square)
        s = Square(10)
        self.assertEqual(type(s), Square)

    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        s1 = Square(9, 99, 999, 1000)
        self.assertTrue(s1.width == 9)
        self.assertTrue(s1.height == 9)
        self.assertTrue(s1.size == 9)
        self.assertTrue(s1.x == 99)
        self.assertTrue(s1.y == 999)
        self.assertTrue(s1.id == 1000)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        s2 = Square(88)
        self.assertTrue(s2.width == 88)
        self.assertTrue(s2.height == 88)
        self.assertTrue(s2.size == 88)
        self.assertTrue(s2.x == 0)
        self.assertTrue(s2.y == 0)
        self.assertTrue(s2.id is not None)

    def test_attr_validated(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, 3])
            Square({20, })
            Square({"d": 20})
            Square(None)
            Square((30, 20), 4)
            Square(" ")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1, 1, 1)
            Square(-20, 1, 1, 1)
            Square(1, -1, 1, 1)
            Square(1, 1, -99, 1)
            Square(9).size(-9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "1", -99, 1)
            Square(1, [10, 3], -99, 1)
            Square(1, {10, 3}, -99, 1)
            Square(1, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "99")
            Square(1, 1, [10, 3])
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -3)

    def test_check_width_ValueError(self):
        """Test ValueError for width in Square"""
        self.assertRaisesRegex(
            ValueError,
            'width must be > 0',
            Square,
            -1, 0, 0, 12
        )

    def test_check_width_ValueError_2(self):
        """Test ValueError for width in Square"""
        self.assertRaisesRegex(
            ValueError,
            'width must be > 0',
            Square,
            0, 0, 0, 12
        )

    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        """Test too little args given throws error"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_class(self):
        """Test class created is indeed Rectangle"""
        s = Square(10)
        self.assertEqual(type(s), Square)

    def test_area(self):
        """Test method: area"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(4).display()
            b = bufr.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_print(self):
        """Test method: __str__"""
        s = Square(1, 2, 3, 44)
        s.size = 500
        self.assertEqual(str(s), '[Square] (44) 2/3 - 500')

    def test_update(self):
        """Test method: update(*args)"""
        s = Square(1, 2, 3, 4)
        s.update(10, 10, 10, 10)
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')
        s.update()
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')
        s.update(99)
        self.assertEqual(str(s), '[Square] (99) 10/10 - 10')
        s.update(99, 5)
        self.assertEqual(str(s), '[Square] (99) 10/10 - 5')
        s.update(44, 55, 1, 2)
        self.assertEqual(str(s), '[Square] (44) 1/2 - 55')
        """Test method: update(*kwargs)"""
        s.update(id=88, size=77, nokey=99)
        self.assertEqual(str(s), '[Square] (88) 1/2 - 77')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        s2 = Square(10, 10)
        s2.update(**sdic)
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')

    def test_create_type(self):
        """Test the create method
        """
        self.assertIsInstance(Square.create(), Square)
        self.assertIsInstance(Square.create(id=None), Square)
        self.assertIsInstance(Square.create(id=0), Square)
        self.assertIsInstance(Square.create(id=0.0), Square)
        self.assertIsInstance(Square.create(id="0"), Square)
        self.assertIsInstance(Square.create(id=(0,)), Square)
        self.assertIsInstance(Square.create(id=[0]), Square)
        self.assertIsInstance(Square.create(id={0}), Square)
        self.assertIsInstance(Square.create(id={0: 0}), Square)
        self.assertIsInstance(Square.create(id=True), Square)
        self.assertIsInstance(Square.create(id=type), Square)

    def test_create_id_equality(self):
        """Test the create method
        """
        square = Square(1)
        self.assertNotEqual(square.id, Square.create().id)
        self.assertNotEqual(square.id, Square.create(id=None).id)
        self.assertEqual(Square.create(id=0).id, 0)
        self.assertEqual(Square.create(id=0.0).id, 0.0)
        self.assertEqual(Square.create(id="0").id, "0")
        self.assertEqual(Square.create(id=(0,)).id, (0,))
        self.assertEqual(Square.create(id=[0]).id, [0])
        self.assertEqual(Square.create(id={0}).id, {0})
        self.assertEqual(Square.create(id={0: 0}).id, {0: 0})

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Square.create(id=True).id, True)
        self.assertIs(Square.create(id=type).id, type)
        self.assertIs(Square.create(id=None).id, None)

    def test_create_id_type(self):
        """Test the create method
        """
        self.assertIsInstance(Square.create().id, int)

    def test_save_to_file(self):
        """Test the save_to_file method
        """
        square = Square(1)
        types = (int, float, str, tuple, list, dict, bool)
        insts = [square] + [Square(1, id=t()) for t in types]
        fname = 'Square.json'
        try:
            remove(fname)
        except FileNotFoundError:
            pass
        self.assertIsNone(Square.save_to_file(None))
        with open(fname) as ifile:
            self.assertEqual(ifile.read(), '[]')
        for index in range(len(insts)):
            self.assertIsNone(Square.save_to_file(insts[index:]))
            with open(fname) as ifile:
                self.assertEqual(ifile.read(), Square.to_json_string(
                    [obj.to_dictionary() for obj in insts[index:]]
                ))
