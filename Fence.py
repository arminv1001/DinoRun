import random
import pygame

from GameObject import GameObject


class Fence(GameObject):
    def __init__(self, WIDTH, HEIGHT, difficulty):

        widthObj = int(WIDTH / 7)
        heightObj = int(HEIGHT / 7)
        fenceImage = self.loadImage(widthObj, heightObj)
        Y = (HEIGHT * (1 / 2) + heightObj) + 30
        super().__init__(WIDTH, HEIGHT, difficulty, fenceImage, widthObj, heightObj, Y)

    @staticmethod
    def loadImage(widthObj, heightObj):
        fenceImage = pygame.image.load("images/Objekte/fence.png")
        fenceImage = pygame.transform.scale(fenceImage, (widthObj, heightObj))
        return fenceImage




