"""
M05 Programming Assignment - Tests
SDEV 220 - Software Development Using Python
Gabriel Abney

This is the testing program for the '__init__.py' file located in the 'project/my_sum/' folder.
"""

import unittest

from my_sum import sum

from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

# had to add extra trailing underscore, so '__main__' not '__main_' from given code on website
if __name__ == "__main__":
    unittest.main()