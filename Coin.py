import pygame

from GameObject import GameObject


class Coin(GameObject):
    def __init__(self, WIDTH, HEIGHT, difficulty):
        widthObj = 40
        heightObj = 40
        coinImage = self.loadImage()
        Y = 370

        super().__init__(WIDTH, HEIGHT, difficulty, coinImage, widthObj, heightObj, Y)

    @staticmethod
    def loadImage():
        coinImage = pygame.image.load('Images/Objekte/coin.png')
        coinImage = pygame.transform.scale(coinImage, (40, 40))
        return coinImage

    def removeCoin(self):
        self.X = self.ResetX
