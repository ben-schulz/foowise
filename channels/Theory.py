import ClaTable as CT
import Sequent as S

class Theory:

    def __init__(self, \
                 table=None, alphabet=set(), constraints=set()):

        self.alphabet = alphabet
        self.constraints = constraints

        if table:
            self.table = table
        else:
            self.table = CT.ClaTable()


    def isconsequent(self, gamma, delta):

        return S.Sequent(gamma, delta) in self.constraints


    def fromClassification(cla):

        table = CT.ClaTable.from_classification(cla)

        return Theory(alphabet=cla.typ, table=table)
