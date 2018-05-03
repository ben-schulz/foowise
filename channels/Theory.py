import Sequent as S

class Theory:

    def __init__(self, alphabet=set(), constraints=set()):

        self.alphabet = alphabet
        self.constraints = constraints


    def isconsequent(self, gamma, delta):
        return S.Sequent(gamma, delta) in self.constraints


    def fromClassification(cla):

        return Theory(alphabet=cla.typ)
