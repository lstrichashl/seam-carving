import numpy
from models.gradient import Gradient


class ImagePixel:

    def __init__(self,
                 value=-1,
                 north=-1,
                 east=-1,
                 south=-1,
                 west=-1,
                 gradient_horizontal=Gradient(),
                 gradient_vertical=Gradient()):
        self.value = value
        self.energy_value = -1
        self.__north = north
        self.__east = east
        self.__south = south
        self.__west = west
        self.gradient_horizontal = gradient_horizontal
        self.gradient_vertical = gradient_vertical

    def north(self):
        return self.__north

    def east(self):
        return self.__east

    def south(self):
        return self.__south

    def west(self):
        return self.__west

    def set_north(self, north):
        self.__north = north
        return self

    def set_east(self, east):
        self.__east = east
        return self

    def set_south(self, south):
        self.__south = south
        return self

    def set_west(self, west):
        self.__west = west
        return self