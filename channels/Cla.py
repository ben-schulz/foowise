import functools as f
import Set as S
import InfoPair as I
import LinAlg as Alg

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

            self.matrix = Alg.Matrix(\
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


    def sum(*cla):

        if 0 == len(cla):
            return Cla.empty()

        tok = S.Set.product(*map(lambda c: c.tok, cla))

        vals = {x:set() for x in tok}

        for v in vals.keys():
            
            ix_typs = [{(i,t) for t in cla[i].get_types(v[i])} \
                       for i in range(0,len(cla))]

            vals[v] = S.Set.union(*ix_typs)

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


    def get_types(self, tok, subset=None):

        if not tok in self.validities:
            return set()

        if not subset:
            return self.validities[tok]

        return {t for t in self.validities[tok] if t in subset}


    def agree_all(self, x, y, sigma):

        if not x in self.tok:
            raise ValueError(str(x) + "is not a token.")

        if not y in self.tok:
            raise ValueError(str(y) + "is not a token.")

        typ_x = self.get_types(x, subset=sigma)
        typ_y = self.get_types(y, subset=sigma)

        return S.Set.are_equal(typ_x, typ_y)


    def get_tokens(self, typ):

        return {x for x in self.validities.keys() \
                if self.is_valid(x, typ)}


    def empty():
        return Cla({})
