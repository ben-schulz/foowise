import unittest

from test_context import Set as S

class Test_Set(unittest.TestCase):

    def test_make_indexed_produces_correct_count(self):
        s = {'1','2','3','4','5','6'}

        result = S.Set.make_indexed(s)
        self.assertEqual(len(s), len(result))
        

    def test_union_includes_all_elements_if_disjoint(self):

        x = {'1','2','3','4','5','6'}
        y = {'7','8','9'}

        result = S.Set.union(x,y)

        self.assertEqual(len(x) + len(y), len(result))
        self.assertTrue(all(map(lambda z: z in result, x)))
        self.assertTrue(all(map(lambda z: z in result, y)))


if __name__ == '__main__':
    unittest.main()
