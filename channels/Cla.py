import functools as f
import InfoPair as I
import LinAlg as m

class Cla:

    class ClaTable:

        def __init__(self, validities):

            if not isinstance(validities, dict):
                msg = "Cla.ClaTable() expected 'dict' but got " \
                      "type: " + repr(validities.__class__) + "."
                raise TypeError(msg)

            tok = validities.keys()
            typ = f.reduce(lambda x,y: x.union(y), \
                           validities.values(), set())

            typ_count = len(typ)
            typ_to_col = list(zip(typ, range(0, typ_count)))

            self.typ_to_col = dict(typ_to_col)
            col_to_typ = map(lambda p: (p[1], p[0]), typ_to_col)
            self.col_to_typ = dict(col_to_typ)

            tok_count = len(tok)
            tok_to_row = list(zip(tok, range(0, tok_count)))

            self.tok_to_row = dict(tok_to_row)
            row_to_tok = map(lambda p: (p[1], p[0]), tok_to_row)
            self.row_to_tok = dict(row_to_tok)

            self.matrix = m.Matrix(\
                        [[1 \
                          if x in validities \
                          and alpha in validities[x] \
                          else 0 \

                          for alpha in typ] \
                        for x in tok])


            self.next_tok_key = len(self.tok_to_row)
            self.next_typ_key = len(self.typ_to_col)
            

        def __getitem__(self, key):

            (tok, typ) = key

            tok_ix = self.tok_to_row[tok]
            typ_ix = self.typ_to_col[typ]

            return self.matrix[tok,typ]


        def __setitem__(self, key, value):

            (tok, typ) = key

            tok_ix = self.tok_to_row[tok]
            typ_ix = self.typ_to_col[typ]

            self.matrix[tok_ix][typ_ix] = value
            

        def add_column(self, typ, vals=None):

            self.typ_to_col[typ] = self.next_typ_key
            self.col_to_typ[self.next_typ_key] = typ

            self.next_typ_key += 1

            self.matrix.add_column(vals)


        def add_row(self, tok, vals=None):

            self.tok_to_row[tok] = self.next_tok_key
            self.row_to_tok[self.next_tok_key] = tok

            self.next_tok_key += 1
            
            self.matrix.add_row(vals)
            

        def is_valid(self, tok, typ):

            return 1 == self[(tok,typ)]


        def set_valid(self, tok, typ):

            self[(tok,typ)] = 1


        def set_invalid(self, tok, typ):

            self[(tok,typ)] = 0



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
            for (x,t) in validities:

                self.typ.add(t)

                if not x:
                    continue

                self.tok.add(x)

                if not x in self.validities:
                    self.validities[x] = set()

                self.validities[x].add(t)


        self.table = Cla.ClaTable(self.validities)


    def from_dictionary(vals):

        if not isinstance(vals, dict):

            given_type = vals.__class__
            msg = "expected arg type 'dict' but got " \
                  + "'" + repr(given_type) + "'."
            raise TypeError(msg)

        validities = [(x,t) for x in vals.keys() for t in vals[x]]

        return Cla(validities=validities)


    def is_valid(self, tok, typ):

        return tok in self.validities \
            and typ in self.validities[tok]


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


    def add_token(self, tok):

        if tok not in self.tok:
            self.table.add_row(tok)
            self.tok.add(tok)


    def add_type(self, typ):

        if typ not in self.typ:            
            self.table.add_column(typ)
            self.typ.add(typ)


    def get_types(self, theToken):

        if theToken in self.validities:
            return self.validities[theToken]

        return set()


    def get_tokens(self, typ):

        tokens = []
        for t in self.validities.keys():
            if self.is_valid(t, typ):
                tokens.append(t)

        return tokens


    def add_validity(self, tok, typ):

        self.add_token(tok)
        self.add_type(typ)

        if tok not in self.validities:
            self.validities[tok] = set()

        self.validities[tok].add(typ)


    def is_consequent(self, gamma, delta):

        seq = m.Matrix([
            self.to_vector(gamma),
            self.to_vector(delta)
        ])

        cases = m.Matrix.dot(self.table.matrix, seq.transpose())

        not_all_gammas = cases.column(0) < len(gamma)
        at_least_one_delta = cases.column(1) > 0

        return \
            not_all_gammas\
            .logical_or(at_least_one_delta)\
            .all()


    def to_vector(self, judges):

        v = m.Matrix.zeros(len(self.table.typ_to_col))

        for x in judges:
            ix = self.table.typ_to_col[x]
            v[ix] = 1

        return v


    def empty():
        return Cla()
