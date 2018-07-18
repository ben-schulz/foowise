from foowise.channels import Cla as C

from foowise.math import Set as S
from foowise.math import Relation as R

class Invariant(R.EqRelation):

    def __init__(self, cla, sigma, dual=False):

        if dual:
            cla = cla.dual

        parts = []
        toks = list(cla.tok)
        tok_reps = {}
        while toks:
            x = toks.pop()

            typs_x = cla.get_types(x, subset=sigma)

            part = { y for y in toks
                     if cla.types_agree(x, y, sigma) }

            for y in part:
                toks.remove(y)

            part.add(x)
            parts.append(part)
            tok_reps[x] = part

        R.EqRelation.__init__(self, cla.tok, parts)

        self.cla = cla
        self.sigma = sigma
        self.isdual = dual

        self.tok_reps = tok_reps


    def __str__(self):
        return str(self.parts)


    def canon_rep(self, x):
        return next(iter({y for y in self.tok_reps.keys()
                              if x in self.tok_reps[y]}))


    def quotient(self):

        c_dict = { }

        for x in self.tok_reps:
            c_dict[x] = self.cla.get_types(x, subset=self.sigma)

        cla = C.Cla(c_dict)

        if self.isdual:
            return cla.dual

        return cla
