import unittest

import foowise.channels.Cla as C
import foowise.channels.Infomorphism as I
import foowise.channels.DistSys as D
import foowise.channels.Channel as Ch

import foowise.heuristic.GenQuotient as Q

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
        inf1 = I.Infomorphism.canon_quot(c, inv1)

        inv2 = next(quot)
        inf2 = I.Infomorphism.canon_quot(c, inv2)

        inv3 = next(quot)
        inf3 = I.Infomorphism.canon_quot(c, inv3)

        d = D.DistSys({inf1, inf2, inf3})

        ch = Ch.Channel.colimit(d)


if __name__ == '__main__':
    unittest.main()
