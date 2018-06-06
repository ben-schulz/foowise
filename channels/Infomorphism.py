import Cla as C
import Validity as V
import InfomorphismError as IE
import InfoPair as I

class Infomorphism:

    def __init__(self, c_proximal, c_distal, f_up, f_down):

        self.proximal = c_proximal
        self.distal = c_distal

        self.f_down = {x:f_down(x) for x in self.distal.tok}
        self.f_up = {x:f_up(x) for x in self.proximal.typ}

        self.f_down_img = set(self.f_down.values())
        self.f_up_img = set(self.f_up.values())


        self.satisfiesInfoAxioms()


    def is_valid_distal(self, x, alpha):
        return self.distal.is_valid(x, alpha)


    def is_valid_proximal(self, x, alpha):
        return self.proximal.is_valid(x, alpha)


    def satisfiesInfoAxioms(self):
            
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

            x_validities = (self.proximal
                            .infopairs_by_token(x))

            f_down_x = self.f_down[x]

            f_x_validities = (self.distal
                              .infopairs_by_token(f_down_x))

            for distal_val in f_x_validities:

                t = distal_val.typ
                f_up_t = self.f_up[t]

                if not self.is_valid_proximal(x, f_up_t):

                    not_in_prox = I.InfoPair.invalid(x, f_up_t)
                    bad_pair = (not_in_prox, distal_val)

                    violations.append(bad_pair)

        if violations:

            raise IE.InfomorphismAxiomError(violations)

        return
