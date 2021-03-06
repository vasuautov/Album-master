import pygame

class ImageBank:
    Images = None

    def __init__(self):
        self.Images = []

    def append(self, image):
        self.Images.append(image)
        return len(self.Images) - 1

    def dell_by_index(self, index):
        del self.Images[index]

    def get(self, index):
        if index < 0 or index > len(self.Images) - 1:
            return None
        return self.Images[index]
