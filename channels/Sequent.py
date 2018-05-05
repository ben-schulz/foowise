class Sequent:

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent


    def __repr__(self):
        return repr(antecdent) + ' |- ' + repr(consequent)


    def __str__(self):
        return str(self)


    def __hash__(self):
        return hash(self.antecedent) * hash(self.consequent)


    def try_comparison(action):
        try:
            return action()
        except:
            raise NotImplemented


    def __eq__(self, other):
        return self.antecedent == other.antecedent\
            and self.consequent == other.consequent


    def __neq__(self, other):
        return not (self == other)


    def __lt__(self, other):

        def lt():
            return\
                self.antecedent < other.antecedent\
                and self.consequent < other.consequent

        return Sequent.try_comparison(lt)


    def __gt__(self, other):

        def gt():
            return self.antecedent > other.antecedent\
            and self.consequent > other.consequent

        return Sequent.try_comparison(gt)


    def __le__(self, other):

        if(self < other):
            return True

        return self == other


    def __ge__(self, other):

        if(self > other):
            return True

        return self == other

