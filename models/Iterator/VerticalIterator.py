from models.Iterator.SeamCarvingIterator import SeamCarvingIterator


class VerticalIterator(SeamCarvingIterator):
    def next(self):
        self.current_pixel = self.current_pixel.south()
        return self.current_pixel