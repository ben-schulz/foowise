import InfoPair as I

class Cla:

    def empty():
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

        def unpack_validities(vs):

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


        self.validities = {}
        if validities:
            vs = unpack_validities(validities)
            for v in vs:

                (x, t) = v

                self.tok.add(x)
                self.typ.add(t)
                self.add_validity(x, t)




    def is_valid(self, tok, typ):
        return typ in self.get_types(tok)


    def infopairs_by_token(self, tok):

        pairs = set()

        if tok not in self.validities:
            return pairs

        for typ in self.validities[tok]:
            pairs.add(I.InfoPair.valid(tok, typ))

        return pairs


    def infopairs_by_type(self, typ):

        pairs = set()
        for tok in self.tok:
            if typ in self.validities[tok]:
                pairs.add(I.InfoPair.valid(tok, typ))

        return pairs


    def add_token(self, newToken):
        self.tok.add(newToken)


    def add_type(self, newType):
        self.typ.add(newType)


    def get_types(self, theToken):

        if theToken in self.validities:
            return self.validities[theToken]

        return set()


    def get_tokens(self, theType):

        tokens = []
        for t in self.validities.keys():
            if self.is_valid(t, theType):
                tokens.append(t)

        return tokens


    def add_validity(self, theToken, theType):

        self.tok.add(theToken)
        self.typ.add(theType)

        if theToken not in self.validities:
            self.validities[theToken] = set()

        self.validities[theToken].add(theType)
