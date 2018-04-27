import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismConstraintError as IE

class Infomorphism_Test(unittest.TestCase):


    def createTestClassification(self):
        return C.Cla(tok= self.testTokens, typ=self.testTypes)


    def setUp(self):

        self.testTokens = {'x', 'y', 'z'}
        self.testTypes = {'alpha', 'beta', 'gamma'}


    def test_raiseInvalidInfomorphismErrorOnEmptyDomain(self):

        f_Up = lambda x : None
        f_Down = lambda x : None

        p = C.Cla.Empty()
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

        p.addValidity('x', 'beta')
        d.addValidity('x', 'alpha')

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

        p.addValidity('z', 'alpha')
        d.addValidity('z', 'alpha')

        try:
            I.Infomorphism(p, d, f_Up, f_Down)
            self.assertTrue(False, "Expected 'InfomorphismConstraintError'.")

        except IE.InfomorphismConstraintError:
            pass


if __name__ == '__main__':
    unittest.main()
