import unittest

from test_context import Validity as V
from test_context import Cla as C

class ClaTable_Test(unittest.TestCase):

    def test_from_cla_maps_types_to_indices(self):

        c_types = set({'alpha', 'beta', 'gamma', 'zeta'})
        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        ct = C.Cla.from_dictionary(c_vals)

        table_types = ct.typ_to_col.keys()
        table_indices = ct.typ_to_col.values()

        types_present = map(lambda x: x in table_types, c_types)

        self.assertTrue(all(types_present))
        self.assertEqual(len(c_types), len(table_types))
        self.assertEqual(len(c_types), len(table_indices))


    def test_from_cla_populates_all_columns_in_order(self):

        c_types = set({'alpha', 'beta', 'gamma', 'zeta'})
        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        ct = C.Cla.from_dictionary(c_vals)

        table_indices_left = sorted(ct.col_to_typ.keys())
        table_indices_right = sorted(ct.typ_to_col.values())

        self.assertEqual(table_indices_left, table_indices_right)
        

    def test_from_cla_maps_indices_to_types(self):        

        c_types = set({'alpha', 'beta', 'gamma', 'zeta'})
        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        ct = C.Cla.from_dictionary(c_vals)

        table_types = ct.col_to_typ.values()
        table_indices = ct.col_to_typ.keys()
        
        types_present = map(lambda x: x in table_types, c_types)

        self.assertEqual(len(c_types), len(table_types))
        self.assertEqual(len(c_types), len(table_indices))

        self.assertTrue(all(types_present))


    def test_from_classification_maps_tokens_to_rows(self):

        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        c_tokens = c_vals.keys()

        ct = C.Cla.from_dictionary(c_vals)

        self.assertEqual(c_tokens, ct.tok_to_row.keys())


    def test_from_classification_maps_rows_to_tokens(self):

        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        c_tokens = set(c_vals.keys())

        ct = C.Cla.from_dictionary(c_vals)

        self.assertEqual(set(c_tokens), set(ct.row_to_tok.values()))


    def test_from_classification_produces_the_table_0(self):

        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        c = C.Cla.from_dictionary(c_vals)
        ct = c.table

        for tok in c_vals.keys():
            row_ix = c.tok_to_row[tok]
            for typ in c.typ:
                col_ix = c.typ_to_col[typ]
                if c.is_valid(tok, typ):                    
                    self.assertEqual(1, ct[row_ix, col_ix])
                else:
                    self.assertEqual(0, ct[row_ix, col_ix])


    def test_from_classification_produces_the_table_1(self):

        c_vals = {
            'x' : {'alpha'},
            'y' : {'beta'},
            'z' : { 'gamma'},
            }

        c = C.Cla.from_dictionary(c_vals)
        ct = c.table

        for tok in c_vals.keys():
            row_ix = c.tok_to_row[tok]
            for typ in c.typ:
                col_ix = c.typ_to_col[typ]
                if c.is_valid(tok, typ):                    
                    self.assertEqual(1, ct[row_ix, col_ix])
                else:
                    self.assertEqual(0, ct[row_ix, col_ix])


    def test_from_classification_produces_the_table_2(self):

        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'zeta'},
            }

        c = C.Cla.from_dictionary(c_vals)
        ct = c.table

        for tok in c_vals.keys():
            row_ix = c.tok_to_row[tok]
            for typ in c.typ:
                col_ix = c.typ_to_col[typ]
                if c.is_valid(tok, typ):                    
                    self.assertEqual(1, ct[row_ix, col_ix])
                else:
                    self.assertEqual(0, ct[row_ix, col_ix])


    def test_to_vector_maps_types_to_indices(self):

        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'zeta', 'theta', 'omega'},
            }

        c = C.Cla.from_dictionary(c_vals)
        ct = c.table

        judges = {'alpha', 'beta'}
        result = c.to_vector(judges)

        self.assertEqual(1, result[c.typ_to_col['alpha']])
        self.assertEqual(1, result[c.typ_to_col['beta']])

        others = [t for t in c.typ if t not in judges]
        other_ixs = [c.typ_to_col[t] for t in others]

        are_zero = [0 == result[i] for i in other_ixs]

        self.assertTrue(all(are_zero))


if __name__ == '__main__':
    unittest.main()

