import random
import pygame

from GameObject import GameObject


class FlyingEnemy(GameObject):
    def __init__(self, WIDTH, HEIGHT, difficulty):
        widthObj = 60
        heightObj = 70
        flyImage = self.loadImage(widthObj, heightObj)
        Y = HEIGHT - 240

        super().__init__(WIDTH, HEIGHT, difficulty, flyImage, widthObj, heightObj, Y)

    @staticmethod
    def loadImage(widthObj, heightObj):
        flyImage = pygame.image.load("images/Objekte/flyMan_fly.png")
        flyImage = pygame.transform.scale(flyImage, (widthObj, heightObj))
        return flyImage

    def place(self, window):
        """
        :param window: Pygame Fenster
        :return: -
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.image, (self.X, self.Y))
            self.X -= 1 * self.difficulty * 2
            self.drawHitbox(window)
            if self.X <= -self.widthObj:
                self.spawn = False
                self.X = self.ResetX
