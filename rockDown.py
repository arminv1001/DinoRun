import random

import pygame


class rockDown:
    def __init__(self, WIDTH, HEIGHT, difficulty):
        self.width = 150
        self.height = 335
        self.hillPic = pygame.image.load("images/Objekte/rockGrassDown.png")
        self.hillPic = pygame.transform.scale(self.hillPic, (self.width, self.height))
        self.spawn = False
        self.ResetX = WIDTH + self.width + 10
        self.X = self.ResetX
        self.Y = 0
        self.difficulty = difficulty
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)

    def randomSpawn(self):
        """
        :return:
        """
        if self.spawn == False:
            self.spawn = random.random() > 0.99

    def drawHitbox(self, window):
        """
        :return:
        """
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        pygame.draw.rect(window, (255, 0, 0), self.rect, 2)

    def placeRockDown(self, window):
        """
        :param window: Pygame Fenster
        :return: -
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.hillPic, (self.X, self.Y))
            self.X -= 1 * self.difficulty
            self.drawHitbox(window)
            if self.X <= -self.width:
                self.spawn = False
                self.X = self.ResetX