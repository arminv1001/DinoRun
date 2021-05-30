import pygame
import random


class GameObject:

    def __init__(self, WIDTH, HEIGHT, difficulty,imageObj, widthObj, heightObj):
        self.widthFrame = WIDTH
        self.heightFrame = HEIGHT
        self.widthObj = widthObj
        self.heightObj = heightObj
        self.difficulty = difficulty
        self.X = 0
        self.Y = 0
        self.image = pygame.image.load(imageObj)
        self.hitbox = pygame.Rect(self.X,self.Y, self.widthObj,self.heightObj)

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
        self.hitbox = pygame.Rect(self.X, self.Y, self.widthFrame, self.heightFrame)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
