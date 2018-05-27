import LinAlg as m

class ClaTable:

    def __init__(self, rows=None, tok_to_row=None, typ_to_col=None):

        if not typ_to_col:
            self.typ_to_col = {}
            self.col_to_typ = {}

        else:
            self.typ_to_col = dict(typ_to_col)
            col_to_typ = map(lambda p: (p[1], p[0]), typ_to_col)
            self.col_to_typ = dict(col_to_typ)

        if not tok_to_row:
            self.tok_to_row = {}
            self.row_to_tok = {}
        else:
            self.tok_to_row = dict(tok_to_row)
            row_to_tok = map(lambda p: (p[1], p[0]), tok_to_row)
            self.row_to_tok = dict(row_to_tok)

        if not rows:
            self.mat = m.Matrix([])
        else:
            self.mat = m.Matrix(rows)


    def is_consequent(self, gamma, delta):

        seq = m.Matrix([
            self.to_vector(gamma),
            self.to_vector(delta)
        ])

        cases = m.Matrix.dot(self.mat, seq.transpose())

        not_all_gammas = cases.column(0) < len(gamma)
        at_least_one_delta = cases.column(1) > 0

        return not_all_gammas.logical_or(at_least_one_delta).all()


    def to_vector(self, judges):

        v = m.Matrix.zeros(len(self.typ_to_col))

        for x in judges:
            ix = self.typ_to_col[x]
            v[ix] = 1

        return v


    def from_classification(cla):
        
        typ_count = len(cla.typ)
        typ_to_col = list(zip(cla.typ, range(0, typ_count)))

        tok_count = len(cla.tok)
        tok_to_row = list(zip(cla.tok, range(0, tok_count)))

        def validity_to_int(tok, typ):
            if cla.is_valid(tok,typ):
                return 1
            else:
                return 0

        rows = [[validity_to_int(tok,typ) \
                for typ in cla.typ] \
                for tok in cla.tok]

        return ClaTable(\
                    rows=rows,\
                    tok_to_row=tok_to_row,\
                    typ_to_col=typ_to_col)
