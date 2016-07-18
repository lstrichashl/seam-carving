from models.Iterator.HorizontalIterator import HorizontalIterator
from models.Iterator.VerticalIterator import VerticalIterator


class SeamCarvingImage:
    def __init__(self, image_pixel_array):
        self.head = image_pixel_array[0][0]
        self.__current_horizontal_iter_pixel = self.head
        self.__current_vertical_iter_pixel = self.head
        self.horizontal_iterator = HorizontalIterator(image_pixel_array[len(image_pixel_array) - 1][0])
        self.vertical_iterator = VerticalIterator(image_pixel_array[0][len(image_pixel_array[0]) - 1])

    def __iter__(self):
        return self

    def next(self):
        if self.__current_horizontal_iter_pixel.east() is not None:
            self.__current_horizontal_iter_pixel = self.__current_horizontal_iter_pixel.east()
            return self.__current_horizontal_iter_pixel
        elif self.__current_vertical_iter_pixel.south() is not None:
            self.__current_vertical_iter_pixel = self.__current_vertical_iter_pixel.south()
            self.__current_horizontal_iter_pixel = self.__current_vertical_iter_pixel
            return self.__current_horizontal_iter_pixel
        else:
            self.__current_horizontal_iter_pixel = self.head
            raise StopIteration()
