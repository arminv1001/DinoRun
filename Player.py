import pygame

class Player:

    def __init__(self,x,y,step):
        self.x = x
        self.y = y
        self.step = step

        self.walkIndex = 0

    def left(self):
        self.x -= self.step

    def right(self):
        self.x += self.step

    def up(self):
        self.y -= self.step

    def loadImage(self):
        self.walkRight = [pygame.image.load('Images/SpielerImages/Right/R0.png'),
                          pygame.image.load('Images/SpielerImages/Right/R1.png'),
                          pygame.image.load('Images/SpielerImages/Right/R2.png'),
                          pygame.image.load('Images/SpielerImages/Right/R3.png'),
                          pygame.image.load('Images/SpielerImages/Right/R4.png'),
                          pygame.image.load('Images/SpielerImages/Right/R5.png'),
                          pygame.image.load('Images/SpielerImages/Right/R6.png'),
                          pygame.image.load('Images/SpielerImages/Right/R7.png')]

        self.walkLeft =  [pygame.image.load('Images/SpielerImages/Left/L0.png'),
                          pygame.image.load('Images/SpielerImages/Left/L1.png'),
                          pygame.image.load('Images/SpielerImages/Left/L2.png'),
                          pygame.image.load('Images/SpielerImages/Left/L3.png'),
                          pygame.image.load('Images/SpielerImages/Left/L4.png'),
                          pygame.image.load('Images/SpielerImages/Left/L5.png'),
                          pygame.image.load('Images/SpielerImages/Left/L6.png'),
                          pygame.image.load('Images/SpielerImages/Left/L7.png')]
