import numpy


class Energy:

    def __init__(self, value=0, neighbors=numpy.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])):
        self.value = value
        self.neighbors = neighbors
