from models.image_pixel import ImagePixel


class Gradient:

    def __init__(self, value=0, parent=ImagePixel()):
        self.value = value
        self.parent = parent

