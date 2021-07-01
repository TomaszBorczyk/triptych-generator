import os
from PIL import Image, ImageEnhance


MAIN_FOLDER = "C:\\Users\\Tom\\Desktop\\triptychs"
INPUT_SUBFOLDER = "\\source"
OUTPUT_SUBFOLDER = "\\output"
IMAGE_SUBPATH = "\\1\\DSCF6487.jpg"
IMAGE_SOURCE_FOLDER = MAIN_FOLDER + INPUT_SUBFOLDER
IMAGE_OUTPUT_FOLDER = MAIN_FOLDER + OUTPUT_SUBFOLDER
SHARPEN_FACTOR = 1.5

outputImagePathBuilder = lambda filename: IMAGE_OUTPUT_FOLDER + "\\" + filename


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


def sharpen(image, factor):
    enhancer = ImageEnhance.Sharpness(image)
    sharpenedImage = enhancer.enhance(factor)
    return sharpenedImage


def processImage(path):
    im = Image.open(path)
    out = im.resize((600, 900), Image.LANCZOS)
    sharpened = sharpen(out, SHARPEN_FACTOR)
    outfile = outputImagePathBuilder(str(imageCounter.getCounter()) + '.jpg')
    sharpened.save(outfile, 'JPEG', quality=100)


processSingleFolder = lambda path: processFolderContents(path, processImage)
processFolderContents(IMAGE_SOURCE_FOLDER, processSingleFolder)


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
