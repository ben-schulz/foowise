import inspect

def dualizable(duals=[]):

    def _dualizable(cls):

        class Dual(object):

            class _Trans(object):

                def __init__(self, instance, dual_map):
                    self.instance = instance
                    self.dual_map = dual_map


                def __getattr__(self, name):

                    _name = self.dual_map.get(name, name)
                    return getattr(self.instance, _name)

                    
            def __init__(self, *args, **kwargs):

                self.instance = cls(*args, **kwargs)

                dual_map = dict(duals
                                + [(d[1], d[0]) for d in duals])

                self.trans = Dual._Trans(self.instance, dual_map)


            def __getattr__(self, name):

                if 'dual' == name:
                    return self.trans

                return getattr(self.instance, name)


        _vars = vars(cls)
        for v in _vars.keys():
            x = getattr(cls, v)

            if inspect.isclass(x):
                setattr(Dual, v, _vars[v])

            elif inspect.ismethod(x):
                setattr(Dual, v, _vars[v])

            elif inspect.isfunction(x) and not '__' == v[0:2]:
                setattr(Dual, v, _vars[v])


        return Dual

    return _dualizable
