from PIL import Image

MAX_QUALITY = 100


def openImage(path):
    im = Image.open(path)
    return im


def saveImage(image, target):
    image.save(target, 'JPEG', quality=MAX_QUALITY)
