import Validity as V
import InfoPair as I

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

                self.tok.add(x)
                self.typ.add(t)
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


    def isValid(self, theToken, theType):

        typeSet = self.getTypes(theToken)

        if theType not in typeSet:
            return self.invalid

        else:
            return self.valid


    def infoPairsByToken(self, tok):

        pairs = set()
        for typ in self.validities[tok]:
            pairs.add(I.InfoPair.valid(tok, typ))

        return pairs


    def infoPairsByType(self, typ):

        pairs = set()
        for tok in self.tok:
            if typ in self.validities[tok]:
                pairs.add(I.InfoPair.valid(tok, typ))

        return pairs


    def addToken(self, newToken):
        self.tok.add(newToken)


    def addType(self, newType):
        self.typ.add(newType)


    def getTypes(self, theToken):

        if theToken in self.validities:
            return self.validities[theToken]

        return set()


    def getTokens(self, theType):

        tokens = []
        for t in self.validities.keys():
            if self.valid == self.isValid(t, theType):
                tokens.append(t)

        return tokens


    def addValidity(self, theToken, theType):

        self.tok.add(theToken)
        self.typ.add(theType)

        if theToken not in self.validities:
            self.validities[theToken] = set()

        self.validities[theToken].add(theType)
