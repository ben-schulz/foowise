import Cla as C
import Invariant as I

class Channel:

    def colimit(d):

        c_sum = C.Cla.sum(*d.clas)             

        infs = {(inf.proximal.index, inf.distal.index)
                for inf in d.infs}

        sigma = set()
        for p in c_sum.tok:

            for (i, x) in p:
                for (j, y) in p:

                    if not (i, j) in infs:
                        continue

                    add = True
                    for inf in d.get_infomorphisms(i, j):
                        add = add and inf.f_down[y] == x

                    if add:
                        sigma.add(p)

        return I.Invariant(c_sum, sigma, dual=True).quotient()
