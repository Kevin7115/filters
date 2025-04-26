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


def add_pixel(pixel1, pixel2):
    return (
        pixel1[0] + pixel2[0],
        pixel1[1] + pixel2[1],
        pixel1[2] + pixel2[2],
    )

def getNeighbors(x, y, array):
    return [
        array[y-2][x-2],
        array[y-2][x-1],
        array[y-2][x],
        array[y-2][x+1],
        array[y-2][x+2],
        array[y-1][x-2],
        array[y-1][x-1],
        array[y-1][x],
        array[y-1][x+1],
        array[y-1][x+2],
        array[y][x-2],
        array[y][x-1],
        array[y][x+1],
        array[y][x+2],
        array[y+1][x-2],
        array[y+1][x-1],
        array[y+1][x],
        array[y+1][x+1],
        array[y+1][x+2],
        array[y+2][x-2],
        array[y+2][x-1],
        array[y+2][x],
        array[y+2][x+1],
        array[y+2][x+2],
    ]

def get_average(x, y, array):
    average = array[y][x]
    for pixel in getNeighbors(x, y, array):
        average = add_pixel(average, pixel)
    # return (int(average[0]/9), int(average[1]/9), int(average[2]/9))
    return (int(average[0]/25), int(average[1]/25), int(average[2]/25))


def apply_blur_effect(image_path, output_path):

    try:
        img = load_image(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return

    height, width = img["height"], img["width"]
    img_array = convert_2d(img["pixels"], height, width)

    new_img_array = [[(0,0,0) for x in range(width)] for y in range(height)]
    # x, y = 100, 100
    # print(img_array[y][x])
    # print(getNeighbors(x, y, img_array))
    # print(get_average(x, y, img_array))
    # return

    for y in range(2, height-2):
        for x in range(2, width-2):
            new_img_array[y][x] = get_average(x, y, img_array)
            
    new_pixels = flatten(new_img_array)

    save_image({
        "height": height,
        "width": width,
        "pixels": new_pixels,
    }, output_path, greyscale=False)


# Example usage:
apply_blur_effect("spider.png", "blurspider.png")