"""Initial testing for getting average imageage color"""

from PIL import Image
# imageport numpy as np

def main():
    """Print the average rgb values as a tuple"""

    image = Image.open('./images/checkerboard.jpg')

    x_length = image.size[0]
    y_length = image.size[1]
    total_pixels = x_length * y_length

    rsum = 0
    gsum = 0
    bsum = 0

    for i in range(x_length):
        for j in range(y_length):
            rsum += image.getpixel((i, j))[0]
            gsum += image.getpixel((i, j))[1]
            bsum += image.getpixel((i, j))[2]

    rsum /= total_pixels
    gsum /= total_pixels
    bsum /= total_pixels

    average_rbg_values = (rsum, gsum, bsum)

    print(average_rbg_values)


if __name__ == "__main__":
    main()
