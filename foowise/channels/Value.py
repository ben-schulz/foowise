Any = object()

class Value:

    def __init__(self, index, name):

        self.name = name
        self.index = index


    def __eq__(self, other):

        if not (hasattr(other, 'name')
                and hasattr(other, 'index')):

            return NotImplemented

        return (self.index == other.index
                and self.name == other.name)


    def __str__(self):

        index = str(self.index)
        name = str(self.name)

        return "(" + index + ", " + name + ")"
