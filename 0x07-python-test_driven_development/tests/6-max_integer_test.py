#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_variousFunction(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([-5, 2, 5]), 5)
        self.assertEqual(max_integer([-5, -2, -3]), -2)
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_Error(self):
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_Error_2(self):
        with self.assertRaises(TypeError):
            max_integer(4, 2, 1, 2)

    def test_Error_3(self):
        with self.assertRaises(TypeError):
            max_integer("Melkin", 1)

    def test_Error_4(self):
        with self.assertRaises(TypeError):
            max_integer("", "")


if __name__ == '__main__':
    unittest.main()
