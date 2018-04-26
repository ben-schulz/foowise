import unittest

from test_context import Cla as C
from test_context import Validity as V


class Test_Cla(unittest.TestCase):

    valid = V.HasType.VALID
    invalid = V.HasType.INVALID


    def test_isValid_returnsInvalidIfTokenDoesNotHaveType(self):
        systemUnderTest = C.Cla()

        result = systemUnderTest.isValid('x', None)

        self.assertEqual(self.invalid, result)


    def test_addToken_addsNewTokenToTokenSet(self):
        systemUnderTest = C.Cla()

        systemUnderTest.addToken('t')

        self.assertTrue('t' in systemUnderTest.tok)


    def test_addType_addsNewTypeToTypeSet(self):
        systemUnderTest = C.Cla()

        systemUnderTest.addType('t')

        self.assertTrue('t' in systemUnderTest.typ)


    def test_addValidity_causes_isValidToReturnTrue(self):

        systemUnderTest = C.Cla()

        systemUnderTest.addValidity('x', 'alpha')

        result = systemUnderTest.isValid('x', 'alpha')

        self.assertEqual(self.valid, result)


if __name__ == '__main__':
    unittest.main()
