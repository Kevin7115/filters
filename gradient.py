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


def apply_gradient_map(image_path, output_path, gradient_colors):
    """
    Applies a color gradient map to a grayscale image.

    Args:
        image_path (str): Path to the grayscale image.
        gradient_colors (list of tuples): List of RGB color tuples 
                                         defining the gradient.

    Returns:
        Image.Image: The processed image with the gradient applied.
    """

    img = greyscale(load_image(image_path))
    height, width = img["height"], img["width"]
    pixels = convert_2d(img["pixels"], height, width)

    output_pixels = [[None for _ in range(width)] for _ in range(height)]

    for x in range(width):
        for y in range(height):
            brightness = pixels[y][x] / 255.0
            index = int(brightness * (len(gradient_colors) - 1))
            color1 = gradient_colors[index]
            color2 = gradient_colors[min(index + 1, len(gradient_colors) - 1)]
            factor = brightness * (len(gradient_colors) - 1) - index
            
            r = int(color1[0] + (color2[0] - color1[0]) * factor)
            g = int(color1[1] + (color2[1] - color1[1]) * factor)
            b = int(color1[2] + (color2[2] - color1[2]) * factor)
            output_pixels[y][x] = (r, g, b)

    save_image({
        "height": height,
        "width": width,
        "pixels": flatten(output_pixels),
    }, output_path, greyscale=False)


# Example usage:
# https://uigradients.com/#Wiretap - premade gradients
# https://www.rapidtables.com/web/color/RGB_Color.html - color to rgb value

# Idk but its a pretty cool orange
# gradient_colors = [(0, 0, 0), (255, 0, 0), (255, 255, 0), (255, 255, 255)]

# Wire Tap
gradient_colors = [(138, 35, 135), (233, 64, 87), (242, 113, 33)]

#Freaky
# gradient_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Freaky but Winter
# gradient_colors = [(50, 0, 50), (0, 255, 179), (255, 0, 255)]

apply_gradient_map("mount-fuji.png", "mount-gradient.png", gradient_colors)
