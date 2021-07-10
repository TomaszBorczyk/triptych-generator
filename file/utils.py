import os
from pathlib import Path
from typing import Callable, List

DEFAULT_EXTENSION = 'jpeg'
DEFAULT_NAME = ''
EXTENSION_SEPARATOR = '.'


def getImagesPathsInDirectory(directoryPath: str) -> List[str]:
    filenames = getFilenamesFromDirectory(directoryPath)
    imageFilenames = [filename for filename in filenames if isImageFile(filename)]

    return getPathsFromFilenames(directoryPath, imageFilenames)


def isImageFile(filename: str) -> bool:
    imageExtensions = ('.jpg', '.png')
    return filename.endswith(imageExtensions)


def processFolderContents(path: str, handler: Callable[[str], None]):
    sourceElements = os.listdir(path)

    for element in sourceElements:
        handler(os.path.join(path, element))


def getFilenamesFromDirectory(directoryPath: str) -> List[str]:
    return os.listdir(directoryPath)


def getPathsFromFilenames(directoryPath: str, filenames: List[str]) -> List[str]:
    return [os.path.join(directoryPath, element) for element in filenames]


def getFilesPathsInDirectory(directoryPath: str) -> List[str]:
    filenames = os.listdir(directoryPath)
    return [os.path.join(directoryPath, element) for element in filenames]


def buildPath(folderPath: str, filename: str):
    return os.path.join(folderPath, filename)


def generateFilename(counter: int, name: str=DEFAULT_NAME, extension: str=DEFAULT_EXTENSION):
    return name + str(counter) + EXTENSION_SEPARATOR + extension


def createDirectory(path: str):
    Path(path).mkdir(parents=False, exist_ok=True)
