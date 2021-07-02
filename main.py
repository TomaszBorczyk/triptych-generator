import os
from PIL import Image, ImageEnhance


MAIN_FOLDER = "C:\\Users\\Tom\\Desktop\\triptychs"
INPUT_SUBFOLDER = "source"
OUTPUT_SUBFOLDER = "output"
IMAGE_SOURCE_FOLDER = os.path.join(MAIN_FOLDER, INPUT_SUBFOLDER)
IMAGE_OUTPUT_FOLDER = os.path.join(MAIN_FOLDER, OUTPUT_SUBFOLDER)

SHARPEN_FACTOR = 1.5

OUTPUT_WIDTH = 1920
OUTPUT_HEIGHT = 1080
OUTPUT_DIMENSIONS = (OUTPUT_WIDTH, OUTPUT_HEIGHT)

TRIPTYCH_ELEMENT_HEIGHT_BY_WIDTH = 3/2
TRIPTYCH_ELEMENT_WIDTH = 600
TRIPTYCH_ELEMENT_HEIGHT = int(TRIPTYCH_ELEMENT_WIDTH * TRIPTYCH_ELEMENT_HEIGHT_BY_WIDTH)
TRIPTYCH_ELEMENT_DIMENSIONS = (TRIPTYCH_ELEMENT_WIDTH, TRIPTYCH_ELEMENT_HEIGHT)

TRIPTYCH_ELEMENT_MARGIN_TOP = (OUTPUT_HEIGHT - TRIPTYCH_ELEMENT_HEIGHT) // 2
TRIPTYCH_ELEMENT_MARGIN_SIDES = (OUTPUT_WIDTH - 3 * TRIPTYCH_ELEMENT_WIDTH) // 4
TRIPTYCH_ELEMENT_MARGIN_INTERNAL = TRIPTYCH_ELEMENT_MARGIN_SIDES

BACKGROUND_COLOR = (255, 255, 255)


outputImagePathBuilder = lambda filename: os.path.join(IMAGE_OUTPUT_FOLDER, filename)


class ImageCounter:
    def __init__(self):
        self.counter = 0

    def getCounter(self):
        self.counter += 1
        return self.counter


imageCounter = ImageCounter()


def processFolderContents(path, handler):
    sourceElements = os.listdir(path)

    for element in sourceElements:
        handler(os.path.join(path, element))


def getFolderImages(path):
    sourceElements = os.listdir(path)
    return [os.path.join(path, element) for element in sourceElements]


def sharpen(image, factor):
    enhancer = ImageEnhance.Sharpness(image)
    sharpenedImage = enhancer.enhance(factor)
    return sharpenedImage


def processImage(path):
    im = Image.open(path)
    out = im.resize(TRIPTYCH_ELEMENT_DIMENSIONS, Image.LANCZOS)
    sharpened = sharpen(out, SHARPEN_FACTOR)
    return sharpened


def createTriptych(images):
    triptych = Image.new('RGB', OUTPUT_DIMENSIONS, BACKGROUND_COLOR)
    upperLeftY = TRIPTYCH_ELEMENT_MARGIN_TOP

    for i, image in enumerate(images):
        upperLeftX = i * TRIPTYCH_ELEMENT_WIDTH + (i + 1) * TRIPTYCH_ELEMENT_MARGIN_SIDES
        triptych.paste(image, (upperLeftX, upperLeftY))

    return triptych


def saveImage(image):
    outfile = outputImagePathBuilder(str(imageCounter.getCounter()) + '.jpg')
    image.save(outfile, 'JPEG', quality=100)


def fullTriptychFlow(folderPath):
    imagePaths = getFolderImages(folderPath)
    images = [processImage(path) for path in imagePaths]
    triptych = createTriptych(images)
    saveImage(triptych)


processFolderContents(IMAGE_SOURCE_FOLDER, fullTriptychFlow)

# IMAGE_SUBPATH = "\\1\\DSCF6487.jpg"
# im = Image.open(IMAGE_SOURCE_FOLDER + IMAGE_SUBPATH)
# sharpnessStep = 0.1
# sharpnessValues = [1 + x * sharpnessStep for x in range(1, 11)]
#
#
# def sharpen(image, factor):
#     enhancer = ImageEnhance.Sharpness(image)
#     sharpenedImage = enhancer.enhance(factor)
#     return sharpenedImage
#
#
# for sharpness in sharpnessValues:
#     sharpenedImage = sharpen(im, sharpness)
#     outfile = outputImagePathBuilder('sharpened_' + str(sharpness*10) + '.jpg')
#     sharpenedImage.save(outfile, 'JPEG', quality=100)
