import Cla as C
import Invariant as I

class Channel:

    def colimit(clas, infs):

        if 3 != len(clas) or 2 != len(infs):
            raise NotImplemented

        c_sum = C.Cla.sum(*clas) 

        sigma = {x for x in c_sum.tok
                 if x[0] == infs[0].f_down[x[1]]
                 and x[2] == infs[1].f_down[x[1]]}

        return I.Invariant(c_sum, sigma, dual=True).quotient()
