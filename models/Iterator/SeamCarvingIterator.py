class SeamCarvingIterator:
    def __init__(self, start_pixel):
        self.current_pixel = start_pixel

    def __iter__(self):
        return self