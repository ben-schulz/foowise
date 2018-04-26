import Validity as V

class Cla:

    def __init__(self):

        self.tok = set()
        self.typ = set()

        self.validities = {}

        self.valid = V.HasType.VALID
        self.invalid = V.HasType.INVALID


    def isValid(self, someToken, someType):

        typeSet = self.getTypes(someToken)

        if someType not in typeSet:
            return self.invalid

        else:
            return self.valid


    def addToken(self, newToken):
        self.tok.add(newToken)


    def addType(self, newType):
        self.typ.add(newType)


    def getTypes(self, someToken):

        if someToken in self.validities:
            return self.validities[someToken]

        return set()


    def addValidity(self, someToken, someType):

        self.tok.add(someToken)
        self.typ.add(someType)

        if someToken not in self.validities:
            self.validities[someToken] = set()

        self.validities[someToken].add(someType)
