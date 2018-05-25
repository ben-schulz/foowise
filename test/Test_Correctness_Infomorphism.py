import unittest

from test_context import Infomorphism as I
from test_context import Cla as C
from test_context import Validity as V
from test_context import InfomorphismConstraintError as IE
from test_context import InfoPair as IP

class Infomorphism_Correctness(unittest.TestCase):


    def expect_infomorphism(self, p, d, f_up, f_down):

        try:
            I.Infomorphism(p, d, f_up, f_down)

        except IE.InfomorphismConstraintError as e:
            raise e


    def expect_axiom_violation(self, p, d, f_up, f_down, expected_violations=None):

        violation_list_message = ''
        
        message = 'Expected infomorphism failed'
        if expected_violations:
            for v in expected_violations:
                violation_list_message += repr(v) + '\n'
            message += ' due to: ' + violation_list_message

        try:
            I.Infomorphism(p, d, f_up, f_down)
            self.assertTrue(False, message)

        except IE.InfomorphismConstraintError as e:
            pass


    def test_small_identity(self):

        v1 = {
            'x':{'alpha', 'beta'},
            'y':{'beta'}
            }

        p = C.Cla(validities=v1)
        d = C.Cla(validities=v1)

        f_up = lambda x: x
        f_down = lambda x: x

        self.expect_infomorphism(p, d, f_up, f_down)


    def test_singleton_classifications(self):

        p_vals = [('x', 'alpha')]
        d_vals = [('y', 'beta')]

        p = C.Cla(validities=p_vals)
        d = C.Cla(validities=d_vals)

        f_up = lambda x: 'beta'
        f_down = lambda x: 'x'

        self.expect_infomorphism(p, d, f_up, f_down)


    def test_minNonemptyNotInfomorphic(self):

        v1 = [('x', 'alpha')]
        v2 = [('x','alpha'), ('y', 'beta')]

        p = C.Cla(validities=v1)
        d = C.Cla(validities=v2)

        f_up = lambda x: 'alpha'
        f_down = lambda x: 'x'

        expected_violations = [IP.InfoPair.invalid('y', 'alpha')]

        self.expect_axiom_violation(p, d, f_up, f_down, expected_violations=expected_violations)


if __name__ == '__main__':
    unittest.main()
        
