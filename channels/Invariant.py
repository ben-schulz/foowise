import Relation as R

class Invariant(R.Relation):

    def __init__(self, cla, sigma):

        r_dict = {}

        for x in cla.tok:
            r_dict[x] = set()
            for y in cla.tok:
                typ_x = {t for t in cla.get_types(x) if t in sigma}
                typ_y = {t for t in cla.get_types(y) if t in sigma}

                if typ_x.issubset(typ_y) \
                   and typ_y.issubset(typ_x):
                    r_dict[x].add(y)


        R.Relation.__init__(self, r_dict)

        self.cla = cla
        self.sigma = sigma

