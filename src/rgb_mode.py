"""Get modal image color"""

from scipy import stats

def get_rgb_value(image):
    """Print the average rgb values as a tuple"""

    x_length = image.size[0]
    y_length = image.size[1]

    pixels = []

    for i in range(x_length):
        for j in range(y_length):
            html_color = "#%02X%02X%02X" % (image.getpixel((i, j))[0],
                                            image.getpixel((i, j))[1],
                                            image.getpixel((i, j))[2])
            pixels.append(html_color)

    return stats.mode(pixels)[0][0]
