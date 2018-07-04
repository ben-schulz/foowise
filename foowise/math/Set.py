import functools as f
import itertools as it

import random

class Set:

    def are_equal(left, right):
        return left.issubset(right) and right.issubset(left)


    def product(*xs):

        if xs:
            return it.product(*xs)

        return set()


    def union(*xs):
        return f.reduce(lambda y,z: z.union(y), xs, set())


    def intersect(*xs):

        if not xs:
            return set()
        
        return f.reduce(lambda y,z: z.intersection(y), xs, xs[0])


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


    def rand_subset(x):

        _x = list(x)
        l_x = len(x)

        def in_range():
            return random.randint(0, l_x-1)

        while True:
            size = random.randint(1, l_x-1)

            rand_ixs = {in_range() for _ in range(0,size)}

            yield {_x[i] for i in rand_ixs}
