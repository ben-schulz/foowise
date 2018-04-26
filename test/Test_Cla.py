import unittest

from test_context import Cla
from test_context import Validity as V


class Cla_Test(unittest.TestCase):

    valid = V.HasType.VALID
    invalid = V.HasType.INVALID

    def test_isValid_returnsInvalidIfTokenDoesNotHaveType(self):
        systemUnderTest = Cla.Cla()

        self.assertEqual(self.invalid, systemUnderTest.isValid())

if __name__ == '__main__':
    unittest.main()
