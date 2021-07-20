from PIL import ImageEnhance, Image, ImageOps

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


def addBorder(image, borderSize: int, borderColor: str = '#ffffff'):
    img_with_border = ImageOps.expand(image, border=borderSize, fill=borderColor)
    return img_with_border
