import pygame
# todo max Slide

class Player:
    """
    Klasse für die Protagonistin.
    """

    def __init__(self, x, y, step, difficulty):
        """
        Konstruktor
        :param x: x-Koordinate
        :param y: y-Koordinate
        :param step:
        :param difficulty: Spielgeschwindigkeit
        """
        self.jumpDistance = 2
        self.x = x - 48
        self.y = y - 64
        self.yConst = self.y
        self.step = step
        self.difficulty = difficulty
        self.jumpHight = 8
        self.left = False
        self.right = False
        self.walkIndex = 0
        self.jumpIndex = self.jumpHight
        self.jump = False
        self.down = False
        self.dead = False
        self.deadEnd = False
        self.loadImage()
        self.rect = pygame.Rect(self.x, self.y, 96, 128)
        self.maxX = 700

        self.DEBUG = False

    def move(self):
        """
        Bewegungssteuerung
        :test:
            - walkIndex hat den richtigen Wert angenommen, wenn der Spieler sich nach Links bewegt
            - Das Attribut X hat den richtigen Wert angenommen, während der Spieler sich nicht bewegt hat
        """
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

        # Sprung
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
        # Tot-Animation
        if self.dead:
            if self.y >= 490:
                self.deadEnd = True
            elif self.y <= 500:
                self.y += 5

        else:
            if self.x >= 0:
                self.x -= self.difficulty

    def draw(self, window):
        """
        Protagonistin neu zeichen.
        :param window: Spielfenster
        :test:  - Werden die Booleanwerte richtig verarbeitet.
                -  Die richtigen Bilder werden zu der passenden Bewegung geladen.
        """
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
                window.blit(self.walkRight[self.walkIndex // 6], (self.x, self.y))
        else:
            if self.down:
                window.blit(self.downStanding, (self.x, self.y))
            else:
                window.blit(self.standing, (self.x, self.y))

    def loadImage(self):
        """
        Bilder für die Protagonistin laden.
        Bildgroeße: 96x128
        :test:
            - wurden die Richtigen Bilder geladen
            - besitzen die Attribute den Richtigen Datentyp
        """
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
        self.downStanding = pygame.image.load('Images/SpielerImages/down/down.png')

    def drawHitbox(self, window):
        """
        Die Hitbox um den Player wird erstellt
        :param window: Fenster - GUI
        :test:
            - Hitbox wird verkleinert, wenn Spieler sicht duckt
            - Hitbox hat die richtige Größe
        """
        playerDownDiv = 1
        playerDownHigh = 0
        if self.down:
            playerDownDiv = 2
            playerDownHigh = 100 / 2
        self.rect = pygame.Rect(self.x + 10, self.y + 20 + playerDownHigh, 80, 110 / playerDownDiv - 15)
        if self.DEBUG:
            pygame.draw.rect(window, (255, 0, 0), self.rect, 2)

    def checkCollision(self, objRect):
        """
        Es wird vergliechen ob die Hitbox des Spielers die Hitbox eines Objektes schneidet
        :param objRect: Objekt vom Typ GomeObject
        :return: Wenn beide miteinander Kollidieren wird ein boolescher Wert zurückgegeben. True - Kollision
        :test:
            - Richtiger Rückgabewert?
            - Kolliosionserkennung funktioniert?
        """
        return self.rect.colliderect(objRect)
