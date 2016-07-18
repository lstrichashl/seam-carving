from models.Iterator.SeamCarvingIterator import SeamCarvingIterator


class HorizontalGradientIterator(SeamCarvingIterator):
    def next(self):
        if self.current_pixel.horizontal_iterator.parent is not None:
            pixel = self.current_pixel.horizontal_iterator.parent
            self.current_pixel = pixel
            return pixel, pixel.horizontal_iterator.parent_direction
        else:
            self.current_pixel = self.start_pixel
            raise StopIteration()
