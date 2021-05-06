import pygame


class Player:

    def __init__(self, x, y, step, difficulty):
        self.x = x - 48
        self.y = y - 64
        self.step = step
        self.difficulty = difficulty
        self.left = False
        self.right = False
        self.walkIndex = 0
        self.loadImage()

    def draw(self, window):
        if self.walkIndex + 1 >= 42:
            self.walkIndex = 0

        if self.left:
            window.blit(self.walkLeft[self.walkIndex // 6], (self.x, self.y))
            if self.x >= 0:
                self.x -= self.step
                self.walkIndex += 1
        elif self.right:
            # TODO muss besser
            window.blit(self.walkRight[self.walkIndex // 6], (self.x, self.y))
            if self.x <= 700:
                self.x += self.step
                self.walkIndex += 1
        else:
            window.blit(self.standing, (self.x, self.y))
            if self.x >= 0:
                self.x -= self.difficulty

    def loadImage(self):
        # Bildgroeße: 96x128
        self.walkRight = [pygame.image.load('Images/SpielerImages/Right/R0.png'),
                          pygame.image.load('Images/SpielerImages/Right/R1.png'),
                          pygame.image.load('Images/SpielerImages/Right/R2.png'),
                          pygame.image.load('Images/SpielerImages/Right/R3.png'),
                          pygame.image.load('Images/SpielerImages/Right/R4.png'),
                          pygame.image.load('Images/SpielerImages/Right/R5.png'),
                          pygame.image.load('Images/SpielerImages/Right/R6.png'),
                          pygame.image.load('Images/SpielerImages/Right/R7.png')]

        self.walkLeft = [pygame.image.load('Images/SpielerImages/Left/L0.png'),
                         pygame.image.load('Images/SpielerImages/Left/L1.png'),
                         pygame.image.load('Images/SpielerImages/Left/L2.png'),
                         pygame.image.load('Images/SpielerImages/Left/L3.png'),
                         pygame.image.load('Images/SpielerImages/Left/L4.png'),
                         pygame.image.load('Images/SpielerImages/Left/L5.png'),
                         pygame.image.load('Images/SpielerImages/Left/L6.png'),
                         pygame.image.load('Images/SpielerImages/Left/L7.png')]

        self.standing = pygame.image.load('Images/SpielerImages/standing.png')
