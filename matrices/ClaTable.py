import numpy as np

class ClaTable:

    def __init__(self, rows=list(), typ_to_col=None):

        if not typ_to_col:
            self.typ_to_col = {}
        else:
            self.typ_to_col = dict(typ_to_col)

        col_to_typ = map(lambda p: (p[1], p[0]), typ_to_col)
        self.col_to_typ = dict(col_to_typ)


    def from_classification(cla):
        
        typ_count = len(cla.typ)
        typ_to_col = list(zip(cla.typ, range(0, typ_count)))
        
        return ClaTable(typ_to_col=typ_to_col)
