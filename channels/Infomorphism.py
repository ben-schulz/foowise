import Cla as C
import Validity as V
import InfomorphismConstraintError as IE
import InfoPair as I

class Infomorphism:

    def __init__(self, c_Proximal, c_Distal, f_Up, f_Down):

        self.proximal = c_Proximal
        self.distal = c_Distal

        self.f_Up = Infomorphism.calculate_function_image(f_Up, self.proximal.tok)

        self.f_Down = Infomorphism.calculate_function_image(f_Down, self.distal.typ)

        self.f_Up_img = set(self.f_Up.values())
        self.f_Down_img = set(self.f_Down.values())

        try:
            self.satisfiesInfoAxioms()

        except Exception as e:
            raise e


    def is_valid_distal(self, x, alpha):
        return self.distal.is_valid(x, alpha)


    def is_valid_proximal(self, x, alpha):
        return self.proximal.is_valid(x, alpha)

    
    def calculate_function_image(f, dom):

        img = {}
        for x in dom:
            img[x] = f(x)

        return img


    def satisfiesInfoAxioms(self):

        if not self.f_Up_img.issubset(self.distal.tok):
            raise IE.InfomorphismConstraintError(IE.InfomorphismErrorReason.BAD_RANGE_F_UP)

        if not self.f_Down_img.issubset(self.proximal.typ):
            raise IE.InfomorphismConstraintError(IE.InfomorphismErrorReason.BAD_RANGE_F_DOWN)

        infoConstraintViolations = []
        for x in self.proximal.tok:

            x_validities = self.proximal.infopairs_by_token(x)

            f_Up_x = self.f_Up[x]
            f_x_validities = self.distal.infopairs_by_token(f_Up_x)

            for inDistal in f_x_validities:

                t = inDistal.typ
                f_Down_t = self.f_Down[t]
                if not self.is_valid_proximal(x, f_Down_t):

                    notInProximal = I.InfoPair.invalid(x, f_Down_t)
                    badInfoPair = (notInProximal, inDistal)

                    infoConstraintViolations.append(badInfoPair)

        violationCount = len(infoConstraintViolations)
        if 0 < violationCount:

            violationListCount = min(5, violationCount)

            raise IE.InfomorphismConstraintError(IE.InfomorphismErrorReason.INFO_AXIOM_VIOLATED, infoConstraintViolations)

        return
