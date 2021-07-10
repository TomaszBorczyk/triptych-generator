from PIL import Image

MAX_QUALITY = 100
JPEG_TYPE = 'JPEG'
RGB_IMAGE_MODE = 'RGB'


def openImage(path):
    return Image.open(path)


def saveImage(image, target):
    image.save(target, JPEG_TYPE, quality=MAX_QUALITY)


def createEmptyImage(dimensions, color):
    return Image.new(RGB_IMAGE_MODE, dimensions, color)
