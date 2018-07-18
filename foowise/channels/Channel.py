from . import Value
from . import Cla as C
from . import Invariant as I

from ..math import Set as S

class Channel:

    def colimit(d):

        c_sum = C.Sum(*d.clas)             

        infs = {(inf.proximal.index, inf.distal.index)
                for inf in d.infs}

        sigma_parts = []
        for dist_ix in range(0, len(d.clas)):

            dist_id = c_sum.ident_at(dist_ix)
            dist_infs = d.get_infomorphisms(Value.Any, dist_id)

            for f in dist_infs:
                prox_id = f.proximal.index
                prox_ix = c_sum.index_of(prox_id)

                toks = {x for x in c_sum.tok
                       if x[prox_ix] == f.f_down[x[dist_ix]]}

                sigma_parts.append(toks)

        sigma = S.Set.intersect(*sigma_parts)

        return I.Invariant(c_sum, sigma, dual=True).quotient()
