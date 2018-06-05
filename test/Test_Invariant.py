import unittest

import Assert as A

from test_context import Cla as C
from test_context import Invariant as I
from test_context import Relation as R

class Test_Invariant(unittest.TestCase):

    def test_empty_invariant(self):

        cla = C.Cla({})
        sigma = set()

        result = I.Invariant(cla, sigma)

        self.assertNotEqual(None, result)


    def test_holds_respects_sigma(self):
        
        cla = C.Cla({
            'x':{1,2,3,4,5,6,7,8,9,10,11,12},
            'y':{2,4,6,8,10,12},
            'z':{3,6,9,12},
            'q':{2,4,8,16}
        })
        sigma = {2,4}

        inv = I.Invariant(cla, sigma)
        inv_pairs = inv.all_pairs()

        self.assertTrue(('x','y') in inv_pairs)


    def test_holds_defines_partition_of_cla_tok(self):

        cla = C.Cla({
            'x':{1,2,3,4,5,6,7},
            'y':{2,4,6,8,10,12},
            'z':{3,6,9,12},
            'q':{2,4,8,16}
        })
        sigma = {2,4}

        result = I.Invariant(cla, sigma)

        self.assertTrue(issubclass(type(result), R.EqRelation))


    def test_invariant_dualizable(self):
        cla = C.Cla({
            'x':{1,2,3,4,5,6,7},
            'y':{2,4,6,8,10,12},
            'z':{3,6,9,12},
            'q':{2,4,8,16}
        })

        sigma = {'x', 'y', 'q'}

        inv = I.Invariant(cla, sigma, dual=True)
        result = inv.all_pairs()

        self.assertTrue((2,4) in result)
        self.assertFalse((2,3) in result)


if __name__ == '__main__':
    unittest.main()
