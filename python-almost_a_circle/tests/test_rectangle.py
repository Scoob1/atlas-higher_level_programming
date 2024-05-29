#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0  # Reset the object count before each test
        self.maxDiff = None  # Reset the maxDiff attribute for detailed assertion errors

    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        
        # Add more test cases for different scenarios
        r2 = Rectangle(3, 5, 1, 1)
        self.assertEqual(r2.id, 2)
        
        # Test cases for attribute validation
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, -2)
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 2, -1, 0)
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 2, "invalid", 0)
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 2, 0, "invalid")

if __name__ == '__main__':
    unittest.main()
