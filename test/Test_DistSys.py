import unittest

from test_context import Cla as C
from test_context import Infomorphism as I
from test_context import DistSys as D

class Test_DistSys(unittest.TestCase):

    def test_distinguishes_classifications_in_infomorphisms(self):

        i = 1
        j = 2
        k = 3

        c1 = C.Cla({'x':{0}}, index=i)
        c2 = C.Cla({'y':{1}}, index=j)
        c3 = C.Cla({'z':{2}}, index=k)        

        f_up_1 = lambda _: 1
        f_down_1 = lambda _: 'x'
        inf_1_2 = I.Infomorphism(c1, c2, f_up_1, f_down_1)

        f_up_2 = lambda _: 2
        f_down_2 = lambda _: 'y'
        inf_2_3 = I.Infomorphism(c2, c3, f_up_2, f_down_2)

        infs = [inf_1_2, inf_2_3]
        d = D.DistSys(infs)

        self.assertEqual(3, len(d.clas))

        self.assertEqual(c1.index, d.get_cla(c1.index).index)
        self.assertEqual(c2.index, d.get_cla(c2.index).index)
        self.assertEqual(c3.index, d.get_cla(c3.index).index)


    def test_classifications_not_duplicated_when_shared(self):

        c = C.Cla({'x':{0}})

        f_up_1 = lambda x: x
        f_down_1 = lambda x: x
        inf_1_2 = I.Infomorphism(c, c, f_up_1, f_down_1)

        f_up_2 = lambda x: x
        f_down_2 = lambda x: x
        inf_2_3 = I.Infomorphism(c, c, f_up_2, f_down_2)

        infs = [inf_1_2, inf_2_3]
        d = D.DistSys(infs)

        self.assertEqual(1, len(d.clas))
        self.assertNotEqual(None, d.get_cla(c.index))


    def test_get_infomorphisms_returns_list_of_all(self):

        i = 1
        j = 2
        k = 3

        c1 = C.Cla({'x':{0}}, index=i)
        c2 = C.Cla({'y':{1}}, index=j)
        c3 = C.Cla({'z':{2}}, index=k)

        f_up_1 = lambda _: 1
        f_down_1 = lambda _: 'x'
        inf_1_2 = I.Infomorphism(c1, c2, f_up_1, f_down_1)

        inf_2_1 = inf_1_2.dual

        f_up_2 = lambda _: 2
        f_down_2 = lambda _: 'y'
        inf_2_3 = I.Infomorphism(c2, c3, f_up_2, f_down_2)

        infs = [inf_1_2, inf_2_1, inf_2_3]
        d = D.DistSys(infs)

        c1_to_c2 = d.get_infomorphisms(c1.index, c2.index)
        c2_to_c1 = d.get_infomorphisms(c2.index, c1.index)
        c2_to_c3 = d.get_infomorphisms(c2.index, c3.index)

        self.assertTrue(inf_1_2 in c1_to_c2)
        self.assertTrue(inf_2_1 in c2_to_c1)
        self.assertTrue(inf_2_3 in c2_to_c3)


if __name__ == '__main__':
    unittest.main()
