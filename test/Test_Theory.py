import unittest

from test_context import Cla as C
from test_context import JudgementSet as J
from test_context import Sequent as S
from test_context import Theory as T

class Theory_Test(unittest.TestCase):

    def test_entailment_populatesOnInstantiate(self):

        alpha = J.JudgementSet({'alpha'})
        alpha_and_beta = J.JudgementSet({'alpha', 'beta'})

        beta_or_gamma = J.JudgementSet({'beta', 'gamma'})
        gamma = J.JudgementSet({'gamma'})

        constraints = {
            alpha.entails(beta_or_gamma),
            alpha_and_beta.entails(gamma)
            }

        theory = T.Theory(constraints=constraints)

        self.assertTrue(theory.isconsequent(alpha, beta_or_gamma))
        self.assertTrue(theory.isconsequent(alpha_and_beta, gamma))


    def test_fromClassification_returnsCorrectEntailment(self):
        cla = C.Cla({
            'x' : {'1', '3'},
            'y' : {'2', '3'},
            'z' : {'1', '2'},
            'q' : {'1', '2', '3', '4'},
        })

        _1 = J.JudgementSet({'1'})
        _3 = J.JudgementSet({'3'})

        _1_2_and_3 = J.JudgementSet({'1', '2', '3'})
        _4 = J.JudgementSet({'4'})


        theory = T.Theory.fromClassification(cla)

        self.assertTrue(theory.isconsequent(_1, _3))
        self.assertTrue(theory.isconsequent(_1_2_and_3, _4))

if __name__ == '__main__':
    unittest.main()
