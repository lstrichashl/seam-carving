import numpy
from models.Iterator.HorizontalIterator import HorizontalIterator
from models.Iterator.VerticalIterator import VerticalIterator
from models.image_pixel import ImagePixel
from models.seam_carving_image import SeamCarvingImage


def main(regular_image):
    image = regular_image_to_seam_carving_image(regular_image)


def regular_image_to_seam_carving_image(regular_image):
    image_pixel_array = regular_image_to_image_pixel_array(regular_image)
    set_image_neighbors(image_pixel_array)
    set_image_gradients(image_pixel_array)
    return SeamCarvingImage(image_pixel_array)


def set_image_gradients(image_pixel_array):
    for row in image_pixel_array:
        for pixel in row:
            pixel.gradient_horizontal.update()
            pixel.gradient_vertical.update()


def set_image_neighbors(image_pixel_array):
    for row_index, row in enumerate(image_pixel_array):
        for column_index, pixel in enumerate(row):
            set_pixel_neighbors(pixel, column_index, row_index)


def set_pixel_neighbors(self, pixel, column_index, row_index):
    neighbors = self.get_neighbors(row_index, column_index)
    pixel.set_north(neighbors[0][1])
    pixel.set_east(neighbors[1][2])
    pixel.set_south(neighbors[2][1])
    pixel.set_west(neighbors[1][0])


def regular_image_to_image_pixel_array(self, image):
    return [[ImagePixel(value=image[row_index][column_index])
             for column_index, pixel in enumerate(row)]
            for row_index, row in enumerate(image)]


def get_neighbors(self, row_index, column_index):
    neighbors = numpy.array([[None, None, None],
                             [None, None, None],
                             [None, None, None]])
    if row_index > 0:
        neighbors[0][1] = self.array[row_index - 1][column_index]
    if row_index < len(self.array):
        neighbors[2][1] = self.array[row_index + 1][column_index]
    if column_index > 0:
        neighbors[1][0] = self.array[row_index][column_index - 1]
    if column_index < len(self.array[0]):
        neighbors[1][2] = self.array[row_index][column_index + 1]
    return neighbors
