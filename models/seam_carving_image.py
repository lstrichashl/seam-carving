from models.Iterator.HorizontalIterator import HorizontalIterator
from models.Iterator.VerticalIterator import VerticalIterator


class SeamCarvingImage:
    def __init__(self, image_pixel_array):
        self.horizontal_iterator = HorizontalIterator(image_pixel_array[len(image_pixel_array) - 1][0])
        self.vertical_iterator = VerticalIterator(image_pixel_array[0][len(image_pixel_array[0]) - 1])
