import unittest

from test_context import Relation as R
from test_context import Set as S

class Test_Relation(unittest.TestCase):

    def test_holds_true_for_all_inputs(self):

        r_dict = {
            'x': {'y', 'z'},
            'y': {'x', 'z'},
            'z': {'q'}
            }

        rel = R.Relation(r_dict)

        for x in r_dict.keys():
            for v in r_dict[x]:
                self.assertTrue(rel.holds(x, v))
                self.assertFalse(rel.not_holds(x, v))


    def test_holds_false_for_pair_not_in_input(self):

        r_dict = {
            'x': {'y', 'z'},
            'y': {'x', 'z'},
            'z': {'q'}
            }

        rel = R.Relation(r_dict)

        right_values = S.Set.union(*(r_dict.values()))

        for a in r_dict.keys():

            not_rels = [b for b in right_values \
                        if b not in r_dict[a]]

            holds = lambda x: rel.holds(a,x)
            not_holds = lambda x: rel.not_holds(a, x)

            holds_is_false = list(map(holds, not_rels))
            not_holds_is_true = list(map(not_holds, not_rels))

            self.assertFalse(all(holds_is_false))
            self.assertTrue(all(not_holds_is_true))

            
if __name__ == '__main__':
    unittest.main()

