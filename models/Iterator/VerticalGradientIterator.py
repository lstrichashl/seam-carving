from models.Iterator.SeamCarvingIterator import SeamCarvingIterator


class VerticalGradientIterator(SeamCarvingIterator):
    def next(self):
        if self.current_pixel.gradient_vertical.parent is not None:
            pixel = self.current_pixel.gradient_vertical.parent
            self.current_pixel = pixel
            return pixel, pixel.gradient_vertical.parent_direction
        else:
            self.current_pixel = self.start_pixel
            raise StopIteration()
