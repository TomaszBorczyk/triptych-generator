import os

from fileUtils.fileUtils import getFolderFilesPaths, processFolderContents, generateFilename, \
    buildPath
from imageUtils.imageProcessing import enhancedResize
from imageUtils.utils import openImage, saveImage
from triptychGeneration import createTriptych

MAIN_FOLDER = "C:\\Users\\Tom\\Desktop\\triptychs"
INPUT_SUBFOLDER = "source"
OUTPUT_SUBFOLDER = "output"
IMAGE_SOURCE_FOLDER = os.path.join(MAIN_FOLDER, INPUT_SUBFOLDER)
IMAGE_OUTPUT_FOLDER = os.path.join(MAIN_FOLDER, OUTPUT_SUBFOLDER)

OUTPUT_WIDTH = 1920
OUTPUT_HEIGHT = 1080
OUTPUT_DIMENSIONS = (OUTPUT_WIDTH, OUTPUT_HEIGHT)

TRIPTYCH_ELEMENT_HEIGHT_BY_WIDTH = 3 / 2
TRIPTYCH_ELEMENT_WIDTH = 600
TRIPTYCH_ELEMENT_HEIGHT = int(TRIPTYCH_ELEMENT_WIDTH * TRIPTYCH_ELEMENT_HEIGHT_BY_WIDTH)
TRIPTYCH_ELEMENT_DIMENSIONS = (TRIPTYCH_ELEMENT_WIDTH, TRIPTYCH_ELEMENT_HEIGHT)

TRIPTYCH_ELEMENT_MARGIN_TOP = (OUTPUT_HEIGHT - TRIPTYCH_ELEMENT_HEIGHT) // 2
TRIPTYCH_ELEMENT_MARGIN_SIDES = (OUTPUT_WIDTH - 3 * TRIPTYCH_ELEMENT_WIDTH) // 4
TRIPTYCH_ELEMENT_MARGIN_INTERNAL = TRIPTYCH_ELEMENT_MARGIN_SIDES

BACKGROUND_COLOR = (255, 255, 255)


class Counter:
    def __init__(self):
        self.counter = 0

    def getValue(self):
        self.counter += 1
        return self.counter


def fullTriptychFlow(folderPath, counter):
    imagePaths = getFolderFilesPaths(folderPath)
    images = [enhancedResize(openImage(path), TRIPTYCH_ELEMENT_DIMENSIONS) for path in imagePaths]
    triptych = createTriptych(
        images,
        OUTPUT_DIMENSIONS,
        BACKGROUND_COLOR,
        TRIPTYCH_ELEMENT_MARGIN_TOP,
        TRIPTYCH_ELEMENT_MARGIN_SIDES,
        TRIPTYCH_ELEMENT_WIDTH
    )

    outputFilename = generateFilename(counter.getValue())
    outputPath = buildPath(IMAGE_OUTPUT_FOLDER, outputFilename)

    saveImage(triptych, outputPath)


if __name__ == '__main__':
    imageCounter = Counter()
    generateTriptych = lambda folder: fullTriptychFlow(folder, imageCounter)
    processFolderContents(IMAGE_SOURCE_FOLDER, generateTriptych)
