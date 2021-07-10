from image.utils import createEmptyImage


def createTriptych(images, dimensions: (int, int), backgroundColor: (int, int, int), marginTop: int, sideMargin: int, imageElementWidth: int):
    background = createEmptyImage(dimensions, backgroundColor)
    triptych = pasteImages(background, images, marginTop, sideMargin, imageElementWidth)

    return triptych


def pasteImages(background, images, upperLeftY: int, sideMargin: int, imageElementWidth: int):
    output = background.copy()

    for i, image in enumerate(images):
        upperLeftX = calculateImageX(i, imageElementWidth, sideMargin)
        output.paste(image, (upperLeftX, upperLeftY))

    return output


def calculateImageX(count: int, targetImageWidth: int, sideMargin: int) -> int:
    return count * targetImageWidth + (count + 1) * sideMargin
