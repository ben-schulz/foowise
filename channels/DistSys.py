
class DistSys:

    def __init__(self, infs):

        self.infs = infs

        clas = [i.proximal for i in infs] + [i.distal for i in infs]

        self.clas = {i.index:i for i in clas}
