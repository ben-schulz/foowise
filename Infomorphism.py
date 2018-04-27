import Cla as C
import Validity as V
import InfomorphismConstraintError as IE

class Infomorphism:

    def __init__(self, c_Proximal, c_Distal, f_Up, f_Down):

        self.proximal = c_Proximal
        self.distal = c_Distal

        self.f_Up = f_Up
        self.f_Down = f_Down

        if not self.satisfiesInfoAxioms():
            raise IE.InfomorphismConstraintError

    def satisfiesInfoAxioms(self):

        token_image = set()
        for tok in self.proximal.tok:
            token_image.add(self.f_Up(tok))

        if not token_image.issubset(self.distal.tok):
            return False

        type_image = set()
        for typ in self.distal.typ:
            type_image.add(self.f_Down(typ))

        if not type_image.issubset(self.proximal.typ):
            return False

        return True
