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


    def test_all_pairs_returns_all_true_relations(self):

        r_dict = {
            'x': {'y', 'z'},
            'y': {'x', 'z'},
            'z': {'q'}
            }

        rel = R.Relation(r_dict)
        result = rel.all_pairs()

        self.assertEqual(5, len(result))

        for x in r_dict.keys():
            for v in r_dict[x]:
                self.assertTrue((x,v) in result)


    def test_EqRelation_generates_from_a_partition(self):

        sigma = {1,2,3,4,5,6,7,8,9}
        parts = [{1}, {2,4,8}, {3,6,9}, {5,7}]

        rel = R.EqRelation(sigma, parts)

        for p in parts:
            holds = [rel.holds(a,b) for a in p for b in p]
            self.assertTrue(all(holds))


    def test_EqRelation_raises_valueerror_on_not_disjoint(self):

        sigma = {1,2,3,4,5,6,7,8,9}
        parts = [{1}, {1,2,4,8}, {3,6,9}, {5,7}]

        try:
            rel = R.EqRelation(sigma, parts)
            msg = "Expected 'ValueError' raised."
            Assert.fail(msg)

        except ValueError:
            pass


    def test_EqRelation_raises_valueerror_on_not_cover(self):

        sigma = {1,2,3,4,5,6,7,8,9}
        parts = [{1}, {4,8}, {3,9}, {5,7}]

        try:
            rel = R.EqRelation(sigma, parts)
            msg = "Expected 'ValueError' raised."
            Assert.fail(msg)

        except ValueError:
            pass

        

            
if __name__ == '__main__':
    unittest.main()

