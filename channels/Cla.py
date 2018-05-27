import InfoPair as I
import LinAlg as m

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

        self.validities = {}
        if validities:

            vs = validities
            for (x,t) in vs:

                self.tok.add(x)
                self.typ.add(t)
                self.add_validity(x, t)

        typ_count = len(self.typ)
        typ_to_col = list(zip(self.typ, range(0, typ_count)))

        tok_count = len(self.tok)
        tok_to_row  = list(zip(self.tok, range(0, tok_count)))

        self.typ_to_col = dict(typ_to_col)
        col_to_typ = map(lambda p: (p[1], p[0]), typ_to_col)
        self.col_to_typ = dict(col_to_typ)

        self.tok_to_row = dict(tok_to_row)
        row_to_tok = map(lambda p: (p[1], p[0]), tok_to_row)
        self.row_to_tok = dict(row_to_tok)

        def validity_to_int(tok, typ):
            if self.is_valid(tok,typ):
                return 1
            else:
                return 0


        rows = [[validity_to_int(tok,typ) \
                for typ in self.typ] \
                for tok in self.tok]

        if not rows:
            self.mat = m.Matrix([])

        else:
            self.mat = m.Matrix(rows)

        self.table = self.to_table()




    def from_dictionary(vals):

        if not isinstance(vals, dict):

            given_type = vals.__class__
            msg = "expected arg type 'dict' but got " \
                  + "'" + repr(given_type) + "'."
            raise TypeError(msg)

        validities = [(x,t) for x in vals.keys() for t in vals[x]]
        return Cla(validities=validities)


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


    def to_table(self):

        typ_count = len(self.typ)
        typ_to_col = list(zip(self.typ, range(0, typ_count)))

        tok_count = len(self.tok)
        tok_to_row = list(zip(self.tok, range(0, tok_count)))

        def validity_to_int(tok, typ):
            if self.is_valid(tok,typ):
                return 1
            else:
                return 0

        rows = [[validity_to_int(tok,typ) \
                for typ in self.typ] \
                for tok in self.tok]

        return m.Matrix(rows)



    def is_consequent(self, gamma, delta):

        seq = m.Matrix([
            self.to_vector(gamma),
            self.to_vector(delta)
        ])

        cases = m.Matrix.dot(self.table, seq.transpose())

        not_all_gammas = cases.column(0) < len(gamma)
        at_least_one_delta = cases.column(1) > 0

        return \
            not_all_gammas\
            .logical_or(at_least_one_delta)\
            .all()


    def to_vector(self, judges):

        v = m.Matrix.zeros(len(self.typ_to_col))

        for x in judges:
            ix = self.typ_to_col[x]
            v[ix] = 1

        return v
