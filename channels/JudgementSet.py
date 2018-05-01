import Sequent as S

class JudgementSet:

    def __init__(self, judgements=set()):
        self.judgements = judgements


    def __repr__(self):
        return repr(self.judgements)


    def __iter__(self):
        return self.judgements.__iter__


    def __hash__(self):
        individual_hashes = [hash(x) for x in self.judgements]
        return len(self.judgements) * sum(individual_hashes)


    def __eq__(self, other):

        return\
            self.judgements.issubset(other.judgements)\
            and other.judgements.issubset(self.judgements)


    def __neq__(self, other):

        return not (self == other)


    def entails(self, other):
        return S.Sequent(self, other)


    def add(self, item):
        self.judgements.add(item)
