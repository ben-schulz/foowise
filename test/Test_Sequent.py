import unittest

from test_context import JudgementSet as J
from test_context import Sequent as S

class Sequent_Test(unittest.TestCase):

    def test_sequent_lt_isSubsetRelation(self):

        _1 = J.JudgementSet({'alpha'})
        _2 = J.JudgementSet({'gamma'})

        _3 = J.JudgementSet({'alpha', 'beta'})
        _4 = J.JudgementSet({'beta', 'gamma'})
        
        _1_entails_2 = _1.entails(_2)
        _3_entails_4 = _3.entails(_4)

        self.assertTrue(_1_entails_2 < _3_entails_4)
        self.assertFalse(_3_entails_4 < _1_entails_2)

        self.assertFalse(_1_entails_2 < _1_entails_2)
        self.assertFalse(_3_entails_4 < _3_entails_4)

        
    def test_sequent_gt_isSubsetRelation(self):

        _1 = J.JudgementSet({'alpha'})
        _2 = J.JudgementSet({'gamma'})

        _3 = J.JudgementSet({'alpha', 'beta'})
        _4 = J.JudgementSet({'beta', 'gamma'})
        
        _1_entails_2 = _1.entails(_2)
        _3_entails_4 = _3.entails(_4)

        self.assertTrue(_3_entails_4 > _1_entails_2)
        self.assertFalse(_1_entails_2 > _3_entails_4)

        self.assertFalse(_1_entails_2 < _1_entails_2)
        self.assertFalse(_3_entails_4 < _3_entails_4)


    def test_sequent_le_isSubsetRelation(self):

        _1 = J.JudgementSet({'alpha'})
        _2 = J.JudgementSet({'gamma'})

        _3 = J.JudgementSet({'alpha', 'beta'})
        _4 = J.JudgementSet({'beta', 'gamma'})
        
        _1_entails_2 = _1.entails(_2)
        _3_entails_4 = _3.entails(_4)

        self.assertTrue(_1_entails_2 <= _3_entails_4)
        self.assertFalse(_3_entails_4 <= _1_entails_2)

        self.assertTrue(_1_entails_2 <= _1_entails_2)
        self.assertTrue(_3_entails_4 <= _3_entails_4)


    def test_sequent_ge_isSubsetRelation(self):

        _1 = J.JudgementSet({'alpha'})
        _2 = J.JudgementSet({'gamma'})

        _3 = J.JudgementSet({'alpha', 'beta'})
        _4 = J.JudgementSet({'beta', 'gamma'})
        
        _1_entails_2 = _1.entails(_2)
        _3_entails_4 = _3.entails(_4)

        self.assertTrue(_3_entails_4 >= _1_entails_2)
        self.assertFalse(_1_entails_2 >= _3_entails_4)

        self.assertTrue(_1_entails_2 >= _1_entails_2)
        self.assertTrue(_3_entails_4 >= _3_entails_4)



if __name__ == '__main__':
    unittest.main()
        
