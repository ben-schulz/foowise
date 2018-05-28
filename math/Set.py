import functools as f
import itertools as it

class Set:

    def product(*xs):
        return it.product(*xs)

    def union(*xs):
        return f.reduce(lambda y,z: z.union(y), xs, set())

    def make_indexed(s):
        return set(zip(range(0,len(s)), s))
