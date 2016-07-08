from models.energy import Energy
from models.gradient import Gradient


class ImagePixel:

    def __init__(self, value=0, energy=Energy(), gradient_horizontal=Gradient(), gradient_vertical=Gradient()):
        self.value = value
        self.energy = energy
        self.gradient_horizontal = gradient_horizontal
        self.gradient_vertical = gradient_vertical
