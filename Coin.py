import pygame


class Coin:

    def __init__(self,difficulty, WIDTH, HEIGHT):
        self.difficulty = difficulty
        self.loadImage()
        self.setCoin()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT


    def setCoin(self):
        self.x = 1000
        self.y = 370

    def loadImage(self):
        self.coinImage = pygame.image.load('Images/Objekte/coin.png')
        self.coinImage = pygame.transform.scale(self.coinImage, (40, 40))

    def draw(self, window):
        if self.x >= 0:
            window.blit(self.coinImage,(self.x, self.y))
            self.x -= self.difficulty
            print(self.x)
        else:
            self.setCoin()