import Validity as V

class InfoPair:

    def __init__(self, x, t, holds):

        self.tok = x
        self.typ = t
        self.holds = holds


    def __eq__(self, other):

        try:
            return\
                self.tok == other.tok and\
                self.typ == other.typ and\
                self.holds == other.holds
        
        except:
            return False


    def __neq__(self, other):
        return not self == other


    def __hash__(self):

        if V.HasType.VALID == self.holds:
            parity = 1
        else:
            parity = -1

        return parity * hash(self.tok) * hash(self.typ)


    def __repr__(self):
        
        if V.HasType.VALID == self.holds:
            infixOperator = ' |= '
        elif V.HasType.INVALID == self.holds:
            infixOperator = ' |\= '

        return '< ' +\
            repr(self.tok) + infixOperator  + repr(self.typ) +\
            ' >'


    def __str__(self):
        return repr(self)


    def valid(x, t):        
        return InfoPair(x, t, V.HasType.VALID)


    def invalid(x, t):
        return InfoPair(x, t, V.HasType.INVALID)


