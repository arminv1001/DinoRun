import pygame


class Player:

    def __init__(self, x, y, step, difficulty):
        self.jumpDistance = 2
        self.x = x - 48
        self.y = y - 64
        self.step = step
        self.difficulty = difficulty
        self.jumpHight = 8
        self.left = False
        self.right = False
        self.walkIndex = 0
        self.jumpIndex = self.jumpHight
        self.jump = False
        self.down = False
        self.loadImage()
        self.rect = pygame.Rect(self.x, self.y, 96, 128)
        self.maxX = 700

    def move(self):
        if self.walkIndex + 1 >= 42:
            self.walkIndex = 0

        if self.left:
            if self.x >= 0:
                self.x -= (self.step + self.difficulty)
                self.walkIndex += 1
        elif self.right:
            if self.x <= self.maxX:
                self.x += self.step
                self.walkIndex += 1

        # TODO Parameter für den Sprung einstellen
        if self.jump:
            if self.jumpIndex >= - self.jumpHight:
                self.y -= (self.jumpIndex * abs(self.jumpIndex)) * 0.5
                if self.right and self.x <= self.maxX:
                    self.x += self.step * self.jumpDistance
                elif self.left and self.x >= 0:
                    self.x -= self.step * self.jumpDistance
                self.jumpIndex -= 1

            else:
                self.jumpIndex = self.jumpHight
                self.jump = False

        else:
            if self.x >= 0:
                self.x -= self.difficulty

    def draw(self, window):
        if self.jump:
            if self.left:
                window.blit(self.jumpLeft[1], (self.x, self.y))
            else:
                window.blit(self.jumpRight[1], (self.x, self.y))
        elif self.left:
            if self.down:
                window.blit(self.downLeft, (self.x, self.y))
            else:
                window.blit(self.walkLeft[self.walkIndex // 6], (self.x, self.y))
        elif self.right:
            if self.down:
                window.blit(self.downRight, (self.x, self.y))
            else:
                # TODO muss besser
                window.blit(self.walkRight[self.walkIndex // 6], (self.x, self.y))
        else:
            window.blit(self.standing, (self.x, self.y))

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

        self.jumpLeft = [pygame.image.load('Images/SpielerImages/jump/jumpL.png'),
                         pygame.image.load('Images/SpielerImages/jump/fallL.png')]

        self.jumpRight = [pygame.image.load('Images/SpielerImages/jump/jumpR.png'),
                          pygame.image.load('Images/SpielerImages/jump/fallR.png')]

        self.downLeft = pygame.image.load('Images/SpielerImages/down/downL.png')
        self.downRight = pygame.image.load('Images/SpielerImages/down/downR.png')

    # TODO muss neu gemacht werden
    def drawHitbox(self, window):
        playerDownDiv = 1
        playerDownHigh = 0
        if self.down:
            playerDownDiv = 2
            playerDownHigh = 100 / 2
        self.rect = pygame.Rect(self.x , self.y + 20+ playerDownHigh, 96, 128 / playerDownDiv)
        pygame.draw.rect(window, (255, 0, 0), self.rect, 2)

    def checkCollision(self, objRect):
        if self.rect.colliderect(objRect):
            return True
        else:
            return False
