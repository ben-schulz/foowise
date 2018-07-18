from . import LinAlg as A
from. import Set as S

class Relation:

    def __init__(self, r_dict):

        self.left = set(r_dict.keys())
        self.right = S.Set.union(*(r_dict[x] \
                                   for x in r_dict.keys()))

        self.table_map_left = dict(zip(self.left, \
                                       range(0, len(self.left))))

        self.table_map_right = dict(zip(self.right, \
                                        range(0, len(self.right))))

        self.r_dict = r_dict
        self.table = A.Matrix(\
                              [[1 \
                                if a in r_dict \
                                and b in r_dict[a] \
                                else 0

                                for b in self.right]
                               for a in self.left]
                              )


    def holds(self, a, b):

        ix_a = self.table_map_left[a]
        ix_b = self.table_map_right[b]

        return 1 == self.table[ix_a, ix_b]


    def not_holds(self, a, b):

        ix_a = self.table_map_left[a]
        ix_b = self.table_map_right[b]

        return 0 == self.table[ix_a, ix_b]


    def all_pairs(self):

        return {(a,b) \
         for a in self.left
         for b in self.right
         if self.holds(a,b)}


class EqRelation(Relation):

    def __init__(self, sigma, parts):

        self.parts = parts

        if not S.Set.is_partition(sigma, parts):
            msg = "'EqRelation' must generate from a "\
                  "disjoint partition."
            raise ValueError(msg)

        r_dict = {}
        for p in parts:
            for x in p:
                if not x in r_dict:
                    r_dict[x] = p
        
        Relation.__init__(self, r_dict)
