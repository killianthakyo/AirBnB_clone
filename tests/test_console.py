#!/usr/bin/python3
""" Unit tests for AirBnB console """

import unittest
import console
import pep8


class Test_Amenity(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def create(self):
        ''' create an instance of the HBNBCommand class'''
        return HBNBCommand()


if __name__ == '__main__':
    unittest.main()
