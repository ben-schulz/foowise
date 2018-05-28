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

            if tok not in self.tok_to_row:
                return None

            if typ not in self.typ_to_col:
                return None

            tok_ix = self.tok_to_row[tok]
            typ_ix = self.typ_to_col[typ]

            return self.matrix[tok_ix,typ_ix]


        def __setitem__(self, key, value):

            (tok, typ) = key

            tok_ix = self.tok_to_row[tok]
            typ_ix = self.typ_to_col[typ]

            self.matrix[tok_ix][typ_ix] = value


        def is_valid(self, tok, typ):

            return 1 == self[(tok,typ)]


        def is_invalid(self, tok, typ):

            return 0 == self[(tok,typ)]


        def set_valid(self, tok, typ):

            self[(tok,typ)] = 1


        def set_invalid(self, tok, typ):

            self[(tok,typ)] = 0



    def __init__(self, validities):

        if not isinstance(validities, dict):

            given_type = validities.__class__
            msg = "expected arg type 'dict' but got " \
                  + "'" + repr(given_type) + "'."
            raise TypeError(msg)

        self.tok = set()
        self.typ = set()

        for x in validities.keys():

            if x:
                self.tok.add(x)

            for t in validities[x]:
                self.typ.add(t)

        self.validities = validities
        self.table = Cla.ClaTable(self.validities)


    def is_valid(self, tok, typ):
        return self.table.is_valid(tok, typ)


    def sum(c_left, c_right):

        tok = {(x,y) for x in c_left.tok for y in c_right.tok}
        vals = {x:set() for x in tok}

        for (x,y) in vals.keys():
            vals[(x,y)] = {(0,t) for t in c_left.get_types(x)} \
                      .union({(1,t) for t in c_right.get_types(y)})

        return Cla(vals)

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


    def get_types(self, tok):

        if tok in self.validities:
            return self.validities[tok]

        return set()


    def get_tokens(self, typ):

        return {x for x in self.validities.keys() \
                if self.is_valid(x, typ)}


    def empty():
        return Cla({})
