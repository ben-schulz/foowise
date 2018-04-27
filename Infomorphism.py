import Cla as C
import Validity as V
import InfomorphismConstraintError as IE

class Infomorphism:

    def __init__(self, c_Proximal, c_Distal, f_Up, f_Down):

        self.valid = V.HasType.VALID
        self.invalid = V.HasType.INVALID

        self.proximal = c_Proximal
        self.distal = c_Distal

        self.f_Up = Infomorphism.calculate_function_image(f_Up, self.proximal.tok)

        self.f_Down = Infomorphism.calculate_function_image(f_Down, self.distal.typ)

        self.f_Up_img = set(self.f_Up.values())

        self.f_Down_img = set(self.f_Down.values())

        if not self.satisfiesInfoAxioms():
            raise IE.InfomorphismConstraintError


    def is_valid_distal(self, x, alpha):
        return self.valid == self.distal.isValid(x, alpha)


    def is_valid_proximal(self, x, alpha):
        return self.valid == self.proximal.isValid(x, alpha)

    
    def calculate_function_image(f, dom):

        img = {}
        for x in dom:
            img[x] = f(x)

        return img


    def satisfiesInfoAxioms(self):

        if not self.f_Up_img.issubset(self.distal.tok):
            return False

        if not self.f_Down_img.issubset(self.proximal.typ):
            return False

        invalidProximalTypes = {}
        for x in self.proximal.tok:

            x_types = self.proximal.getTypes(x)

            f_x = self.f_Up[x]
            f_x_types = self.distal.getTypes(f_x)

            invalidProximalTypes[x] = set()
            for t in f_x_types:

                f_Down_t = self.f_Down[t]
                if not self.is_valid_proximal(x, f_Down_t):

                    invalidProximalTypes[x].add(f_Down_t)

        for x in invalidProximalTypes.keys():
            if 0 < len(invalidProximalTypes[x]):
                return False

        return True
