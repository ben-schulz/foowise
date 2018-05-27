import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismError as IE
from test_context import InfoPair as IP

class Infomorphism_Test(unittest.TestCase):

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


    def test_create_identityAlwaysValid(self):

        f_down = lambda x : x
        f_up = lambda x : x

        p = C.Cla({
            'x':{'alpha','beta'},
            'y':{'beta'}
        })
        d = C.Cla({
            'x':{'alpha','beta'},
            'y':{'beta'}
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


    def test_InfomorphismConstraintError_IncludesInvalidRels(self):

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

            inDistal = IP.InfoPair.valid('x', 'alpha')
            notInProximal = IP.InfoPair.invalid('x', 'alpha')
            failureCase = (notInProximal, inDistal)

            message = 'Expected \'' + str(failureCase) \
                      + '\' but got: \'' + str(e.violations) + '\''

            self.assertTrue(failureCase in e.violations, message)


if __name__ == '__main__':
    unittest.main()
