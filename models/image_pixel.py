import numpy
from models.gradient import Gradient


class ImagePixel:

    def __init__(self, value=-1,
                 neighbors=numpy.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]),
                 gradient_horizontal=Gradient(),
                 gradient_vertical=Gradient()):
        self.value = value
        self.energy_value = -1
        self.neighbors = neighbors
        self.gradient_horizontal = gradient_horizontal
        self.gradient_vertical = gradient_vertical

    def north_west(self):
        return self.neighbors[0][0]

    def north(self):
        return self.neighbors[0][1]

    def north_east(self):
        return self.neighbors[0][2]

    def east(self):
        return self.neighbors[1][2]

    def south_east(self):
        return self.neighbors[2][2]

    def south(self):
        return self.neighbors[2][1]

    def south_west(self):
        return self.neighbors[2][0]

    def west(self):
        return self.neighbors[1][0]