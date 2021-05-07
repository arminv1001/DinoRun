import random

import pygame

class Fence:
    def __init__(self,WIDTH,HEIGHT,difficulty):
        self.width = int(WIDTH/7)
        self.height = int(HEIGHT/7)
        self.hillPic = pygame.image.load("images/Huegel/fence.png")
        self.hillPic = pygame.transform.scale(self.hillPic, (self.width, self.height))
        self.spawn = False
        self.ResetX = WIDTH + self.width + 10
        self.X = self.ResetX
        self.Y = (HEIGHT * (1/2) + self.height) + 30
        self.difficulty = difficulty

    def randomSpawn(self):
        """
        :return:
        """
        if self.spawn == False:
            self.spawn = random.random() > 0.9

    def placeFence(self, window):
        """
        :param window: Pygame Fenster
        :return: -
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.hillPic,(self.X,self.Y))
            self.X -= 1 * self.difficulty
            if self.X <= -self.width:
                self.spawn = False
                self.X = self.ResetX