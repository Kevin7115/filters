from rich import print
from PIL import Image

def load_image(filename):
    with open(filename, "rb") as img_handle:
        img = Image.open(img_handle)
        img = img.convert("RGB")  # in case we were given a greyscale image
        img_data = img.getdata()
        pixels = list(img_data)
        width, height = img.size
        return {"height": height, "width": width, "pixels": pixels}
    
def save_image(image, filename, mode = "PNG", greyscale = True):
    if (image["height"] is None or image["width"] is None or image["pixels"] is None):
        print("[yellow]Part 3 - Not Implemented Yet")
        return

    imgMode = "L" if greyscale else "RGB"
    out = Image.new(mode=imgMode, size=(image["width"], image["height"]))
    out.putdata(image["pixels"])
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()

def greyscale(img_data):
    pixels = [round(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]) for p in img_data["pixels"]]
    return {
        "height": img_data["height"],
        "width": img_data["width"],
        "pixels": pixels,
    }

def just_blue(img_data):
    pixels = [(p[0], 0, p[2]) for p in img_data["pixels"]]
    return {
        "height": img_data["height"],
        "width": img_data["width"],
        "pixels": pixels,
    }