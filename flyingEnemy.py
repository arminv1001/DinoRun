import random
import pygame

from GameObject import GameObject


class flyingEnemy(GameObject):
    def __init__(self, WIDTH, HEIGHT, difficulty):
        self.width = 60
        self.height = 70
        self.hillPic = pygame.image.load("images/Objekte/flyMan_fly.png")
        self.hillPic = pygame.transform.scale(self.hillPic, (self.width, self.height))
        self.spawn = False
        self.ResetX = WIDTH + self.width + 10
        self.X = self.ResetX
        self.Y = HEIGHT-240
        self.difficulty = difficulty
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)


    def drawHitbox(self, window):
        """
        :return:
        """
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        pygame.draw.rect(window, (255, 0, 0), self.rect, 2)

    def place(self, window):
        """
        :param window: Pygame Fenster
        :return: -
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.hillPic, (self.X, self.Y))
            self.X -= 1 * self.difficulty * 2
            self.drawHitbox(window)
            if self.X <= -self.width:
                self.spawn = False
                self.X = self.ResetX