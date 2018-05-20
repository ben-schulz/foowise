import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismConstraintError as IE
from test_context import InfoPair as IP

class Infomorphism_Test(unittest.TestCase):


    def createTestClassification(self):
        return C.Cla(tok= self.testTokens, typ=self.testTypes)


    def setUp(self):

        self.testTokens = {'x', 'y', 'z'}
        self.testTypes = {'alpha', 'beta', 'gamma'}


    def test_raiseInvalidInfomorphismErrorOnEmptyDomain(self):

        f_Up = lambda x : None
        f_Down = lambda x : None

        p = C.Cla.empty()
        d = self.createTestClassification()

        try:
            I.Infomorphism(p, d, f_Up, f_Down)

            self.assertTrue(False, "Expected 'InfomorphismConstraintError' raised.")

        except IE.InfomorphismConstraintError:
            pass

    def test_create_identityAlwaysValid(self):

        f_Up = lambda x : x
        f_Down = lambda x : x

        p = self.createTestClassification()
        d = self.createTestClassification()

        result = I.Infomorphism(p, d, f_Up, f_Down)

    def test_create_raiseErrorIfValidityViolatedForward(self):

        f_Up = lambda x : x
        f_Down = lambda x : 'alpha'

        p = self.createTestClassification()
        d = self.createTestClassification()

        p.add_validity('x', 'beta')
        d.add_validity('x', 'alpha')

        try:
            I.Infomorphism(p, d, f_Up, f_Down)
            self.assertTrue(False, "Expected 'InfomorphismConstraintError'.")

        except IE.InfomorphismConstraintError:
            pass


    def test_create_raiseErrorIfValidityViolatedBack(self):
        f_Up = lambda x : 'z'
        f_Down = lambda x : 'gamma'

        p = self.createTestClassification()
        d = self.createTestClassification()

        p.add_validity('z', 'alpha')
        d.add_validity('z', 'alpha')

        try:
            I.Infomorphism(p, d, f_Up, f_Down)
            self.assertTrue(False, "Expected 'InfomorphismConstraintError'.")

        except IE.InfomorphismConstraintError:
            pass


    def test_InfomorphismConstraintError_IncludesInvalidRels(self):

        f_Up = lambda x : x
        f_Down = lambda x : 'alpha'

        p = self.createTestClassification()
        d = self.createTestClassification()

        p.add_validity('x', 'beta')
        d.add_validity('x', 'alpha')

        try:
            I.Infomorphism(p, d, f_Up, f_Down)
            self.assertTrue(False, "Expected 'InfomorphismConstraintError'.")

        except IE.InfomorphismConstraintError as e:
            inDistal = IP.InfoPair.valid('x', 'alpha')
            notInProximal = IP.InfoPair.invalid('x', 'alpha')
            failureCase = (notInProximal, inDistal)

            message = 'Expected \'' + str(failureCase) + '\' but got: \'' + str(e.constraintViolations) + '\''
            self.assertTrue(failureCase in e.constraintViolations, message)


if __name__ == '__main__':
    unittest.main()
