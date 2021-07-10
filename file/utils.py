import os

DEFAULT_EXTENSION = 'jpeg'
DEFAULT_NAME = ''
EXTENSION_SEPARATOR = '.'


def processFolderContents(path, handler):
    sourceElements = os.listdir(path)

    for element in sourceElements:
        handler(os.path.join(path, element))


def getFolderFilesPaths(path):
    sourceElements = os.listdir(path)
    return [os.path.join(path, element) for element in sourceElements]


def buildPath(folderPath, filename):
    return os.path.join(folderPath, filename)


def generateFilename(counter, name=DEFAULT_NAME, extension=DEFAULT_EXTENSION):
    return name + str(counter) + EXTENSION_SEPARATOR + extension