import unittest

import uuid as u

import Assert as A
from test_context import Cla as C
from test_context import InfoPair as I
from test_context import Index as Id

class Test_Cla(unittest.TestCase):

    def assertValid(self, c, tok, typ):

        message = str(tok) + " |= " + str(typ)

        self.assertTrue(c.is_valid(tok, typ),
                        'Expected ' + message)

        self.assertFalse(c.is_invalid(tok, typ),
                         'Expected NOT ' + message)


    def assertNotValid(self, c, tok, typ):

        message = str(tok) + " |!= " + str(typ)

        self.assertFalse(c.is_valid(tok, typ),
                         'Expected ' + message)

        self.assertTrue(c.is_invalid(tok, typ),
                        'Expected NOT ' + message)


    def test_is_valid_and_is_not_valid_false_for_NoneType(self):

        c = C.Cla({})

        self.assertFalse(c.is_valid('x', None))
        self.assertFalse(c.is_invalid('x', None))


    def test_is_invalid_returns_false_for_token_not_valid(self):

        c = C.Cla({
            'x':{1,6},
            'z': {6},
            'q': set()
        })

        self.assertTrue(c.is_invalid('z', 1))


    def test_add_token_adds_to_token_set(self):

        c = C.Cla({
            'x':set()
        })

        self.assertTrue('x' in c.tok)


    def test_add_type_adds_type_to_typ(self):

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
            }, index=1)

        c_right = C.Cla({
            'a': {'alpha', 'beta', 'gamma'},
            'b': {'beta'},
            'c': {'gamma'}
            }, index=2)

        result = C.Cla.sum(c_left, c_right)

        self.assertTrue(isinstance(result, C.Cla))

        expect_tok = {(x,y) for x in c_left.tok \
                      for y in c_right.tok}

        expect_typ = {(1,t) for t in c_left.typ} \
                     .union({(2,t) for t in c_right.typ})

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
            }, index=1)

        c_right = C.Cla({
            'a': {'alpha', 'beta', 'gamma'},
            'b': {'beta'},
            'c': {'gamma'}
            }, index=2)

        result = C.Cla.sum(c_left, c_right)

        for (x,y) in result.tok:

            for(i, t) in result.typ:

                valid_result = result.is_valid((x,y), (i,t))
                if 1 == i:
                    valid_part = c_left.is_valid(x, t)
                    msg = "c_left.is_valid" \
                          + repr((x,t)) + " = " + repr(valid_part)

                elif 2 == i:
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
            }, index=1)

        result = C.Cla.sum(c_left)

        for x in result.tok:

            for(i, t) in result.typ:

                self.assertEqual(1, i)
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

        A.Assert.sets_equal(c.tok, c.dual.typ)
        A.Assert.sets_equal(c.typ, c.dual.tok)

        A.Assert.sets_equal(c.get_types('x'),
                            c.dual.get_tokens('x'))

        A.Assert.sets_equal(c.get_tokens(2),
                            c.dual.get_types(2))


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
                        c.dual.tokens_agree('x', 'y', sigma_typ))

        self.assertTrue(c.tokens_agree(2, 5, sigma_tok),
                        c.dual.types_agree(2, 5, sigma_tok))


    def test_dual_reverses_validity_relation(self):

        c = C.Cla({
            'x':{1,2},
            'y':{1}
            })

        self.assertTrue(c.dual.is_valid(1, 'x'))
        self.assertTrue(c.dual.is_valid(2, 'x'))

        self.assertTrue(c.dual.is_valid(1, 'y'))
        self.assertTrue(c.dual.is_invalid(2, 'y'))


    def test_index_raises_valueerror_if_not_equable(self):

        class NonEquableTestClass:
            pass

        try:
            c = C.Cla({}, index=NonEquableTestClass())
            self.assertTrue(False, "Expected 'ValueError'.")

        except ValueError:
            pass


    def test_index_equal_to_random_index_if_not_specified(self):

        c = C.Cla({})
        self.assertTrue(isinstance(c.index, Id.Index))


    def test_index_equal_to_kwarg_if_specified_and_equable(self):

        c = C.Cla({}, index=255)

        self.assertEqual(c.index, 255)


    def test_sum_indexes_tokens_by_classification_index(self):

        c0 = C.Cla({'x':{0}}, index=256)
        c1 = C.Cla({'y':{-1}}, index=255)

        c_sum = C.Cla.sum(c0, c1)

        self.assertTrue(c0.is_valid('x', 0))
        self.assertTrue(c1.is_valid('y', -1))

        self.assertTrue(c_sum.is_valid(('x','y'), (c0.index, 0)))
        self.assertTrue(c_sum.is_valid(('x','y'), (c1.index, -1)))


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
