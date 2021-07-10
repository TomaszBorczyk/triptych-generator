from PIL import ImageEnhance, Image

DEFAULT_SHARPEN_FACTOR = 1.5


def sharpen(image, factor: float):
    enhancer = ImageEnhance.Sharpness(image)
    sharpenedImage = enhancer.enhance(factor)
    return sharpenedImage


def resize(image, dimensions):
    return image.resize(dimensions, Image.LANCZOS)


def enhancedResize(image, dimensions: (int, int), sharpenFactor: float=DEFAULT_SHARPEN_FACTOR):
    out = resize(image, dimensions)
    sharpened = sharpen(out, sharpenFactor)
    return sharpened
