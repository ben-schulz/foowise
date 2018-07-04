import unittest

from test_context import LinAlg as m

class Test_LinAlg(unittest.TestCase):

    def test_add_row(self):

        matrix = m.Matrix([[0,1,2]])

        matrix.add_row()

        self.assertEqual(3, matrix.cols())
        self.assertEqual(2, matrix.rows())


    def test_add_column(self):

        matrix = m.Matrix([[0,1,2],[3,4,5]])

        matrix.add_column()

        self.assertEqual(4, matrix.cols())
        self.assertEqual(2, matrix.rows())


if __name__ == '__main__':
    unittest.main()
