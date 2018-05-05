import unittest

from test_context import Cla as C
from test_context import ClaTable as CT

class ClaTable_Test(unittest.TestCase):

    def test_fromCla_producesTable(self):
        c_vals = {
            'x' : {'alpha', 'beta', 'gamma'},
            'y' : {'alpha', 'beta', 'zeta'},
            'z' : {'beta', 'gamma', 'zeta'},
            'q' : {'alpha', 'gamma', 'zeta'}
            }

        c = C.Cla(c_vals)
        ct = CT.ClaTable.from_classification(c)

        self.assertNotEqual(None, ct)

        

if __name__ == '__main__':
    unittest.main()

