import foowise.math.Set as S

import foowise.channels.Cla as C
import foowise.channels.Invariant as I


def get_invariant(cla):

    subset = S.Set.rand_subset(cla.typ)

    while True:
        yield I.Invariant(cla, next(subset))
