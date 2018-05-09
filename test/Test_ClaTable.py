import unittest

from test_context import Cla as C
from test_context import ClaTable as CT

class ClaTable_Test(unittest.TestCase):

    def test_from_cla_maps_types_to_indices(self):

        c_types = set({'alpha', 'beta', 'gamma', 'zeta'})
        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        c = C.Cla(c_vals)
        ct = CT.ClaTable.from_classification(c)

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

        c = C.Cla(c_vals)
        ct = CT.ClaTable.from_classification(c)

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

        c = C.Cla(c_vals)
        ct = CT.ClaTable.from_classification(c)

        table_types = ct.col_to_typ.values()
        table_indices = ct.col_to_typ.keys()
        
        types_present = map(lambda x: x in table_types, c_types)

        self.assertEqual(len(c_types), len(table_types))
        self.assertEqual(len(c_types), len(table_indices))

        self.assertTrue(all(types_present))


if __name__ == '__main__':
    unittest.main()

