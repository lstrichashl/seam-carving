from enum import Enum

from models.image_pixel import ImagePixel


class Gradient:

    def __init__(self, value=-1, parent=ImagePixel(), parent_direction=ParentVerticalDirection.north_east):
        self.value = value
        self.parent = parent
        self.parent_direction = parent_direction


class ParentVerticalDirection(Enum):
    north_east = 0
    north = 1
    north_west = 2


class ParentHorizontalDirection(Enum):
    north_west = 0
    west = 1
    south_west = 2

