#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_positive_numbers(self):
        """Test case for a list of positive numbers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_negative_numbers(self):
        """Test case for a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

    def test_mixed_numbers(self):
        """Test case for a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-10, 20, -30, 40]), 40)

    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test case for a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_values(self):
        """Test case for a list with duplicate values."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        """Test case for a list of float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

"""
    def test_string_values(self):
        #Test case for a list with string values.
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_invalid_input(self):
        #Test case for invalid input
        with self.assertRaises(TypeError):
            max_integer("invalid input")
            """
