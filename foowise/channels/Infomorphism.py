import uuid as u

from . import Cla as C
from . import InfomorphismError as IE
from . import Index as Id

from ..math import Dual as D

@D.dualizable(duals=[
    ('proximal', 'distal'),
    ('f_up', 'f_down')
])
class Infomorphism:

    class InfoPair:

        def __init__(self, x, t, holds):

            self.tok = x
            self.typ = t
            self.holds = holds


        def __eq__(self, other):

            try:
                return (
                    self.tok == other.tok
                    and self.typ == other.typ
                    and self.holds == other.holds)

            except:
                return False


        def __neq__(self, other):
            return not self.__eq__(other)


        def __str__(self):

            if self.holds:
                infix_op = ' |= '
            elif self.holds:
                infix_op = ' |\= '

            return ('< '
                + repr(self.tok) + infix_op  + repr(self.typ)
                + ' >')


        def valid(x, t):        
            return Infomorphism.InfoPair(x, t, True)


        def invalid(x, t):
            return Infomorphism.InfoPair(x, t, False)


    def __init__(self,
                 proximal,
                 distal,
                 f_up,
                 f_down,
                 validate=True):

        self.proximal = proximal
        self.distal = distal

        self.f_down = {x:f_down(x) for x in self.distal.tok}
        self.f_up = {x:f_up(x) for x in self.proximal.typ}

        self.f_down_img = set(self.f_down.values())
        self.f_up_img = set(self.f_up.values())

        if validate:
            self.satisfies_info_axioms()

        self.index = Id.Index()


    def satisfies_info_axioms(self):
            
        if not self.f_down_img.issubset(self.proximal.tok):
            f_name = "f_down"
            r_name = "the proximal classification's token set"

            raise IE.MorphismRangeError(f_name=f_name,
                                        r_name=r_name,
                                        img=self.f_down_img,
                                        target=self.proximal.tok)

        if not self.f_up_img.issubset(self.distal.typ):
            f_name = "f_up"
            r_name = "the distal classification's type set"
            raise IE.MorphismRangeError(f_name=f_name,
                                        r_name=r_name,
                                        img=self.f_up_img,
                                        target=self.distal.typ)

        def failure_case(f_down_x, t, x, f_up_t):
            
            if self.proximal.is_valid(f_down_x, t):
                prox = Infomorphism.InfoPair.valid(f_down_x, t)
            else:
                prox = Infomorphism.InfoPair.invalid(f_down_x, t)

            if self.distal.is_valid(x, f_up_t):
                dist = Infomorphism.InfoPair.valid(x, f_up_t)
            else:
                dist = Infomorphism.InfoPair.invalid(x, f_up_t)

            return (prox, dist)


        violations = []

        toks = [(x, self.f_down[x]) for x in self.distal.tok]
        typs = [(self.f_up[t], t) for t in self.proximal.typ]

        for (x, f_down_x) in toks:
            for (f_up_t, t) in typs:

                if (self.proximal.is_valid(f_down_x, t)
                    != self.distal.is_valid(x, f_up_t)):

                    violations.append(
                        failure_case(f_down_x, t, x, f_up_t))

        if violations:

            raise IE.InfomorphismAxiomError(violations)

        return


    def canon_quot(cla, inv):

        f_up = lambda typ: typ
        f_down = lambda x: inv.canon_rep(x)

        quot = inv.quotient()

        if inv.isdual:
            return Infomorphism(cla, quot, f_down, f_up)

        return Infomorphism(quot, cla, f_up, f_down)
