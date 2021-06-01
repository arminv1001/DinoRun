import pygame
import random


class GameObject:

    def __init__(self, WIDTH, HEIGHT, difficulty, imageObj, widthObj, heightObj, Y):
        self.widthFrame = WIDTH
        self.heightFrame = HEIGHT
        self.widthObj = widthObj
        self.heightObj = heightObj
        self.difficulty = difficulty
        self.Y = Y
        self.ResetX = WIDTH + self.widthObj + 10
        self.X = self.ResetX
        self.image = imageObj
        self.hitbox = pygame.Rect(self.X, self.Y, self.widthObj, self.heightObj)
        self.spawn = False

    def randomSpawn(self):
        """
        :return:
        """
        if not self.spawn:
            self.spawn = random.random() > 0.99

    def drawHitbox(self, window):
        """
        :return:
        """
        self.hitbox = pygame.Rect(self.X, self.Y, self.widthObj, self.heightObj)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def place(self, window):
        """
        :param window: Pygame Fenster
        :return: -
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.image, (self.X, self.Y))
            self.X -= 1 * self.difficulty
            self.drawHitbox(window)
            if self.X <= -self.widthObj:
                self.spawn = False
                self.X = self.ResetX
