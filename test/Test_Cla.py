import unittest

from test_context import Cla as C
from test_context import InfoPair as I

class Test_Cla(unittest.TestCase):

    def assertValid(self, c, tok, typ):
        result = c.is_valid(tok, typ)
        message = 'Expected ' + str(tok) + " |= " + str(typ)
        self.assertTrue(result, message)


    def assertNotValid(self, c, tok, typ):
        result = c.is_valid(tok, typ)
        message = 'Expected ' + str(tok) + " !|= " + str(typ)
        self.assertFalse(result, message)


    def test_is_valid_returnsInvalidIfTokenDoesNotHaveType(self):
        c = C.Cla()

        self.assertNotValid(c, 'x', None)


    def test_addToken_addsNewTokenToTokenSet(self):
        c = C.Cla()

        c.addToken('t')

        self.assertTrue('t' in c.tok)


    def test_addType_addsNewTypeToTypeSet(self):
        c = C.Cla()

        c.addType('t')

        self.assertTrue('t' in c.typ)


    def test_addValidity_causes_is_validToReturnTrue(self):

        c = C.Cla()

        c.addValidity('x', 'alpha')

        result = c.is_valid('x', 'alpha')

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

        self.assertTrue(c.is_valid(testToken, testType))


    def test_Empty_hasNoTokensNoTypesAndNoValidities(self):

        c = C.Cla.Empty()

        self.assertEqual(0, len(c.tok))
        self.assertEqual(0, len(c.typ))
        self.assertFalse(c.is_valid(None, None))


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

    def test_infoPairsByToken_ReturnsEachValidType(self):

        vals = {
            ('y', 'beta'),
            ('x', 'alpha'),
            ('z', 'gamma'),
            ('x', 'beta'),
        }

        c = C.Cla(validities=vals)

        result = c.infoPairsByToken('x')

        expectAlpha = I.InfoPair.valid('x', 'alpha')
        expectBeta = I.InfoPair.valid('x', 'beta')

        self.assertEqual(2, len(result))
        self.assertTrue(expectAlpha in result)
        self.assertTrue(expectBeta in result)


    def test_infoPairsByType_ReturnsEachValidToken(self):

        vals = {
            ('y', 'beta'),
            ('x', 'alpha'),
            ('z', 'gamma'),
            ('x', 'beta'),
        }

        c = C.Cla(validities=vals)

        result = c.infoPairsByType('beta')

        expect_x = I.InfoPair.valid('x', 'beta')
        expect_y = I.InfoPair.valid('y', 'beta')

        self.assertEqual(2, len(result))
        self.assertTrue(expect_x in result)
        self.assertTrue(expect_y in result)


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
