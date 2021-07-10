import os
from typing import Callable

DEFAULT_EXTENSION = 'jpeg'
DEFAULT_NAME = ''
EXTENSION_SEPARATOR = '.'


def processFolderContents(path: str, handler: Callable[[str], None]):
    sourceElements = os.listdir(path)

    for element in sourceElements:
        handler(os.path.join(path, element))


def getFolderFilesPaths(path: str):
    sourceElements = os.listdir(path)
    return [os.path.join(path, element) for element in sourceElements]


def buildPath(folderPath: str, filename: str):
    return os.path.join(folderPath, filename)


def generateFilename(counter: int, name: str=DEFAULT_NAME, extension: str=DEFAULT_EXTENSION):
    return name + str(counter) + EXTENSION_SEPARATOR + extension
