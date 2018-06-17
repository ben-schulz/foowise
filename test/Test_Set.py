import unittest
import Assert as A
from test_context import Set as S

class Test_Set(unittest.TestCase):        


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

        are_subsets = map(lambda y: y.issubset(x), sets)

        self.assertTrue(all(are_subsets))


    def test_intersection_all_and_only_shared_elements(self):

        x0 = {1,2,3,4,5,6,7,8}
        x1 = {2,4,6,8,10,12}
        x2 = {3,6,9}

        result = S.Set.intersect(x0,x1,x2)

        A.Assert.sets_equal({6}, result)


    def test_insersection_of_no_sets_empty(self):

        A.Assert.sets_equal(set(), S.Set.intersect())


    def test_intersection_with_any_empty_set_is_empty(self):

        x0 = {1,2,3,4,5,6,7,8}
        x1 = {2,4,6,8,10,12}
        x2 = {3,6,9}
        x3 = set()


        A.Assert.sets_equal(set(), S.Set.intersect(x0,x1,x2,x3))


if __name__ == '__main__':
    unittest.main()
