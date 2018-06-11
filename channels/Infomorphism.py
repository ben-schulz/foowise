import uuid as u

import Cla as C
import Validity as V
import InfomorphismError as IE
import Index as Id

class Infomorphism:

    class InfoPair:
        def __init__(self, x, t, holds):

            self.tok = x
            self.typ = t
            self.holds = holds


        def __eq__(self, other):

            try:
                return\
                    self.tok == other.tok and\
                    self.typ == other.typ and\
                    self.holds == other.holds

            except:
                return False


        def __neq__(self, other):
            return not self == other


        def __hash__(self):

            if V.HasType.VALID == self.holds:
                parity = 1
            else:
                parity = -1

            return parity * hash(self.tok) * hash(self.typ)


        def __repr__(self):

            if V.HasType.VALID == self.holds:
                infixOperator = ' |= '
            elif V.HasType.INVALID == self.holds:
                infixOperator = ' |\= '

            return '< ' +\
                repr(self.tok) + infixOperator  + repr(self.typ) +\
                ' >'
        

        def __str__(self):
            return repr(self)


        def valid(x, t):        
            return Infomorphism.InfoPair(x, t, V.HasType.VALID)


        def invalid(x, t):
            return Infomorphism.InfoPair(x, t, V.HasType.INVALID)


    def __init__(self, c_proximal, c_distal, f_up, f_down):

        self.proximal = c_proximal
        self.distal = c_distal

        self.f_down = {x:f_down(x) for x in self.distal.tok}
        self.f_up = {x:f_up(x) for x in self.proximal.typ}

        self.f_down_img = set(self.f_down.values())
        self.f_up_img = set(self.f_up.values())

        self.satisfies_info_axioms()

        self.index = Id.Index()


    def is_valid_distal(self, x, alpha):
        return self.distal.is_valid(x, alpha)


    def is_valid_proximal(self, x, alpha):
        return self.proximal.is_valid(x, alpha)


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

        violations = []
        for x in self.distal.tok:

            x_validities = self.proximal.get_types(x)

            f_down_x = self.f_down[x]

            f_x_validities = self.distal.get_types(f_down_x)

            for t in f_x_validities:

                if t in self.f_up:
                    f_up_t = self.f_up[t]

                    if not self.is_valid_proximal(x, f_up_t):

                        not_in_prox = Infomorphism.InfoPair.invalid(x, f_up_t)
                        bad_pair = (not_in_prox,
                                    Infomorphism.InfoPair.valid(f_down_x, t))

                        violations.append(bad_pair)

        if violations:

            raise IE.InfomorphismAxiomError(violations)

        return


    def canon_quot(cla, inv):

        f_up = lambda typ: typ
        f_down = lambda x: inv.canon_rep(x)

        quot = inv.quotient()

        return Infomorphism(quot, cla, f_up, f_down)
