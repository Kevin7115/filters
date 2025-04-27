from pil_manager import *
import math


def convert_2d(array, height, width):
    array_2d = []
    for y in range(height):
        new_row = []
        for x in range(width):
            new_row.append(array[y*width+x])
        array_2d.append(new_row)
    return array_2d


def flatten(array_2d):
    array = []
    for y in array_2d:
        for ele in y:
            array.append(ele)
    return array


def apply_vignette_effect(image_path, output_path):
    try:
        img = load_image(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return

    height, width = img["height"], img["width"]
    img_array = convert_2d(img["pixels"], height, width)

    center_x = width // 2
    center_y = height // 2
    max_distance = math.sqrt(center_x**2 + center_y**2)

    new_img_array = [row.copy() for row in img_array]

    for y in range(height):
        for x in range(width):
            pixel = img_array[y][x]
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            factor = 1 - (distance / max_distance)  # 1 near center, 0 near edges
            factor = factor * factor  # make it more dramatic (squared falloff)

            new_pixel = (
                int(pixel[0] * factor),
                int(pixel[1] * factor),
                int(pixel[2] * factor),
            )
            new_img_array[y][x] = new_pixel

    new_pixels = flatten(new_img_array)

    save_image({
        "height": height,
        "width": width,
        "pixels": new_pixels,
    }, output_path, greyscale=False)

apply_vignette_effect("mount-fuji.png", "mount-vignette.png")