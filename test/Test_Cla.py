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


    def test_add_token_addsNewTokenToTokenSet(self):
        c = C.Cla()

        c.add_token('t')

        self.assertTrue('t' in c.tok)


    def test_add_type_addsNewTypeToTypeSet(self):
        c = C.Cla()

        c.add_type('t')

        self.assertTrue('t' in c.typ)


    def test_add_validity_causes_is_validToReturnTrue(self):

        c = C.Cla()

        c.add_validity('x', 'alpha')

        result = c.is_valid('x', 'alpha')

        self.assertValid(c, 'x', 'alpha')


    def test_get_types_returnsAllandOnlyTypesOfGivenToken(self):

        c = C.Cla()

        testToken = 'x'
        testTypeOne = 1
        testTypeTwo = 2

        c.add_validity(testToken, testTypeOne)
        c.add_validity(testToken, testTypeTwo)

        result = c.get_types(testToken)

        self.assertTrue(testTypeOne in result)
        self.assertTrue(testTypeTwo in result)
        self.assertEqual(2, len(result))


    def test_getTokens_returnsAllAndOnlyTokensOfType(self):

        c = C.Cla()

        testType = 'x'
        testTokenOne = 1
        testTokenTwo = 2

        c.add_validity(testTokenOne, testType)
        c.add_validity(testTokenTwo, testType)

        result = c.get_tokens(testType)

        self.assertTrue(testTokenOne in result)
        self.assertTrue(testTokenTwo in result)
        self.assertEqual(2, len(result))


    def test_add_validity_independentOfImplementationTypes(self):

        c = C.Cla()

        testToken = FooClass(1)
        testType = BarClass(2)

        c.add_validity(testToken, testType)

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

        result = c.infopairs_by_token('x')

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

        result = c.infopairs_by_type('beta')

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
