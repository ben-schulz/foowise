import Validity as V

class Cla:

    def Empty():
        return Cla()

    def __init__(self, validities=None, tok=None, typ=None):

        if tok:
            self.tok = tok
        else:
            self.tok = set()

        if typ:
            self.typ = typ            
        else:
            self.typ = set()

        self.validities = {}
        if validities:
            vs = self.unpackValidities(validities)
            for v in vs:
                (x, t) = v
                self.addValidity(x, t)

        self.valid = V.HasType.VALID
        self.invalid = V.HasType.INVALID


    def unpackValidities(self, vs):

        unpacked_vs = []
        for v in vs:

            try:
                (x, t) = v
                unpacked_vs.append(v)

            except ValueError:
                v_typ = vs[v]
                for t in v_typ:
                    unpacked_vs.append((v, t))

        return unpacked_vs


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
