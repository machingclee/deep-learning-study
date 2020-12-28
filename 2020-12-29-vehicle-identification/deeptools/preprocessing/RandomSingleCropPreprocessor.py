from sklearn.feature_extraction.image import extract_patches_2d

# this processor randomly crop an image of fixed size.


class RandomSingleCropPreprocessor:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def preprocess(self, image):
        return extract_patches_2d(image, (self.height, self.width), max_patches=1)[0]
