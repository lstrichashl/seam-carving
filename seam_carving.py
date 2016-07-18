from models.Iterator.VerticalGradientIterator import VerticalGradientIterator
from models.gradient import ParentHorizontalDirection, ParentVerticalDirection, Gradient
from models.image_pixel import ImagePixel
from models.seam_carving_image import SeamCarvingImage


def main(regular_image):
    image = regular_image_to_seam_carving_image(regular_image)


def regular_image_to_seam_carving_image(regular_image):
    image_pixel_array = regular_image_to_image_pixel_array(regular_image)
    image = SeamCarvingImage(image_pixel_array)
    set_image_neighbors(image_pixel_array)
    set_image_gradients(image)
    return image


def find_seam_vertical(image):
    min_pixel = min(image.horizontal_iterator)
    iterator = VerticalGradientIterator(min_pixel)
    for pixel, next_direction in iterator:
        delete_vertical_pixel(pixel, next_direction)
        last_pixel = pixel


def delete_vertical_pixel(pixel, next_direction):
    if pixel.east() is not None:
        pixel.east().set_west(pixel.west())
    if pixel.west() is not None:
        pixel.west().set_east(pixel.east())
    if ParentVerticalDirection.north_east == next_direction:
        if pixel.north() is not None:
            pixel.north().set_south(pixel.east())
        if pixel.east() is not None:
            pixel.east().set_north(pixel.north())
    elif ParentVerticalDirection.north_west == next_direction:
        if pixel.north() is not None:
            pixel.north().set_south(pixel.west())
        if pixel.west() is not None:
            pixel.west().set_north(pixel.north())
    update_pixel_energy(pixel.east())
    update_pixel_energy(pixel.west())


def regular_image_to_image_pixel_array(image):
    return [[ImagePixel(value=image[row_index][column_index])
             for column_index, pixel in enumerate(row)]
            for row_index, row in enumerate(image)]


def set_image_gradients(image):
    for pixel in image:
        set_pixel_vertical_gradient(pixel)
        set_pixel_horizontal_gradient(pixel)


def set_pixel_vertical_gradient(pixel):
    if pixel.north().gradient_vertical.value < pixel.north().east().gradient_vertical.value:
        if pixel.north().gradient_vertical.value < pixel.north().west().gradient_vertical.value:
            pixel.gradient_vertical = Gradient(value=pixel.north().gradient_vertical.value + pixel.energy_value,
                                               parent=pixel.north(),
                                               parent_direction=ParentVerticalDirection.north)
    elif pixel.north().east().gradient_vertical.value < pixel.north().west().gradient_vertical.value:
        pixel.gradient_vertical = Gradient(value=pixel.north().east().gradient_vertical.value + pixel.energy_value,
                                           parent=pixel.north().east(),
                                           parent_direction=ParentVerticalDirection.north_east)
    else:
        pixel.gradient_vertical = Gradient(value=pixel.north().west().gradient_vertical.value + pixel.energy_value,
                                           parent=pixel.north().west(),
                                           parent_direction=ParentVerticalDirection.north_west)


def set_pixel_horizontal_gradient(pixel):
    if pixel.north().west().gradient_horizontal.value < pixel.west().gradient_horizontal.value:
        if pixel.north().west().gradient_horizontal.value < pixel.south().west().gradient_horizontal.value:
            pixel.gradient_horizontal = Gradient(value=pixel.north().west().gradient_horizontal.value + pixel.energy_value,
                                                 parent=pixel.north().west(),
                                                 parent_direction=ParentHorizontalDirection.north_west)
    elif pixel.west().gradient_horizontal.value < pixel.south().west().gradient_horizontal.value:
        pixel.gradient_horizontal = Gradient(value=pixel.west().gradient_horizontal.value + pixel.energy_value,
                                             parent=pixel.west(),
                                             parent_direction=ParentHorizontalDirection.west)
    else:
        pixel.gradient_horizontal = Gradient(value=pixel.south().west().gradient_horizontal.value + pixel.energy_value,
                                             parent=pixel.south().west(),
                                             parent_direction=ParentHorizontalDirection.south_west)


def set_image_neighbors(image_pixel_array):
    for row_index, row in enumerate(image_pixel_array):
        for column_index, pixel in enumerate(row):
            set_pixel_neighbors(pixel, image_pixel_array, row_index, column_index)


def set_pixel_neighbors(pixel, array, row_index, column_index):
    if row_index > 0:
        pixel.set_north(array[row_index - 1][column_index])
    if row_index < len(array):
        pixel.set_south(array[row_index + 1][column_index])
    if column_index > 0:
        pixel.set_east(array[row_index][column_index - 1])
    if column_index < len(array[0]):
        pixel.set_west(array[row_index][column_index + 1])
    update_pixel_energy(pixel)


def update_pixel_energy(pixel):
    energy_value = pixel.north().value
    energy_value += pixel.north().east().value
    energy_value += pixel.east().value
    energy_value += pixel.south().east().value
    energy_value += pixel.south().value
    energy_value += pixel.south().west().value
    energy_value += pixel.west().value
    energy_value += pixel.north().west().value
    energy_value /= 8
    pixel.energy_value = energy_value

