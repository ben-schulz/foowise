import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismError as IE
from test_context import InfoPair as IP

class Infomorphism_Test(unittest.TestCase):


    def test_classification(self):
        return C.Cla(tok= self.testTokens, typ=self.testTypes)


    def setUp(self):

        self.testTokens = {'x', 'y', 'z'}
        self.testTypes = {'alpha', 'beta', 'gamma'}


    def test_raiseInvalidInfomorphismErrorOnEmptyDomain(self):

        f_down = lambda x : None
        f_up = lambda x : None

        p = C.Cla.empty()
        d = self.test_classification()

        try:
            I.Infomorphism(p, d, f_down, f_up)

            self.assertTrue(False, "Expected 'MorphismRangeError'.")

        except IE.MorphismRangeError:
            pass


    def test_create_identityAlwaysValid(self):

        f_down = lambda x : x
        f_up = lambda x : x

        p = self.test_classification()
        d = self.test_classification()

        result = I.Infomorphism(p, d, f_down, f_up)


    def test_create_raiseErrorIfValidityViolatedForward(self):

        f_down = lambda x : x
        f_up = lambda x : 'alpha'

        p = self.test_classification()
        d = self.test_classification()

        p.add_validity('x', 'beta')
        d.add_validity('x', 'alpha')

        try:
            I.Infomorphism(p, d, f_up, f_down)
            self.assertTrue(False, \
                            "Expected 'InfomorphismAxiomError'.")

        except IE.InfomorphismAxiomError:
            pass


    def test_create_raiseErrorIfValidityViolatedBack(self):

        f_up = lambda x : 'gamma'
        f_down = lambda x : 'z'

        p = self.test_classification()
        d = self.test_classification()

        p.add_validity('z', 'alpha')
        d.add_validity('z', 'alpha')

        try:
            I.Infomorphism(p, d, f_up, f_down)
            self.assertTrue(False, \
                            "Expected 'InfomorphismAxiomError'.")

        except IE.InfomorphismAxiomError:
            pass


    def test_InfomorphismConstraintError_IncludesInvalidRels(self):

        f_down = lambda x : x
        f_up = lambda x : 'alpha'

        p = self.test_classification()
        d = self.test_classification()

        p.add_validity('x', 'beta')
        d.add_validity('x', 'alpha')

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
