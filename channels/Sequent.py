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


    def __eq__(self, other):
        return self.antecedent == other.antecedent\
            and self.consequent == other.consequent


    def __neq__(self, other):
        return not (self == other)
