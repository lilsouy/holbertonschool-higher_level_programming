#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        """Test a list where max is at the beginning."""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_at_end(self):
        """Test a list where max is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_negative_integers(self):
        """Test a list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test a list with integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2, 3.7]), 3.7)

    def test_duplicates(self):
        """Test a list with duplicate max values."""
        self.assertEqual(max_integer([5, 5, 2, 5]), 5)

if __name__ == '__main__':
    unittest.main()
