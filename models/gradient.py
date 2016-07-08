from models.image_pixel import ImagePixel


class Gradient:

    def __init__(self, value=-1, parent=ImagePixel()):
        self.value = value
        self.parent = parent

