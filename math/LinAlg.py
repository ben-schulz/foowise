import numpy as np

class Matrix:

    def __init__(self, m):
        self.matrix = np.matrix(m, copy=True)


    def __getitem__(self, key):
        return self.matrix.__getitem__(key)


    def __setitem__(self, key, value):
        self.matrix.__setitem__(key, value)


    def __lt__(self, other):

        if isinstance(other, Matrix):
            other_value = other.matrix
        else:
            other_value = other

        return Matrix(self.matrix < other_value)


    def __gt__(self, other):

        if isinstance(other, Matrix):
            other_value = other.matrix
        else:
            other_value = other

        return Matrix(self.matrix > other_value)


    def dot(self, other):
        return Matrix(np.dot(self.matrix, other.matrix))


    def transpose(self):
        return Matrix(self.matrix.transpose())


    def column(self, n):
        return Matrix(self.matrix[:,n])


    def row(self, n):
        return Matrix(self.matrix[n,:])


    def zeros(dims):
        return np.zeros(dims)


    def all(self):
        return Matrix(self.matrix.all())


    def logical_or(self, other):
        return Matrix(np.logical_or(self.matrix, other.matrix))
