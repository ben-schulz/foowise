import Sequent as S

class Theory:

    def __init__(self, \
                 cla=None,
                 table=None, alphabet=set(), constraints=set()):

        self.alphabet = alphabet
        self.constraints = constraints

        self.cla = cla
        if cla:
            self.table = self.cla.table


    def isconsequent(self, gamma, delta):

        if gamma.entails(delta) in self.constraints:
            return True

        return self.cla.is_consequent(gamma, delta)


    def from_classification(cla):

        return Theory(alphabet=cla.typ, cla=cla)
