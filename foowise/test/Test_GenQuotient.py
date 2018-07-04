import unittest

import Cla as C
import Invariant as I
import GenQuotient as Q

class Test_GenQuotient(unittest.TestCase):

    def test_finds_an_invariant(self):

        c = C.Cla({
            'x': {1,2,3,4,5,6},
            'y': {2,4,6},
            'z': {3,6},
            'u': {2,4},
            'v': {1,3,5},
        })

        inv = next(Q.get_invariant(c))

        quot = inv.quotient()

        self.assertTrue(isinstance(inv, I.Invariant))


if __name__ == '__main__':
    unittest.main()
