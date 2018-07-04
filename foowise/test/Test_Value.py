import unittest

from test_context import Index as Id
from test_context import Value as V

class Test_Value(unittest.TestCase):

    def test_values_compare_equal_on_id_and_name(self):

        _id = Id.Index.from_int(1)

        v_left1 = V.Value(_id, 'x')
        v_left2 = V.Value(_id, 'x')

        self.assertEqual(v_left1, v_left2)


    def test_values_compare_unequal_on_unequal_index(self):

        _id1 = Id.Index.from_int(1)
        _id2 = Id.Index.from_int(2)

        v_x1 = V.Value(_id1, 'x')
        v_x2 = V.Value(_id2, 'x')

        self.assertNotEqual(v_x1, v_x2)


    def test_values_compare_unequal_on_unequal_name(self):

        _id = Id.Index.from_int(1)
        v_x = V.Value(_id, 'x')
        v_y = V.Value(_id, 'y')

        self.assertNotEqual(v_x, v_y)


if __name__ == '__main__':
    unittest.main()
