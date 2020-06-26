"""Sort the images in the images directory by color"""

import os
import shutil
from PIL import Image
from rgb_mode import get_rgb_value

IMAGE_DIR = './images/'
DEST_DIR = './sorted/'
SIZE = (128, 128)

def main():
    """Sort the images in the images directory by color"""
    images = os.listdir(IMAGE_DIR)

    for i, item in enumerate(images):
        images[i] = RGBImage(item)

    images.sort(key=lambda image: image.mode)
    print(images)

    for i, item in enumerate(images):
        shutil.copyfile(IMAGE_DIR + item.filename,
                        DEST_DIR + str(i) + item.filename[-4:])

class RGBImage:
    """Wrapper class for Pillow images"""
    def __init__(self, filename, shrink=True):
        self.filename = filename
        self.image = Image.open(IMAGE_DIR + filename)
        if shrink:
            self.shrink_image(SIZE)
        self.mode = get_rgb_value(self.image)

    def shrink_image(self, size):
        """Shrink the image to the size specified in the parameter"""
        self.image = self.image.transform(size, Image.EXTENT,
                                          (0, 0, self.image.width - 1,
                                           self.image.height - 1))
        return self

    def __repr__(self):
        return repr((self.filename, self.mode))

if __name__ == "__main__":
    main()
