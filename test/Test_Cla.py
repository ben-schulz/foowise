import unittest

from test_context import Cla as C
from test_context import Validity as V


class Test_Cla(unittest.TestCase):

    valid = V.HasType.VALID
    invalid = V.HasType.INVALID


    def assertValid(self, c, tok, typ):
        result = c.isValid(tok, typ)
        message = 'Expected ' + str(tok) + " |= " + str(typ)
        self.assertEqual(self.valid, result, message)


    def assertNotValid(self, c, tok, typ):
        result = c.isValid(tok, typ)
        message = 'Expected ' + str(tok) + " !|= " + str(typ)
        self.assertEqual(self.invalid, result, message)


    def test_isValid_returnsInvalidIfTokenDoesNotHaveType(self):
        c = C.Cla()

        result = c.isValid('x', None)

        self.assertNotValid(c, 'x', None)


    def test_addToken_addsNewTokenToTokenSet(self):
        c = C.Cla()

        c.addToken('t')

        self.assertTrue('t' in c.tok)


    def test_addType_addsNewTypeToTypeSet(self):
        c = C.Cla()

        c.addType('t')

        self.assertTrue('t' in c.typ)


    def test_addValidity_causes_isValidToReturnTrue(self):

        c = C.Cla()

        c.addValidity('x', 'alpha')

        result = c.isValid('x', 'alpha')

        self.assertValid(c, 'x', 'alpha')


    def test_getTypes_returnsAllandOnlyTypesOfGivenToken(self):

        c = C.Cla()

        testToken = 'x'
        testTypeOne = 1
        testTypeTwo = 2

        c.addValidity(testToken, testTypeOne)
        c.addValidity(testToken, testTypeTwo)

        result = c.getTypes(testToken)

        self.assertTrue(testTypeOne in result)
        self.assertTrue(testTypeTwo in result)
        self.assertEqual(2, len(result))


    def test_getTokens_returnsAllAndOnlyTokensOfType(self):

        c = C.Cla()

        testType = 'x'
        testTokenOne = 1
        testTokenTwo = 2

        c.addValidity(testTokenOne, testType)
        c.addValidity(testTokenTwo, testType)

        result = c.getTokens(testType)

        self.assertTrue(testTokenOne in result)
        self.assertTrue(testTokenTwo in result)
        self.assertEqual(2, len(result))


    def test_addValidity_independentOfImplementationTypes(self):

        c = C.Cla()

        testToken = FooClass(1)
        testType = BarClass(2)

        c.addValidity(testToken, testType)

        result = c.isValid(testToken, testType)

        self.assertEqual(self.valid, result)


    def test_Empty_hasNoTokensNoTypesAndNoValidities(self):

        c = C.Cla.Empty()

        self.assertEqual(0, len(c.tok))
        self.assertEqual(0, len(c.typ))
        self.assertEqual(self.invalid, c.isValid(None, None))


    def test_constructor_populatesValiditiesGivenSet(self):

        vals = {
            ('x', 'alpha'),
            ('x', 'beta'),
            ('y', 'beta'),
            ('z', 'gamma')
        }

        c = C.Cla(validities=vals)

        self.assertValid(c, 'x', 'alpha')
        self.assertValid(c, 'x', 'beta')
        self.assertValid(c, 'y', 'beta')
        self.assertValid(c, 'z', 'gamma')

    def test_constructor_populatesValiditiesGivenSet(self):

        vals = {
            ('x', 'alpha'),
            ('x', 'beta'),
            ('y', 'beta'),
            ('z', 'gamma')
        }

        c = C.Cla(validities=vals)

        self.assertValid(c, 'x', 'alpha')
        self.assertValid(c, 'x', 'beta')
        self.assertValid(c, 'y', 'beta')
        self.assertValid(c, 'z', 'gamma')

    def test_constructor_populatesValiditiesGivenSet(self):

        vals = {
            ('x', 'alpha'),
            ('x', 'beta'),
            ('y', 'beta'),
            ('z', 'gamma')
        }

        c = C.Cla(validities=vals)

        self.assertValid(c, 'x', 'alpha')
        self.assertValid(c, 'x', 'beta')
        self.assertValid(c, 'y', 'beta')
        self.assertValid(c, 'z', 'gamma')


    def test_constructor_populatesValiditiesGivenDict(self):

        vals = {
            'x': {'alpha', 'beta'},
            'y': {'beta'},
            'z': {'gamma'},
            'q': set()
        }

        c = C.Cla(validities=vals)

        self.assertValid(c, 'x', 'alpha')
        self.assertValid(c, 'x', 'beta')
        self.assertValid(c, 'y', 'beta')
        self.assertValid(c, 'z', 'gamma')



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
