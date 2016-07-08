import numpy
from models.image_pixel import ImagePixel


class SeamCarvingImage:
    def __init__(self, image):
        self.array = [[ImagePixel(image[row_index][column_index])
                      for column_index, pixel in enumerate(row)]
                      for row_index, row in enumerate(image)]

        for row_index, row in enumerate(self.array):
            for column_index, pixel in enumerate(row):
                pixel.energy.neighbors = self.calc_neighbors(row_index, column_index)

    def get_neighbors(self, row_index, column_index):
        return self.array[row_index][column_index].energy.neighbors

    def calc_neighbors(self, row_index, column_index):
        neighbors = numpy.array([[-1, -1, -1],
                                 [-1, -1, -1],
                                 [-1, -1, -1]])
        if row_index > 0:
            if column_index > 0:
                neighbors[0][0] = self.array[row_index - 1][column_index - 1]
            if column_index < len(self.array[0]):
                neighbors[0][2] = self.array[row_index - 1][column_index + 1]
            neighbors[0][1] = self.array[row_index - 1][column_index]
        if row_index < len(self.array):
            if column_index > 0:
                neighbors[2][0] = self.array[row_index + 1][column_index - 1]
            if column_index < len(self.array[0]):
                neighbors[2][2] = self.array[row_index + 1][column_index + 1]
            neighbors[2][1] = self.array[row_index + 1][column_index]
        if column_index > 0:
            neighbors[1][0] = self.array[row_index][column_index - 1]
        if column_index < len(self.array[0]):
            neighbors[1][2] = self.array[row_index][column_index + 1]
        return neighbors




