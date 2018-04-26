import Validity as V

class Cla:

    def Empty():
        return Cla()

    def __init__(self, tok=None, typ=None):

        if not tok:
            tok = set()

        if not typ:
            typ = set()

        self.tok = tok
        self.typ = typ

        self.validities = {}

        self.valid = V.HasType.VALID
        self.invalid = V.HasType.INVALID


    def isValid(self, someToken, someType):

        typeSet = self.getTypes(someToken)

        if someType not in typeSet:
            return self.invalid

        else:
            return self.valid


    def addToken(self, newToken):
        self.tok.add(newToken)


    def addType(self, newType):
        self.typ.add(newType)


    def getTypes(self, someToken):

        if someToken in self.validities:
            return self.validities[someToken]

        return set()


    def getTokens(self, someType):

        tokens = []
        for t in self.validities.keys():
            if self.valid == self.isValid(t, someType):
                tokens.append(t)

        return tokens


    def addValidity(self, someToken, someType):

        self.tok.add(someToken)
        self.typ.add(someType)

        if someToken not in self.validities:
            self.validities[someToken] = set()

        self.validities[someToken].add(someType)
