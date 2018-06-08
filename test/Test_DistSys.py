import unittest

from test_context import Cla as C
from test_context import Infomorphism as I
from test_context import DistSys as D

class Test_DistSys(unittest.TestCase):

    def test_distinguishes_classifications_in_infomorphisms(self):

        i = 0
        j = 1
        k = 2

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

        self.assertTrue(c1.index in d.clas)
        self.assertTrue(c2.index in d.clas)
        self.assertTrue(c3.index in d.clas)


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
        self.assertTrue(c.index in d.clas)


if __name__ == '__main__':
    unittest.main()
