import Set as S

import Cla as C
import Invariant as I


def get_invariant(cla):

    subset = S.Set.rand_subset(cla.typ)

    while True:
        yield I.Invariant(cla, next(subset))
