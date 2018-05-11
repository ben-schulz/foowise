import Validity as V
import numpy as np

class ClaTable:

    def __init__(self, rows=None, tok_to_row=None, typ_to_col=None):

        if not typ_to_col:
            self.typ_to_col = {}
        else:
            self.typ_to_col = dict(typ_to_col)

        col_to_typ = map(lambda p: (p[1], p[0]), typ_to_col)
        self.col_to_typ = dict(col_to_typ)

        if not tok_to_row:
            self.tok_to_row = {}
        else:
            self.tok_to_row = dict(tok_to_row)

        row_to_tok = map(lambda p: (p[1], p[0]), tok_to_row)
        self.row_to_tok = dict(row_to_tok)

        if not rows:
            self.mat = np.matrix([])
        else:
            self.mat = np.matrix(rows)
            



    def from_classification(cla):
        
        typ_count = len(cla.typ)
        typ_to_col = list(zip(cla.typ, range(0, typ_count)))

        tok_count = len(cla.tok)
        tok_to_row = list(zip(cla.tok, range(0, tok_count)))

        rows = []
        for tok in cla.tok:
            row = []
            for typ in cla.typ:
                if V.HasType.VALID == cla.isValid(tok, typ):
                    row.append(1)
                else:
                    row.append(0)
            rows.append(row)

        return ClaTable(\
                    rows=rows,\
                    tok_to_row=tok_to_row,\
                    typ_to_col=typ_to_col)
