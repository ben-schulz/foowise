import unittest

from test_context import Dual as D

class Test_Dual(unittest.TestCase):

    @D.dualizable(duals=[
        ('a', 'b'),
        ('call_a', 'call_b')])
    class Example:

        class Foo:
            pass

        def __init__(self, a, b, non_dual='non_dual'):
            self.a = a
            self.b = b
            self.foo = Test_Dual.Example.Foo()
            self.non_dual = non_dual


        def call_a(self):
            return 'call_a'


        def call_b(self):
            return 'call_b'


        def call_non_dual(self, x):
            return 'call_' + x

        def call_non_instance_non_dual(x):

            return 'non_instance_' + x


    def test_dual_respects_existing_members(self):

        example = Test_Dual.Example('a', 'b')

        self.assertEqual('a', example.a)
        self.assertEqual('b', example.b)


    def test_dual_respects_existing_methods(self):

        example = Test_Dual.Example('a', 'b')

        self.assertEqual('call_a', example.call_a())
        self.assertEqual('call_b', example.call_b())


    def test_dual_switches_methods_on_dual_call(self):

        example = Test_Dual.Example('a', 'b')

        self.assertEqual('call_b', example.co.call_a())
        self.assertEqual('call_a', example.co.call_b())


    def test_dual_switches_members_on_dual_reference(self):

        example = Test_Dual.Example('a', 'b')

        self.assertEqual('b', example.co.a)
        self.assertEqual('a', example.co.b)


    def test_dual_does_not_persist_state_after_co(self):

        example = Test_Dual.Example('a', 'b')

        dual = example.co

        self.assertEqual('b', dual.a)
        self.assertEqual('a', example.a)


    def test_dual_retains_duality_after_assignment(self):

        example = Test_Dual.Example('a', 'b')

        dual = example.co

        self.assertEqual('b', dual.a)
        self.assertEqual('a', dual.b)


    def test_dual_allows_internal_classes(self):

        example = Test_Dual.Example('a', 'b')

        self.assertNotEqual(None, example.foo)


    def test_dual_preserves_nondual_members(self):

        example = Test_Dual.Example('a', 'b', 'non_dual_x')

        self.assertEqual('call_x', example.call_non_dual('x'))

        self.assertEqual('non_dual_x', example.non_dual)

        non_instance_result = (Test_Dual.Example.
                               call_non_instance_non_dual('x'))

        self.assertEqual('non_instance_x', non_instance_result)


if __name__ == '__main__':
    unittest.main()
