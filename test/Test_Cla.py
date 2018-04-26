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


    def test_getTypes_returnsAllandOnlyTypesOfGivenToken(self):

        systemUnderTest = C.Cla()

        testToken = 'x'
        testTypeOne = 1
        testTypeTwo = 2

        systemUnderTest.addValidity(testToken, testTypeOne)
        systemUnderTest.addValidity(testToken, testTypeTwo)

        result = systemUnderTest.getTypes(testToken)

        self.assertTrue(testTypeOne in result)
        self.assertTrue(testTypeTwo in result)
        self.assertEqual(2, len(result))


    def test_getTokens_returnsAllAndOnlyTokensOfType(self):

        systemUnderTest = C.Cla()

        testType = 'x'
        testTokenOne = 1
        testTokenTwo = 2

        systemUnderTest.addValidity(testTokenOne, testType)
        systemUnderTest.addValidity(testTokenTwo, testType)

        result = systemUnderTest.getTokens(testType)

        self.assertTrue(testTokenOne in result)
        self.assertTrue(testTokenTwo in result)
        self.assertEqual(2, len(result))

        pass

    def test_addValidity_independentOfImplementationTypes(self):

        systemUnderTest = C.Cla()

        testToken = FooClass(1)
        testType = BarClass(2)

        systemUnderTest.addValidity(testToken, testType)

        result = systemUnderTest.isValid(testToken, testType)

        self.assertEqual(self.valid, result)



class EquableTestClass:

    def __init__(self, primitiveValuedId):
        self.id = primitiveValuedId

    def __hash__(self):
        return self.id


    def __eq__(self, other):

        try:
            return self.id == other.id

        except AttributeError:
            return False


    def __neq__(self, other):
        return not self.eq(other)

class FooClass(EquableTestClass):
    pass

class BarClass(EquableTestClass):
    pass


if __name__ == '__main__':
    unittest.main()
