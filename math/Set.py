import functools as f
import itertools as it

class Set:

    def are_equal(left, right):
        return left.issubset(right) and right.issubset(left)

    def product(*xs):
        return it.product(*xs)


    def union(*xs):
        return f.reduce(lambda y,z: z.union(y), xs, set())


    def make_indexed(s):
        return set(zip(range(0,len(s)), s))


    def is_partition(sigma, parts):

        _parts = list(parts)
        while(_parts):

            p = _parts.pop()
            are_disj = map(lambda x: p.isdisjoint(x), _parts)

            if not all(are_disj):
                return False

        _union_parts = Set.union(*parts)
        if not _union_parts.issubset(sigma) \
           or not sigma.issubset(_union_parts):
            return False

        return True
