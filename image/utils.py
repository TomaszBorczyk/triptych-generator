from PIL import Image

MAX_QUALITY = 100
JPEG_TYPE = 'JPEG'
RGB_IMAGE_MODE = 'RGB'


def openImage(path: str):
    return Image.open(path)


def saveImage(image, target: str):
    image.save(target, JPEG_TYPE, quality=MAX_QUALITY)


def createEmptyImage(dimensions: (int, int), color: (int, int, int)):
    return Image.new(RGB_IMAGE_MODE, dimensions, color)
