from . import Sequent as S
from ..math import LinAlg as m

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


        seq = m.Matrix([
            self.to_vector(gamma),
            self.to_vector(delta)
        ])

        cases = m.Matrix.dot(self.table.matrix, seq.transpose())

        not_all_gammas = cases.column(0) < len(gamma)
        at_least_one_delta = cases.column(1) > 0

        return \
            not_all_gammas\
            .logical_or(at_least_one_delta)\
            .all()

    
    def to_vector(self, judges):

        v = m.Matrix.zeros(len(self.table.typ_to_col))

        for x in judges:
            ix = self.table.typ_to_col[x]
            v[ix] = 1

        return v


    def from_classification(cla):

        return Theory(alphabet=cla.typ, cla=cla)
