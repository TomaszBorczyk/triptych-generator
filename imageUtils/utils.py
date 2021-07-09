from PIL import Image

MAX_QUALITY = 100
JPEG_TYPE = 'JPEG'


def openImage(path):
    return Image.open(path)


def saveImage(image, target):
    image.save(target, JPEG_TYPE, quality=MAX_QUALITY)
