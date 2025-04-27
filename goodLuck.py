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


def apply_filter_effect(image_path, output_path):

    try:
        img = load_image(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return

    height, width = None # get image height and width
    img_array = None # Convert to a 2d array

    new_img_array = [[(0,0,0) for x in range(width)] for y in range(height)]

    # add for loops to loop through every pixel
            
            
    new_pixels = None # Flatten it back to 1d

    save_image({
        "height": height,
        "width": width,
        "pixels": new_pixels,
    }, output_path, greyscale=False)

output_image = None # name your image
apply_filter_effect("mount-fuji.png", output_image)