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


    def test_quotient_returns_correct_classification(self):

        cla = C.Cla({
            'x':{1,2,3,4,5,6,7},
            'y':{2,4,6,8,10,12},
            'z':{3,6,9,12},
            'q':{2,4,8,16}
        })

        sigma = {1, 6}

        inv = I.Invariant(cla, sigma)
        quot = inv.quotient()

        A.Assert.sets_equal(sigma, quot.typ)

        self.assertEqual(3, len(quot.tok))

        self.assertTrue(quot.is_valid('x', 1))

        self.assertTrue(quot.is_invalid('q', 1))
        self.assertTrue(quot.is_invalid('q', 6))

        if 'y' in quot.tok:
            self.assertTrue(quot.is_invalid('y', 1))
            self.assertTrue(quot.is_valid('y', 6))

        elif 'z' in quot.tok:
            self.assertTrue(quot.is_invalid('z', 1))
            self.assertTrue(quot.is_valid('z', 6))

        else:
            msg = 'Expected exactly one of {y, z} in result tokens.'
            self.assertTrue(False, msg)


    def test_dual_quotient_returns_correct_classification(self):

        cla = C.Cla({
            'x':{1,2,3},
            'y':{2,3},
            'z':{1,2},
            'q':{1,3}
        })

        sigma = {'x', 'y', 'z'}

        inv = I.Invariant(cla, sigma, dual=True)
        quot = inv.quotient()

        self.assertTrue(inv.isdual)
        A.Assert.sets_equal(sigma, quot.tok)

        self.assertEqual(3, len(quot.typ))

        if 1 in quot.typ:
            self.assertTrue(quot.is_valid('x', 1))

        elif 2 in quot.typ:
            self.assertTrue(quot.is_valid('x', 2))

        else:
            msg = 'Expected exactly one of {1, 2} in result types.'
            self.asserTrue(False, msg)


if __name__ == '__main__':
    unittest.main()
