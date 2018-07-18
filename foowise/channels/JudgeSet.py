from . import Sequent as S

class JudgeSet:

    def __init__(self, judgements=set()):
        self.judgements = judgements


    def __len__(self):
        return len(self.judgements)


    def __repr__(self):
        return repr(self.judgements)


    def __iter__(self):
        for x in self.judgements:
            yield x


    def __hash__(self):
        individual_hashes = [hash(x) for x in self.judgements]
        return len(self.judgements) * sum(individual_hashes)


    def try_comparison(action):
        try:
            return action()

        except AttributeError:
            raise NotImplementedError


    def __eq__(self, other):

        return\
            self.judgements.issubset(other.judgements)\
            and other.judgements.issubset(self.judgements)


    def __neq__(self, other):
        return not (self == other)

    def __lt__(self, other):

        len_self = len(self.judgements)
        len_other = len(other.judgements)
        
        lt = lambda:\
             len_self < len_other and\
             self.judgements.issubset(other.judgements)

        return JudgeSet.try_comparison(lt)

    def __gt__(self, other):

        len_self = len(self.judgements)
        len_other = len(other.judgements)

        gt = lambda:\
             len_self > len_other and\
             other.judgements.issubset(self.judgements)

        return JudgeSet.try_comparison(gt)


    def __le__(self, other):

        if(self < other):
            return True

        return self == other

    
    def __ge__(self, other):
        return False


    def entails(self, other):
        return S.Sequent(self, other)


    def add(self, item):
        self.judgements.add(item)
