import unittest

from test_context import Cla as C
from test_context import Infomorphism as I

from test_context import Channel as Ch
from test_context import GenQuotient as Q

class Test_Channel(unittest.TestCase):


    def test_colimit_0(self):

        c = C.Cla({
            'prime' : {2,3,5,7,11,13},
            'comp'  : {1,4,6,8,9,10,12},
            'odd'   : {1,3,5,7,9,11,13},
            'even'  : {2,4,6,8,10,12},
            'threes': {3,6,9,12},
            'sixes ': {6,12}
        })

        quot = Q.get_invariant(c)

        inv1 = next(quot)
        q1 = inv1.quotient()

        inv2 = next(quot)
        q2 = inv2.quotient()

        inv3 = next(quot)
        q3 = inv3.quotient()



if __name__ == '__main__':
    unittest.main()
