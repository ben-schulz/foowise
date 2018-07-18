from . import Value

class DistSys:

    def __init__(self, infs):

        self.infs = infs

        clas = [i.proximal for i in infs] + [i.distal for i in infs]

        self._clas = {c.index:c for c in clas}
        self.clas = list(self._clas.values())
        self.indexes = tuple(self._clas.keys())


    def get_cla(self, ix):
        return self._clas.get(ix, None)


    def get_infomorphisms(self, prox_ix, dist_ix):

        if Value.Any == prox_ix:
            return [inf for inf in self.infs
                    if inf.distal.index == dist_ix]

        if Value.Any == dist_ix:
            return [inf for inf in self.infs
                    if inf.proximal.index == prox_ix]

        return [inf for inf in self.infs
                if inf.proximal.index == prox_ix
                and inf.distal.index == dist_ix]
