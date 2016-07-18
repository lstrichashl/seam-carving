from models.Iterator.SeamCarvingIterator import SeamCarvingIterator


class HorizontalIterator(SeamCarvingIterator):
    def next(self):
        if self.current_pixel.south() is not None:
            self.current_pixel = self.current_pixel.east()
            return self.current_pixel
        else:
            self.current_pixel = self.start_pixel
            raise StopIteration()
