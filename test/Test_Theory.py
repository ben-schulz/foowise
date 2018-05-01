import unittest

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


if __name__ == '__main__':
    unittest.main()
