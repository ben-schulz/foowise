import Set as S
import Relation as R

class Invariant(R.EqRelation):

    def __init__(self, cla, sigma):

        parts = []
        toks = list(cla.tok)
        while toks:
            x = toks.pop()
            typs_x = cla.get_types(x, subset=sigma)

            part = {y for y in toks if cla.agree_all(x, y, sigma)}

            for y in part:
                toks.remove(y)

            part.add(x)
            parts.append(part)

        R.EqRelation.__init__(self, cla.tok, parts)

        self.cla = cla
        self.sigma = sigma

