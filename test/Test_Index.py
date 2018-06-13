import unittest

from test_context import Index as I

class Test_Index(unittest.TestCase):


    def test_returns_distinct_with_no_args(self):

        first = I.Index()
        second = I.Index()

        self.assertNotEqual(first, second)


    def test_optionally_accepts_integer(self):

        i = I.Index(int_value=255)

        self.assertEqual(255, i.int)


    def test_from_int_produces_an_id_from_int(self):

        i = I.Index.from_int(255)

        self.assertEqual(255, i.int)


    def test_from_int_raises_error_on_bad_type(self):

        try:
            I.Index.from_int(object())
            self.assertFalse(True, "Expected 'TypeError' raised.")
        except TypeError:
            pass


    def test_compares_equal_when_int_value_equal(self):

        i = I.Index.from_int(255)

        self.assertEqual(255, i)


    def test_equality_reflexive(self):

        i = I.Index.from_int(255)

        self.assertEqual(i, i)


if __name__ == '__main__':
    unittest.main()
