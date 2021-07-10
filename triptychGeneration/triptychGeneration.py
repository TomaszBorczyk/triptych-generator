from image.utils import createEmptyImage


def createTriptych(images, dimensions, backgroundColor, marginTop, marginSides, imageElementWidth):
    background = createEmptyImage(dimensions, backgroundColor)
    triptych = pasteImages(background, images, marginTop, marginSides, imageElementWidth)

    return triptych


def pasteImages(background, images, upperLeftY, marginSides, imageElementWidth):
    output = background.copy()

    for i, image in enumerate(images):
        upperLeftX = calculateImageX(i, imageElementWidth, marginSides)
        output.paste(image, (upperLeftX, upperLeftY))

    return output


def calculateImageX(count, targetImageWidth, marginSides):
    return count * targetImageWidth + (count + 1) * marginSides
