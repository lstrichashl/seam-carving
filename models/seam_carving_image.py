from models.Iterator.HorizontalIterator import HorizontalIterator
from models.Iterator.VerticalIterator import VerticalIterator


class SeamCarvingImage:
    def __init__(self, array):
        self.horizontal_iterator = HorizontalIterator(array[len(array) - 1][0])
        self.vertical_iterator = VerticalIterator(array[0][len(array[0]) - 1])
