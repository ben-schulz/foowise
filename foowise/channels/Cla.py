import functools as f

from foowise.channels import Index as Id
from foowise.channels import InfoPair as I

from foowise.math import Set as S
from foowise.math import LinAlg as Alg
from foowise.math import Dual as D

@D.dualizable(duals=[
    ('tok', 'typ'),
    ('get_tokens', 'get_types'),
    ('tokens_agree', 'types_agree'),
    ('is_valid', 'is_valid_dual'),
    ('is_invalid', 'is_invalid_dual')])
class Cla:

    class ClaTable:

        def __init__(self, validities):

            if not isinstance(validities, dict):
                msg = "Cla.ClaTable() expected 'dict' but got " \
                      "type: " + repr(validities.__class__) + "."
                raise TypeError(msg)

            tok = validities.keys()
            typ = f.reduce(lambda x,y: x.union(y),
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

            self.matrix = Alg.Matrix(
                        [[1
                          if x in validities
                          and alpha in validities[x]
                          else 0

                          for alpha in typ]
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


        def __str__(self):

            def _strlen(x):
                return len(str(x))

            toks = [x for x in self.tok_to_row.keys()]
            typs = [t for t in self.typ_to_col.keys()]

            max_col_width = max(map(lambda x: _strlen(x), typs))

            start_col_ix = max(map(lambda x: _strlen(x), toks))

            pad = 1 + max_col_width

            fmt = '\n' + ' ' * (start_col_ix + pad + 1)

            fmt += f.reduce(lambda acc,n:
                            acc + str(n)
                            + ' '*(pad - _strlen(n) + 1), typs, '')

            fmt += '\n\n'

            for x in toks:
                _str = str(x)
                fmt += _str + ' '*(start_col_ix - len(_str) + 4)

                for t in typs:
                    _str = str(self[(x,t)])
                    fmt += _str + ' '* (pad)
                fmt += '\n\n'

            return fmt


        def is_valid(self, tok, typ):

            return 1 == self[(tok,typ)]


        def is_invalid(self, tok, typ):

            return 0 == self[(tok,typ)]


        def row_values(self, tok):

            tok_ix = self.tok_to_row[tok]

            row = self.matrix[tok_ix, :]

            return { self.col_to_typ[ix] : row[0,ix]
                       for ix in self.col_to_typ.keys() }

        def col_values(self, typ):

            typ_ix = self.typ_to_col[typ]

            col = self.matrix[:, typ_ix]
            
            return { self.row_to_tok[ix] : col[ix,0]
                     for ix in self.row_to_tok.keys() }


    def __init__(self, validities, index=None):

        if not isinstance(validities, dict):

            given_type = validities.__class__
            msg = "expected arg type 'dict' but got " \
                  + "'" + repr(given_type) + "'."
            raise TypeError(msg)

        self.index = index

        self.tok = set()
        self.typ = set()

        for x in validities.keys():

            if x:
                self.tok.add(x)

            for t in validities[x]:
                self.typ.add(t)

        self.validities = validities
        self.table = Cla.ClaTable(self.validities)

        if not index:
            index = Id.Index()

        self.index = index

        if NotImplemented == index.__eq__(0):
            msg = "'index' must have an implementation of '__eq__'."
            raise ValueError(msg)


    def is_valid(self, tok, typ):
        return self.table.is_valid(tok, typ)


    def is_valid_dual(self, typ, tok):
        return self.table.is_valid(tok, typ)


    def is_invalid(self, tok, typ):
        return self.table.is_invalid(tok, typ)


    def is_invalid_dual(self, typ, tok):
        return self.table.is_invalid(tok, typ)


    def get_types(self, tok, subset=None):

        if not tok in self.tok:
            return set()

        row = self.table.row_values(tok)

        if not subset:
            return {t for t in row.keys()
                    if 1 == row[t] }

        return { t for t in row.keys()
                 if 1 == row[t] 
                 and t in subset }


    def types_agree(self, x, y, sigma):

        if not x in self.tok:
            raise ValueError(str(x) + " is not a token.")

        if not y in self.tok:
            raise ValueError(str(y) + " is not a token.")

        typ_x = self.get_types(x, subset=sigma)
        typ_y = self.get_types(y, subset=sigma)

        return S.Set.are_equal(typ_x, typ_y)


    def tokens_agree(self, alpha, beta, sigma):

        if not alpha in self.typ:
            raise ValueError(str(alpha) + " is not a type.")

        if not beta in self.typ:
            raise ValueError(str(beta) + " is not a type.")

        tok_x = self.get_tokens(alpha, subset=sigma)
        tok_y = self.get_tokens(beta, subset=sigma)

        return S.Set.are_equal(tok_x, tok_y)


    def get_tokens(self, typ, subset=None):

        if not typ in self.typ:
            return set()

        col = self.table.col_values(typ)

        if not subset:
            return { x for x in col.keys()
                     if 1 == col[x] }

        return { x for x in col.keys()
                 if 1 == col[x] and x in subset }
    

    def empty():
        return Cla({})


class Sum(Cla):

    def __init__(self, *cla):

        indexes = enumerate(map(lambda c: c.index, cla))

        self._ix_to_id = dict(indexes)
        self._id_to_ix = {self._ix_to_id[k]:k for k in
                          self._ix_to_id.keys()}

        tokens = map((lambda c: c.tok), cla)

        tok = S.Set.product(*tokens)

        vals = {x:set() for x in tok}

        for v in vals.keys():

            ix_typs = [
                {(cla[i].index, t)
                 for t in cla[i].get_types(v[i])}
                for i in range(0,len(cla))]

            vals[v] = S.Set.union(*ix_typs)

        Cla.__init__(self, vals)


    def index_of(self, ident):
        return self._id_to_ix.get(ident, None)


    def ident_at(self, index):
        return self._ix_to_id.get(index, None)
