class SeamCarvingIterator:
    def __init__(self, start_pixel):
        self.start_pixel = start_pixel
        self.current_pixel = self.start_pixel

    def __iter__(self):
        return self