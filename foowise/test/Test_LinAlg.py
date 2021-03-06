import unittest

import foowise.math.LinAlg as m

class Test_LinAlg(unittest.TestCase):

    def test_add_column(self):

        matrix = m.Matrix([[0,1,2],[3,4,5]])

        matrix.add_column()

        self.assertEqual(4, matrix.cols())
        self.assertEqual(2, matrix.rows())


if __name__ == '__main__':
    unittest.main()
