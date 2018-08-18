import unittest

import foowise.channels.Cla as C
import foowise.channels.JudgeSet as J
import foowise.channels.Sequent as S
import foowise.channels.Theory as T

class Theory_Test(unittest.TestCase):

    def test_entailment_populatesOnInstantiate(self):

        alpha = J.JudgeSet({'alpha'})
        alpha_and_beta = J.JudgeSet({'alpha', 'beta'})

        beta_or_gamma = J.JudgeSet({'beta', 'gamma'})
        gamma = J.JudgeSet({'gamma'})

        constraints = {
            alpha.entails(beta_or_gamma),
            alpha_and_beta.entails(gamma)
            }

        theory = T.Theory(constraints=constraints)

        self.assertTrue(theory.isconsequent(alpha, beta_or_gamma))
        self.assertTrue(theory.isconsequent(alpha_and_beta, gamma))


    def test_from_classification_returnsCorrectEntailment(self):
        cla = C.Cla({
            'x' : {'1', '3'},
            'y' : {'2', '3'},
            'z' : {'1', '2'},
            'q' : {'1', '2', '3', '4'},
        })

        _1 = J.JudgeSet({'1'})
        _2_or_3 = J.JudgeSet({'2', '3'})

        _1_2_and_3 = J.JudgeSet({'1', '2', '3'})
        _4 = J.JudgeSet({'4'})


        theory = T.Theory.from_classification(cla)

        self.assertTrue(theory.isconsequent(_1, _2_or_3))
        self.assertTrue(theory.isconsequent(_1_2_and_3, _4))


    def test_to_vector_maps_types_to_indices(self):

        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'zeta', 'theta', 'omega'},
            }

        c = C.Cla(c_vals)
        ct = c.table
        theory = T.Theory.from_classification(c)

        judges = {'alpha', 'beta'}
        result = theory.to_vector(judges)

        self.assertEqual(1, result[ct.typ_to_col['alpha']])
        self.assertEqual(1, result[ct.typ_to_col['beta']])

        others = [t for t in c.typ if t not in judges]
        other_ixs = [ct.typ_to_col[t] for t in others]

        are_zero = [0 == result[i] for i in other_ixs]

        self.assertTrue(all(are_zero))


if __name__ == '__main__':
    unittest.main()
