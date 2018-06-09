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


    def test_union_produces_no_duplicate_elements(self):

        x = {1, 2, 3, 4, 5, 7}
        y = {2, 4, 6, 8}
        z = {3, 6, 9}

        result = S.Set.union(x,y,z)

        self.assertTrue(all(map(lambda n: n in result, x)))
        self.assertTrue(all(map(lambda n: n in result, y)))
        self.assertTrue(all(map(lambda n: n in result, z)))
        self.assertEqual(9, len(result))


    def test_is_partition_returns_true_on_disjoint_cover(self):

        sigma = {1,2,3,4,5,6,7,8,9}
        parts = [{1}, {3,5,7}, {2,4,8}, {6,9}]

        self.assertTrue(S.Set.is_partition(sigma, parts))


    def test_is_partition_returns_true_on_disjoint_cover_0(self):

        sigma = {'q', 'x', 'y', 'z'}
        parts = [{'x', 'y', 'q'}, {'z'}]

        self.assertTrue(S.Set.is_partition(sigma, parts))


    def test_is_partition_returns_false_on_nondisjoint_cover(self):

        sigma = {1,2,3,4,5,6,7,8,9}
        parts = [{1}, {3,2,5,7}, {2,4,8}, {6,9}]

        self.assertFalse(S.Set.is_partition(sigma, parts))


    def test_is_partition_returns_false_on_disjoint_noncover(self):

        sigma = {1,2,3,4,5,6,7,8,9}
        parts = [{1}, {5,7}, {2,4,8}, {6,9}]

        self.assertFalse(S.Set.is_partition(sigma, parts))


    def test_are_equal_returns_true_for_identical(self):

        left = {1,2,3,4,5}
        right = {5,4,2,1,3}

        self.assertTrue(S.Set.are_equal(left, right))


    def test_are_equal_returns_false_for_proper_subset(self):

        left = {1,2,4,5}
        right = {5,4,2,1,3}

        self.assertFalse(S.Set.are_equal(left, right))


    def test_are_equal_returns_false_for_nonshared_element(self):

        left = {1,2,4,5,103}
        right = {5,4,2,1,3}

        self.assertFalse(S.Set.are_equal(left, right))


    def test_rand_subset_returns_a_subset(self):

        x = {1,2,3,4}

        subset = S.Set.rand_subset(x)

        sets = [next(subset) for _ in range(0,32)]

        at_least_one_size_three = map(lambda y: 2 < len(y), sets)

        are_subsets = map(lambda y: y.issubset(x), sets)

        self.assertTrue(any(at_least_one_size_three))
        self.assertTrue(all(are_subsets))


if __name__ == '__main__':
    unittest.main()
