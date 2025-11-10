class Image:
    def __init__(self, pixelData):
        self.pixels = pixelData

    def applyTransformation(self, transformationFunction):
        duplicatedPixels = self.copyPixels()
        modifiedPixels = transformationFunction(duplicatedPixels)
        return Image(modifiedPixels)

    def copyPixels(self):
        return [r[:] for r in self.pixels]


def flipHorizontal(pixelData):
    flipped = []
    for row in pixelData:
        flipped.append(row[::-1])
    return flipped


def adjustBrightness(pixelData, brightnessValue):
    bright = []
    for row in pixelData:
        bright.append([p + brightnessValue for p in row])
    return bright


def rotateNinetyDegree(pixelData):
    rotated = zip(*pixelData[::-1])
    return [list(r) for r in rotated]


class AugmentationPipeline:
    def __init__(self):
        self.steps = []

    def addSteps(self, transformFunc):
        self.steps.append(transformFunc)

    def processImage(self, originalImage):
        transformedImages = []
        for func in self.steps:
            newImg = originalImage.applyTransformation(func)
            transformedImages.append(newImg)
        return transformedImages

originalPixels = [
    [10, 20, 30],
    [40, 50, 60]
]

img = Image(originalPixels)
pipeline = AugmentationPipeline()
pipeline.addSteps(flipHorizontal)
pipeline.addSteps(lambda data: adjustBrightness(data, 10))
pipeline.addSteps(rotateNinetyDegree)

results = pipeline.processImage(img)

for i, res in enumerate(results, start=1):
    print(f"Transformed Tmage {i}: ")
    for row in res.pixels:
        print(row)
