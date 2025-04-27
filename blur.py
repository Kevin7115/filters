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


def getNeighbors(x, y, array, radius):
    neighbors = []
    for y_p in range(y-radius, y+radius+1):
        for x_p in range(x-radius, x+radius):
            neighbors.append(array[y_p][x_p])
    return neighbors


def get_average(x, y, array):
    average = array[y][x]
    neighbors = getNeighbors(x, y, array, 21)
    for pixel in neighbors:
        average = add_pixel(average, pixel)
    
    return (int(average[0]/441), int(average[1]/441), int(average[2]/441))


def avg(x, y, array, radius):
    # Combines the getNeighbor and summation process so it runs quicker
    average = (0, 0, 0)
    for y_p in range(y-(radius // 2), y+(radius // 2)+1):
        for x_p in range(x-(radius // 2), x+(radius // 2)+1):
            average = add_pixel(average, array[y_p][x_p])

    return (int(average[0]/(radius*radius)), 
            int(average[1]/(radius*radius)),
            int(average[2]/(radius*radius)))


def apply_blur_effect(image_path, output_path):

    try:
        img = load_image(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return

    height, width = img["height"], img["width"]
    img_array = convert_2d(img["pixels"], height, width)

    new_img_array = [[(0,0,0) for x in range(width)] for y in range(height)]
    radius = 11

    for y in range(radius, height-radius):
        for x in range(radius, width-radius):
            new_img_array[y][x] = avg(x, y, img_array, radius)
            
    new_pixels = flatten(new_img_array)

    save_image({
        "height": height,
        "width": width,
        "pixels": new_pixels,
    }, output_path, greyscale=False)


# Example usage:
apply_blur_effect("spider.png", "blurspider.png")