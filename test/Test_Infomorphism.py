import unittest

import Assert as A

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Invariant as Inv

from test_context import InfomorphismError as IE


class Test_Infomorphism(unittest.TestCase):

    def test_raiseInvalidInfomorphismErrorOnEmptyDomain(self):

        f_down = lambda x : None
        f_up = lambda x : None

        p = C.Cla.empty()
        d = C.Cla({
            'x':{'alpha'},
            'y':{'beta'}
        })

        try:
            I.Infomorphism(p, d, f_down, f_up)

            self.assertTrue(False, "Expected 'MorphismRangeError'.")

        except IE.MorphismRangeError:
            pass


    def test_identity_valid(self):

        f_down = lambda x: x
        f_up = lambda x: x

        p = C.Cla({
            'x':{'alpha','beta'},
            'y':{'beta'}
        })

        d = C.Cla({
            'x':{'alpha','beta'},
            'y':{'beta'}
        })

        result = I.Infomorphism(p, d, f_up, f_down)


    def test_inclusion_valid(self):

        f_down = lambda x: x
        f_up = lambda x: x

        p = C.Cla({
            'x':{'beta'},
            'y':{'beta'}
        })
        d = C.Cla({
            'x':{'alpha','beta'}
        })

        result = I.Infomorphism(p, d, f_down, f_up)
        


    def test_create_raiseErrorIfValidityViolatedForward(self):

        f_down = lambda x : x
        f_up = lambda x : 'alpha'

        p = C.Cla({
            None:{'alpha','gamma'},
            'x':{'beta'},
            'y':set(),
            'z':set()
            })

        d = C.Cla({
            None:{'beta', 'gamma'},
            'x':{'alpha'},
            'y':set(),
            'z':set()
            })

        try:
            I.Infomorphism(p, d, f_up, f_down)
            self.assertTrue(False, \
                            "Expected 'InfomorphismAxiomError'.")

        except IE.InfomorphismAxiomError:
            pass


    def test_create_raiseErrorIfValidityViolatedBack(self):

        f_up = lambda x : 'gamma'
        f_down = lambda x : 'z'

        p = C.Cla({
            None:{'alpha','gamma'},
            'x':set(),
            'y':set(),
            'z':{'alpha'}
            })

        d = C.Cla({
            None:{'beta', 'gamma'},
            'x':set(),
            'y':set(),
            'z':{'alpha'}
            })

        try:
            I.Infomorphism(p, d, f_up, f_down)
            self.assertTrue(False, \
                            "Expected 'InfomorphismAxiomError'.")

        except IE.InfomorphismAxiomError:
            pass


    def test_infomorphismconstrainterror_includes_invalids(self):

        f_down = lambda x : x
        f_up = lambda x : 'alpha'

        p = C.Cla({
            None:{'alpha','gamma'},
            'x':{'beta'},
            'y':set(),
            'z':set()
            })

        d = C.Cla({
            None:{'beta', 'gamma'},
            'x':{'alpha'},
            'y':set(),
            'z':set()
            })

        try:
            I.Infomorphism(p, d, f_up, f_down)
            self.assertTrue(False, \
                            "Expected 'InfomorphismAxiomError'.")

        except IE.InfomorphismAxiomError as e:

            in_distal = I.Infomorphism.InfoPair.valid('x', 'alpha')

            not_in_proximal = (I.Infomorphism.InfoPair
                             .invalid('x', 'alpha'))

            failureCase = (not_in_proximal, in_distal)

            message = 'Expected \'' + str(failureCase) \
                      + '\' but got: \'' + str(e.violations) + '\''

            self.assertTrue(failureCase in e.violations, message)


    def test_canon_quot_produces_the_canonical_quotient(self):

        c = C.Cla({
            'x':{1,2,3,4,5,6,7,8,9,10},
            'y':{1,3,5,7,9},
            'z':{2,4,6,8,10},
            'u':{3,6,9},
            'v':{5,10},
            'w':{2,3,5,7}
        })

        sigma = {2,3,5}
        inv = Inv.Invariant(c, sigma)

        quot = I.Infomorphism.canon_quot(c, inv)

        self.assertTrue(isinstance(quot, I.Infomorphism))
        self.assertTrue(quot.proximal.typ.issubset(c.typ))

        toks_map_to_eq_classes = [inv.canon_rep(x)
                                  == quot.f_down[x]
                                  for x in c.tok]

        self.assertTrue(all(toks_map_to_eq_classes))


    def test_infomorphism_dualizable(self):

        prox = C.Cla({
            'x': {1}
        })

        dist = C.Cla({
            'y': {2}
        })

        f_up = lambda _: 2
        f_down = lambda _: 'x'

        inf = I.Infomorphism(prox, dist, f_up, f_down)


        self.assertTrue(isinstance(inf.dual.proximal, C.Cla))
        self.assertTrue(isinstance(inf.dual.distal, C.Cla))

        A.Assert.sets_equal(inf.dual.proximal.tok,
                            inf.distal.tok)

        A.Assert.sets_equal(inf.dual.distal.typ,
                            inf.proximal.typ)

        self.assertEqual(inf.dual.f_down[1],
                         inf.f_up[1])

        self.assertEqual(inf.dual.f_up['y'],
                         inf.f_down['y'])


if __name__ == '__main__':
    unittest.main()
