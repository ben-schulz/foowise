import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismConstraintError as IE

class Infomorphism_Correctness(unittest.TestCase):


    def expect_infomorphism(self, c1, c2, f_Up, f_Down):

        try:
            I.Infomorphism(c1, c2, f_Up, f_Down)

        except IE.InfomorphismConstraintError as e:
            raise e


    def expect_axiom_violation(self, c1, c2, f_Up, f_Down, expected_violations):

        message = 'Expected infomorphism failed due to: '
        try:
            I.Infomorphism(c1, c2, f_Up, f_Down)
            self.assertTrue(False, message)

        except IE.InfomorphismConstraintError as e:
            pass


    def test_small_identity(self):

        v1 = {
            'x':{'alpha', 'beta'},
            'y':{'beta'}
            }

        c1 = C.Cla(validities=v1)
        c2 = C.Cla(validities=v1)

        f_Up = lambda x: x
        f_Down = lambda x: x

        self.expect_infomorphism(c1, c2, f_Up, f_Down)


    def test_singleton_classifications(self):

        v1 = [('x', 'alpha')]
        v2 = [('y', 'beta')]

        c1 = C.Cla(validities=v1)
        c2 = C.Cla(validities=v2)

        f_Up = lambda x: 'y'
        f_Down = lambda x: 'alpha'

        self.expect_infomorphism(c1, c2, f_Up, f_Down)


if __name__ == '__main__':
    unittest.main()
        
