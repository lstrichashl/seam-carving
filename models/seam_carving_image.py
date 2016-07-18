import numpy
from models.image_pixel import ImagePixel


class SeamCarvingImage:
    def __init__(self, image):
        self.array = self.image_pixel_array(image)

        for row_index, row in enumerate(self.array):
            for column_index, pixel in enumerate(row):
                self.set_pixel_neighbors(column_index, pixel, row_index)
                if row_index == len(self.array) and column_index == 0:
                    self.horizontal_iterator = HorizontalIterator(pixel)
                if row_index == 0 and column_index == len(self.array):
                    self.vertical_iterator = VerticalIterator(pixel)

        for row in self.array:
            for pixel in row:
                pixel.gradient_horizontal.update()
                pixel.gradient_vertical.update()

    def set_pixel_neighbors(self, column_index, pixel, row_index):
        neighbors = self.get_neighbors(row_index, column_index)
        pixel.set_north(neighbors[0][1])
        pixel.set_east(neighbors[1][2])
        pixel.set_south(neighbors[2][1])
        pixel.set_west(neighbors[1][0])

    def image_pixel_array(self, image):
        return [[ImagePixel(value=image[row_index][column_index])
                 for column_index, pixel in enumerate(row)]
                for row_index, row in enumerate(image)]


    def get_neighbors(self, row_index, column_index):
        neighbors = numpy.array([[-1, -1, -1],
                                 [-1, -1, -1],
                                 [-1, -1, -1]])
        if row_index > 0:
            neighbors[0][1] = self.array[row_index - 1][column_index]
        if row_index < len(self.array):
            neighbors[2][1] = self.array[row_index + 1][column_index]
        if column_index > 0:
            neighbors[1][0] = self.array[row_index][column_index - 1]
        if column_index < len(self.array[0]):
            neighbors[1][2] = self.array[row_index][column_index + 1]
        return neighbors


class SeamCarvingIterator:
    def __init__(self, start_pixel):
        self.current_pixel = start_pixel

    def __iter__(self):
        return self


class VerticalIterator(SeamCarvingIterator):
    def next(self):
        self.current_pixel = self.current_pixel.south()
        return self.current_pixel


class HorizontalIterator(SeamCarvingIterator):
    def next(self):
        self.current_pixel = self.current_pixel.east()
        return self.current_pixel
