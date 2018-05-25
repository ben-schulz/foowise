import Cla as C
import Validity as V
import InfomorphismConstraintError as IE
import InfoPair as I

class Infomorphism:

    def __init__(self, c_Proximal, c_Distal, f_down, f_up):

        self.proximal = c_Proximal
        self.distal = c_Distal

        self.f_down = {x:f_down(x) for x in self.proximal.tok}
        self.f_up = {x:f_up(x) for x in self.distal.typ}

        self.f_down_img = set(self.f_down.values())
        self.f_up_img = set(self.f_up.values())

        try:
            self.satisfiesInfoAxioms()

        except Exception as e:
            raise e


    def is_valid_distal(self, x, alpha):
        return self.distal.is_valid(x, alpha)


    def is_valid_proximal(self, x, alpha):
        return self.proximal.is_valid(x, alpha)


    def satisfiesInfoAxioms(self):

        if not self.f_down_img.issubset(self.distal.tok):
            raise IE.InfomorphismConstraintError(IE.InfomorphismErrorReason.BAD_RANGE_F_UP)

        if not self.f_up_img.issubset(self.proximal.typ):
            raise IE.InfomorphismConstraintError(IE.InfomorphismErrorReason.BAD_RANGE_F_DOWN)

        infoConstraintViolations = []
        for x in self.proximal.tok:

            x_validities = self.proximal.infopairs_by_token(x)

            f_down_x = self.f_down[x]
            f_x_validities = self.distal.infopairs_by_token(f_down_x)

            for inDistal in f_x_validities:

                t = inDistal.typ
                f_up_t = self.f_up[t]
                if not self.is_valid_proximal(x, f_up_t):

                    notInProximal = I.InfoPair.invalid(x, f_up_t)
                    badInfoPair = (notInProximal, inDistal)

                    infoConstraintViolations.append(badInfoPair)

        violationCount = len(infoConstraintViolations)
        if 0 < violationCount:

            violationListCount = min(5, violationCount)

            raise IE.InfomorphismConstraintError(IE.InfomorphismErrorReason.INFO_AXIOM_VIOLATED, infoConstraintViolations)

        return
