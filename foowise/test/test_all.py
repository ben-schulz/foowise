import unittest
import os

import foowise.test

def additional_tests():

    this_suite_path = os.path.abspath(__file__)
    test_dir = os.path.dirname(this_suite_path)

    loader = unittest.TestLoader()
    return loader.discover(test_dir, pattern='Test_*.py')
