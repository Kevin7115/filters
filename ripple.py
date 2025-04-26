import math
from pil_manager import *

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


def apply_wave_effect(image_path, output_path, amplitude=10, frequency=0.05):
    """
    Applies a wave effect to an image.

    Args:
        image_path: Path to the input image.
        output_path: Path to save the output image.
        amplitude: Amplitude of the wave.
        frequency: Frequency of the wave.
    """
    try:
        img = load_image(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return


    height, width = img["height"], img["width"]
    img_array = convert_2d(img["pixels"], height, width)

    new_img_array = [[None for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            # Calculate the offset using a sine function
            offset_x = int(amplitude * math.sin(2 * math.pi * frequency * y))

            # Apply the offset, handling boundaries
            new_x = (x + offset_x) % width
            new_img_array[y][x] = img_array[y][new_x]

    new_pixels = flatten(new_img_array)

    save_image({
        "height": height,
        "width": width,
        "pixels": new_pixels,
    }, output_path, greyscale=False)


# Example usage:
apply_wave_effect("mount-fuji.png", "ripple-fuji.png", amplitude=15, frequency=0.02)