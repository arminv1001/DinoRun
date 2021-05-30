import pygame
import random


class GameObject:

    def __init__(self, WIDTH, HEIGHT, difficulty):
        self.width = WIDTH
        self.height = HEIGHT
        self.difficulty = difficulty
        self.X = 0
        self.Y = 0


    def setX(self, x):
        self.X = x

    def setY(self, y):
        self.Y = y

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
