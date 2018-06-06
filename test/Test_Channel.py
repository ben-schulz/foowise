import unittest

from test_context import Cla as C
from test_context import Infomorphism as I

from test_context import Channel as Ch

class Test_Channel(unittest.TestCase):

    def test_colimit(self):

        c0 = C.Cla({
            'x':{1,2,3},
            'y':{1,3},
            'z':{1,2}
        })

        c1 = C.Cla({
            'a':{5,10},
            'b':{5,20},
            'c':{10,20}
        })

        c2 = C.Cla({
            'p':{3,15,12,30},
            'q':{12},
            'r':{15,30},
            's':{6,12,21},
            't':{3,30}
            })

        up_dict_0 = {1:5, 2:10, 3:20}
        down_dict_0 = {'a':'x', 'b':'y', 'c':'z'}

        f_up_0 = lambda x: up_dict_0.get(x)
        f_down_0 = lambda x: down_dict_0.get(x)

        inf_0 = I.Infomorphism(c0, c1, f_up_0, f_down_0)

        up_dict_1 = {3:5, 15:5, 6:10, 12:20, 21:20, 30:10}
        down_dict_1 = {'a':'t', 'b':'r', 'c':'s'}

        f_up_1 = lambda x: up_dict_1.get(x)
        f_down_1 = lambda x: down_dict_1.get(x)        
        inf_1 = I.Infomorphism(c2, c1, f_up_1, f_down_1)

        core = Ch.Channel.colimit([c0,c1,c2], [inf_0, inf_1])

        self.assertNotEqual(None, core)

        self.assertTrue(all(
            map(lambda x: x[0] == f_down_0(x[1])
                and x[2] == f_down_1(x[1]),
            core.tok)
        ))


if __name__ == '__main__':
    unittest.main()
