import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismConstraintError as IE
from test_context import InfoPair as IP

class Infomorphism_Correctness(unittest.TestCase):


    def expect_infomorphism(self, c1, c2, f_Up, f_Down):

        try:
            I.Infomorphism(c1, c2, f_Up, f_Down)

        except IE.InfomorphismConstraintError as e:
            raise e


    def expect_axiom_violation(self, c1, c2, f_Up, f_Down, expected_violations=None):

        violation_list_message = ''
        
        message = 'Expected infomorphism failed'
        if expected_violations:
            for v in expected_violations:
                violation_list_message += repr(v) + '\n'
            message += ' due to: ' + violation_list_message

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


    def test_minNonemptyNotInfomorphic(self):

        v1 = {'x': 'alpha', 'y':'beta'}
        v2 = {'x': 'alpha'}

        c1 = C.Cla(validities=v1)
        c2 = C.Cla(validities=v2)

        f_Up = lambda x: 'x'
        f_Down = lambda x: 'alpha'

        expected_violations = [IP.InfoPair.invalid('y', 'alpha')]

        self.expect_axiom_violation(c1, c2, f_Up, f_Down, expected_violations=expected_violations)


if __name__ == '__main__':
    unittest.main()
        
