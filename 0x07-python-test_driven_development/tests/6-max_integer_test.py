#!/usr/bin/python3
"""
tests/6-max_integer_test: this module acts as a test file
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    An attempt to create our test object
    """

    def test_correct_maxint(self):
        """ This function tests for the correct output"""
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_neg_and_pos_maxint(self):
        """This function tests among negative numbers"""
        my_list = [-2, 3, 7, 4]
        self.assertEqual(max_integer(my_list), 7)

    def test_empty_maxint(self):
        """This function tests an empty list"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_string_maxint(self):
        """This function tests a list with strings and int"""
        my_list = ['julius', 4, 5]
        with self.assertRaises(TypeError):
            max_integer(my_list)

    def test_none_maxint(self):
        """This function tests None as arguments"""
        my_list = None
        with self.assertRaises(TypeError):
            max_integer(my_list)

    def test_all_neg_maxint(self):
        """This function tests all negative values"""
        my_list = [-1, -9, -3, -8]
        self.assertEqual(max_integer(my_list), -1)

    def test_one_element_maxint(self):
        """This function tests for only list of one item"""
        my_list = [2]
        self.assertEqual(max_integer(my_list), 2)

if __name__ == "__main__":
    unittest.main()
