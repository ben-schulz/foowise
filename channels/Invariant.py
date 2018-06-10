import Cla as C

import Set as S
import Relation as R

class Invariant(R.EqRelation):

    def __init__(self, cla, sigma, dual=False):

        if dual:
            cla = cla.dual

        parts = []
        toks = list(cla.tok)
        while toks:
            x = toks.pop()
            typs_x = cla.get_types(x, subset=sigma)

            part = { y for y in toks
                     if cla.types_agree(x, y, sigma) }

            for y in part:
                toks.remove(y)

            part.add(x)
            parts.append(part)

        R.EqRelation.__init__(self, cla.tok, parts)

        self.cla = cla
        self.sigma = sigma
        self.isdual = dual


    def __str__(self):
        return str(self.parts)


    def quotient(self):

        c_dict = { }

        for p in self.parts:
            x = next(iter(p))
            c_dict[x] = self.cla.get_types(x, subset=self.sigma)

        cla = C.Cla(c_dict)

        if self.isdual:
            return cla.dual

        return cla
