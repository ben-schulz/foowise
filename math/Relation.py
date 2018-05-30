import LinAlg as A
import Set as S

class Relation:

    def __init__(self, r_dict):

        left = set(r_dict.keys())
        right = S.Set.union(*(r_dict[x] for x in r_dict.keys()))

        self.table_map_left = dict(zip(left,range(0, len(left))))
        self.table_map_right = dict(zip(right,range(0, len(right))))

        self.r_dict = r_dict
        self.table = A.Matrix(\
                              [[1 \
                                if a in r_dict \
                                and b in r_dict[a] \
                                else 0

                                for b in right]
                               for a in left]
                              )


    def holds(self, a, b):

        ix_a = self.table_map_left[a]
        ix_b = self.table_map_right[b]

        return 1 == self.table[ix_a, ix_b]


    def not_holds(self, a, b):

        ix_a = self.table_map_left[a]
        ix_b = self.table_map_right[b]

        return 0 == self.table[ix_a, ix_b]
