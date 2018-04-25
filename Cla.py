import Validity as V

class Cla:

    def __init__(self):
        self.tok = []
        self.typ = []

        self.valid = V.HasType.VALID
        self.invalid = V.HasType.INVALID

    def isValid(self):
    	return self.invalid
