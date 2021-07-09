from PIL import ImageEnhance, Image

DEFAULT_SHARPEN_FACTOR = 1.5
RGB_IMAGE_MODE = 'RGB'


def sharpen(image, factor):
    enhancer = ImageEnhance.Sharpness(image)
    sharpenedImage = enhancer.enhance(factor)
    return sharpenedImage


def resize(image, dimensions):
    return image.resize(dimensions, Image.LANCZOS)


def enhancedResize(image, dimensions, sharpenFactor=DEFAULT_SHARPEN_FACTOR ):
    out = resize(image, dimensions)
    sharpened = sharpen(out, sharpenFactor)
    return sharpened


def createEmptyImage(dimensions, color):
    return Image.new(RGB_IMAGE_MODE, dimensions, color)
