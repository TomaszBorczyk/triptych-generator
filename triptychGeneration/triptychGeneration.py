from image.utils import createEmptyImage


def createTriptych(images, dimensions: (int, int), backgroundColor: str, marginTop: int, sideMargin: int,
                   imageElementWidth: int, spacing: int):
    background = createEmptyImage(dimensions, backgroundColor)
    triptych = pasteImages(background, images, marginTop, sideMargin, imageElementWidth, spacing)

    return triptych


def pasteImages(background, images, upperLeftY: int, sideMargin: int, imageElementWidth: int, spacing: int):
    output = background.copy()

    for i, image in enumerate(images):
        upperLeftX = calculateImageX(i, imageElementWidth, sideMargin, spacing)
        output.paste(image, (upperLeftX, upperLeftY))

    return output


def calculateImageX(count: int, targetImageWidth: int, sideMargin: int, spacing: int) -> int:
    return count * targetImageWidth + sideMargin + count * spacing
