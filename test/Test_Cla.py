import unittest

import Assert as A

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


    def test_is_valid_invalid_if_token_does_not_have_type(self):

        c = C.Cla({})

        self.assertNotValid(c, 'x', None)


    def test_add_token_adds_to_token_set(self):

        c = C.Cla({
            'x':set()
        })

        self.assertTrue('x' in c.tok)


    def test_add_type_addsNewTypeToTypeSet(self):

        c = C.Cla({
            None:{'t'}
        })

        self.assertTrue('t' in c.typ)


    def test_get_types_returns_all_and_only_types_of_x(self):

        c = C.Cla({
            'x':{1,2,4}
            })

        result = c.get_types('x')

        self.assertTrue(1 in result)
        self.assertTrue(2 in result)
        self.assertTrue(4 in result)
        self.assertEqual(3, len(result))


    def test_get_types_restricts_to_subset_if_given(self):

        c = C.Cla({
            'x':{1,2,4,5,6,7,8}
            })

        result = c.get_types('x', subset={5,7,103,22})

        self.assertEqual(2, len(result))
        self.assertTrue({5,7}.issubset(result))


    def test_types_agree_returns_true_if_x_and_y_match(self):

        c = C.Cla({
            'x':{2,3,5},
            'y':{2,3,5},
            'z':{2,5},
            'z':{2,3},
            'q':{2,3,5,7}
            })
        
        sigma = {2,3,5}
        self.assertTrue(c.types_agree('x', 'y', sigma))
        

    def test_get_tokens_returns_all_and_only_tokens_of_type(self):

        c = C.Cla({
            'x':{1,2,4},
            'y':{1,3,5},
            'z':{9}
            })

        result = c.get_tokens(1)

        self.assertTrue('x' in result)
        self.assertTrue('y' in result)
        self.assertFalse('z' in result)
        self.assertEqual(2, len(result))


    def test_tokens_agree_returns_true_if_x_and_y_match(self):

        c = C.Cla({
            'x':{2,3,5},
            'y':{2,3,5},
            'z':{2,5},
            'u':{2,3},
            'q':{3,5,7}
            })
        
        sigma = {'x', 'y', 'z'}
        self.assertTrue(c.tokens_agree(2, 5, sigma))


    def test_tokens_agree_returns_false_if_diff_token_exists(self):

        c = C.Cla({
            'x':{2,3,5},
            'y':{2,3,5},
            'z':{2,5},
            'u':{2,3},
            'q':{3,5,7}
            })
        
        sigma = {'x', 'y', 'z', 'u'}
        self.assertFalse(c.tokens_agree(2, 5, sigma))


    def test_validity_works_independent_of_types(self):

        testToken = FooClass(1)
        testType = BarClass(2)

        c = C.Cla({
            testToken:{testType}
            })

        self.assertTrue(c.is_valid(testToken, testType))


    def test_Empty_hasNoTokensNoTypesAndNoValidities(self):

        c = C.Cla.empty()

        self.assertEqual(0, len(c.tok))
        self.assertEqual(0, len(c.typ))
        self.assertFalse(c.is_valid(None, None))


    def test_constructor_populatesValiditiesGivenSet(self):

        vals = {
            'x':{'alpha','beta'},
            'y':{'beta'},
            'z':{'gamma'}
        }

        c = C.Cla(vals)

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
            'x':{'alpha','beta'},
            'y':{'beta'},
            'z':{'gamma'}
            }

        c = C.Cla(vals)

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

        c = C.Cla(vals)

        self.assertValid(c, 'x', 'alpha')
        self.assertValid(c, 'x', 'beta')
        self.assertValid(c, 'y', 'beta')
        self.assertValid(c, 'z', 'gamma')


    def test_infoPairsByToken_ReturnsEachValidType(self):

        vals = {
            'x':{'alpha', 'beta'},
            'y':{'beta'},
            'z':{'gamma'}
            }

        c = C.Cla(vals)

        result = c.infopairs_by_token('x')

        expectAlpha = I.InfoPair.valid('x', 'alpha')
        expectBeta = I.InfoPair.valid('x', 'beta')

        self.assertEqual(2, len(result))
        self.assertTrue(expectAlpha in result)
        self.assertTrue(expectBeta in result)


    def test_infoPairsByType_ReturnsEachValidToken(self):

        vals = {
            'x':{'alpha', 'beta'},
            'y':{'beta'},
            'z':{'gamma'}
            }

        c = C.Cla(vals)

        result = c.infopairs_by_type('beta')

        expect_x = I.InfoPair.valid('x', 'beta')
        expect_y = I.InfoPair.valid('y', 'beta')

        self.assertEqual(2, len(result))
        self.assertTrue(expect_x in result)
        self.assertTrue(expect_y in result)


    def test_from_dictionary_raises_typeerror_on_bad_type(self):

        vals = [('x', 'alpha'), ('y', 'beta')]

        try:
            result = C.Cla(vals)
        except TypeError:
            pass


    def test_from_dictionary_keys_tokens_to_types(self):

        vals = {
            'x': {'alpha', 'beta'},
            'y': {'beta', 'gamma'},
            'z': {'gamma'}
            }

        result = C.Cla(vals)

        for tok in vals.keys():

            msg = 'result missing token: ' + repr(tok)
            self.assertTrue(tok in result.tok, msg=msg)

            for typ in vals[tok]:
                msg = 'expected ' + repr(tok) + ' has type ' \
                      + repr(typ)
                self.assertTrue(result.is_valid(tok, typ), msg=msg)


    def test_from_dictionary_handles_token_None(self):
        vals = {
            None:{'omega'},
            'x': {'alpha', 'beta'},
            'y': {'beta', 'gamma'},
            'z': {'gamma'}
            }

        result = C.Cla(vals)

        self.assertFalse(None in result.tok)
        self.assertTrue('omega' in result.typ)

        for tok in result.tok:
            self.assertNotValid(result, tok, 'omega')

    def test_sum_includes_all_tokens_and_all_types(self):

        c_left = C.Cla({
            'x': {1,2,3},
            'y': {2,5},
            'z': {1}
            })

        c_right = C.Cla({
            'a': {'alpha', 'beta', 'gamma'},
            'b': {'beta'},
            'c': {'gamma'}
            })

        result = C.Cla.sum(c_left, c_right)

        self.assertTrue(isinstance(result, C.Cla))

        expect_tok = {(x,y) for x in c_left.tok \
                      for y in c_right.tok}

        expect_typ = {(0,t) for t in c_left.typ} \
                     .union({(1,t) for t in c_right.typ})

        mismatched_tok_msg = "Result tokens do not match expected."\
                             "\nExpected: " + repr(expect_tok) \
                             + "\nActual: " + repr(result.tok)

        self.assertEqual(expect_tok, result.tok, \
                         msg=mismatched_tok_msg)

        mismatched_typ_msg = "Result types do not matched expected."
        self.assertEqual(expect_typ, result.typ, \
                         msg=mismatched_typ_msg)


    def test_sum_produces_correct_validities(self):

        c_left = C.Cla({
            'x': {1,2,3},
            'y': {2,5},
            'z': {1}
            })

        c_right = C.Cla({
            'a': {'alpha', 'beta', 'gamma'},
            'b': {'beta'},
            'c': {'gamma'}
            })

        result = C.Cla.sum(c_left, c_right)

        for (x,y) in result.tok:

            for(i, t) in result.typ:

                valid_result = result.is_valid((x,y), (i,t))
                if 0 == i:
                    valid_part = c_left.is_valid(x, t)
                    msg = "c_left.is_valid" \
                          + repr((x,t)) + " = " + repr(valid_part)

                elif 1 == i:
                    valid_part = c_right.is_valid(y, t)
                    msg = "c_right.is_valid" \
                          + repr((x,t)) + " = " + repr(valid_part)

                else:
                    msg = "Unexpected type index: " + repr(i)
                    raise ValueError(msg)

                msg += " but sum.is_valid" + repr(((x,y),(i,t))) \
                       + " = " + repr(valid_result)

                self.assertEqual(valid_part, valid_result, msg=msg)


    def test_sum_returns_empty_on_no_args(self):

        result = C.Cla.sum()

        self.assertTrue(isinstance(result, C.Cla))
        self.assertEqual(0, len(result.tok))
        self.assertEqual(0, len(result.typ))
        self.assertEqual(0, len(result.validities))

    
    def test_sum_returns_infomorphic_on_single_input(self):

        c_left = C.Cla({
            'x': {1,2,3},
            'y': {2,5},
            'z': {1}
            })

        result = C.Cla.sum(c_left)

        for x in result.tok:

            for(i, t) in result.typ:

                self.assertEqual(0, i)
                valid_result = result.is_valid(x, (i,t))

                valid_part = c_left.is_valid(x[0], t)
                msg = "c_left.is_valid" \
                      + repr((x,t)) + " = " + repr(valid_part)

                msg += " but sum.is_valid" + repr((x,(i,t))) \
                       + " = " + repr(valid_result)

                self.assertEqual(valid_part, valid_result, msg=msg)


    def test_tok_typ_are_duals(self):

        c = C.Cla({
            'x' : {1,2,3,4,5,6,7,8},
            'y' : {2,4,8,12},
            'z' : {3,6,9,12}
            })

        A.Assert.sets_equal(c.tok, c.co.typ)
        A.Assert.sets_equal(c.typ, c.co.tok)

        A.Assert.sets_equal(c.get_types('x'), c.co.get_tokens('x'))
        A.Assert.sets_equal(c.get_tokens(2), c.co.get_types(2))


    def test_agree_funcs_are_dual(self):

        c = C.Cla({
            'x':{2,3,5},
            'y':{2,3,5},
            'z':{2,5},
            'u':{2,3},
            'q':{3,5,7}
            })
        
        sigma_typ = {2, 5}
        sigma_tok = {'x', 'y', 'z'}

        self.assertTrue(c.types_agree('x', 'y', sigma_typ),
                        c.co.tokens_agree('x', 'y', sigma_typ))

        self.assertTrue(c.tokens_agree(2, 5, sigma_tok),
                        c.co.types_agree(2, 5, sigma_tok))
        
        

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
