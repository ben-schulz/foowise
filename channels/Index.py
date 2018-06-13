import uuid as u

class Index:

    def __init__(self, int_value=None):

        self.uuid = u.uuid1()

        if not int_value:
            self.int = self.uuid.int
        else:
            self.int = int_value


    def from_int(int_value):

        if not isinstance(int_value, int):
            msg = "Expected an instance of 'int'."
            raise TypeError(msg)

        return Index(int_value)
        

    def __eq__(self, other):

        if isinstance(other, int):
            return self.int == other

        try:
            self.uuid == other.uuid
        except:
            return False


    def __neq__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return self.int
