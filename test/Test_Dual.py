import unittest

from test_context import Dual as D

class Test_Dual(unittest.TestCase):

    @D.dualizable(duals=[
        ('a', 'b'),
        ('call_a', 'call_b')])
    class Example:

        def __init__(self, a, b):
            self.a = a
            self.b = b


        def call_a(self):
            return 'call_a'


        def call_b(self):
            return 'call_b'


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


if __name__ == '__main__':
    unittest.main()
