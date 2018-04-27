import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismConstraintError as IE

class Infomorphism_Test(unittest.TestCase):

    def setUp(self):

        self.testTokens = {'x', 'y', 'z'}
        self.testTypes = {'alpha', 'beta', 'gamma'}
        self.testClassification = C.Cla(tok=self.testTokens, typ=self.testTypes)


    def test_throwInvalidInfomorphismExceptionOnEmptyDomain(self):

        f_Up = lambda x : None
        f_Down = lambda x : None

        p = C.Cla.Empty()
        d = self.testClassification

        try:
            I.Infomorphism(p, d, f_Up, f_Down)

            self.assertTrue(False, "Expected 'InfomorphismConstraintError' raised.")

        except IE.InfomorphismConstraintError:
            pass

    def test_create_identity(self):

        f_Up = lambda x : x
        f_Down = lambda x : x

        p = self.testClassification
        d = self.testClassification

        result = I.Infomorphism(p, d, f_Up, f_Down)

        

if __name__ == '__main__':
    unittest.main()