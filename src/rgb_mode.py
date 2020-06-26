"""Initial testing for getting modal image color"""

import sys
from PIL import Image
import numpy as np
from scipy import stats

def get_rgb_value(image):
    """Print the average rgb values as a tuple"""

    x_length = image.size[0]
    y_length = image.size[1]

    pixels = []

    for i in range(x_length):
        for j in range(y_length):
            htmlColor = "#%02X%02X%02X" % (image.getpixel((i, j))[0],
                                           image.getpixel((i, j))[1],
                                           image.getpixel((i, j))[2])
            pixels.append(htmlColor)

    print(stats.mode(pixels)[0][0])
    return stats.mode(pixels)[0][0]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect number of arguments")
    else:
        im = Image.open(sys.argv[1])
        get_rgb_value(im)
