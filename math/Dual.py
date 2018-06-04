
def dualizable(duals=[]):

    def _dualizable(cls):

        class Dual(object):

            class _Trans(object):

                def __init__(self, instance, dual_map):
                    self.instance = instance
                    self.dual_map = dual_map


                def __getattr__(self, name):

                    return getattr(self.instance,
                                   self.dual_map[name])

                    
            def __init__(self, *args, **kwargs):

                self.instance = cls(*args, **kwargs)

                dual_map = dict(duals +
                                     [(d[1], d[0]) for d in duals])

                self.trans = Dual._Trans(self.instance, dual_map)


            def __getattr__(self, name):

                if 'co' == name:
                    return self.trans

                return getattr(self.instance, name)


        return Dual

    return _dualizable
