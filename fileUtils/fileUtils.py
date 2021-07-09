import os


def processFolderContents(path, handler):
    sourceElements = os.listdir(path)

    for element in sourceElements:
        handler(os.path.join(path, element))


def getFolderFilesPaths(path):
    sourceElements = os.listdir(path)
    return [os.path.join(path, element) for element in sourceElements]


def buildPath(folderPath, filename):
    return os.path.join(folderPath, filename)


def generateFilename(counter, name='', extension='jpg'):
    return name + str(counter) + '.' + extension
