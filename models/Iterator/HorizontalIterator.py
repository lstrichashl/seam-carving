from models.Iterator.SeamCarvingIterator import SeamCarvingIterator


class HorizontalIterator(SeamCarvingIterator):
    def next(self):
        self.current_pixel = self.current_pixel.east()
        return self.current_pixel
