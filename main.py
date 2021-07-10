import argparse
import warnings

from file.utils import processFolderContents, generateFilename, buildPath, createDirectory, \
    getImagesPathsInDirectory
from image.processing import enhancedResize
from image.utils import openImage, saveImage
from triptychGeneration import createTriptych


# INPUTS
OUTPUT_WIDTH = 1920
OUTPUT_HEIGHT = 1080
OUTPUT_DIMENSIONS = (OUTPUT_WIDTH, OUTPUT_HEIGHT)
TRIPTYCH_ELEMENT_WIDTH = 600
BACKGROUND_COLOR = (255, 255, 255)


# CONSTS
TRIPTYCH_ELEMENT_HEIGHT_BY_WIDTH = 3 / 2


class Counter:
    def __init__(self):
        self.counter = 0

    def getValue(self):
        self.counter += 1
        return self.counter


def fullTriptychFlow(
    folderPath: str,
    counter: Counter,
    outputFolder: str,
    elementWidth: int,
    backgroundColor: str,
    spacing: int
) -> None:
    # TODO: extract to separate function
    TRIPTYCH_ELEMENT_HEIGHT = int(elementWidth * TRIPTYCH_ELEMENT_HEIGHT_BY_WIDTH)
    TRIPTYCH_ELEMENT_DIMENSIONS = (elementWidth, TRIPTYCH_ELEMENT_HEIGHT)
    TRIPTYCH_ELEMENT_MARGIN_TOP = (OUTPUT_HEIGHT - TRIPTYCH_ELEMENT_HEIGHT) // 2

    # TODO: add dimension checks
    unoccupiedTriptychWidth = OUTPUT_WIDTH - 3 * elementWidth - 2 * (spacing if spacing is not None else 0)

    # TODO: there is probably bug with spacing: try --elementWidth=550 and spacing=30
    if spacing is not None:
        TRIPTYCH_SPACING = spacing
        TRIPTYCH_ELEMENT_MARGIN_SIDES = (unoccupiedTriptychWidth - 2 * TRIPTYCH_SPACING) // 2
    else:
        TRIPTYCH_ELEMENT_MARGIN_SIDES = (unoccupiedTriptychWidth) // 4
        TRIPTYCH_SPACING = TRIPTYCH_ELEMENT_MARGIN_SIDES

    imagePaths = getImagesPathsInDirectory(folderPath)
    imageCount = len(imagePaths)

    # TODO: handle cases with 4, 2 and 1 image in directory
    # TODO: when above happens, rename "triptych" to something else (project name can stay)
    # TODO: handle horizontal images and mix of vertical + horizontal
    if imageCount is 3:
        images = [enhancedResize(openImage(path), TRIPTYCH_ELEMENT_DIMENSIONS) for path in imagePaths]
        triptych = createTriptych(
            images,
            OUTPUT_DIMENSIONS,
            backgroundColor,
            TRIPTYCH_ELEMENT_MARGIN_TOP,
            TRIPTYCH_ELEMENT_MARGIN_SIDES,
            elementWidth,
            TRIPTYCH_SPACING
        )

        outputFilename = generateFilename(counter.getValue())
        outputPath = buildPath(outputFolder, outputFilename)

        saveImage(triptych, outputPath)
    else:
        warnings.warn(f'Invalid number of files in directory - expected 3, got {imageCount} instead')


def parseArguments():
    # TODO: disallow overwriting files by default and add warning, yes/no question
    parser = argparse.ArgumentParser()
    parser.add_argument('sourceFolder')
    parser.add_argument('outputFolder')
    parser.add_argument('--elementWidth', help='Width of a single image within triptych')
    parser.add_argument('--backgroundColor', help='Background color of triptych')
    parser.add_argument('--spacing', help='Spacing in px between images')
    # TODO add option for frame and frame color
    # TODO with more and more options, consider moving to json/yaml file-based config?
    return parser.parse_args()


if __name__ == '__main__':
    # TODO: extract as separate config function, integrate with parser
    args = parseArguments()
    sourceFolder = args.sourceFolder
    outputFolder = args.outputFolder
    elementWidth = int(args.elementWidth) if args.elementWidth else TRIPTYCH_ELEMENT_WIDTH
    backgroundColor = args.backgroundColor if args.backgroundColor else BACKGROUND_COLOR
    spacing = int(args.spacing) if args.spacing else None

    createDirectory(outputFolder)

    imageCounter = Counter()
    generateTriptych = lambda folder: fullTriptychFlow(folder, imageCounter, outputFolder, elementWidth, backgroundColor, spacing)
    processFolderContents(sourceFolder, generateTriptych)
