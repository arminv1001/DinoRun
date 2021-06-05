import pygame
from GameObject import GameObject

class FlyingEnemy(GameObject):
    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        """
        Konstruktor für FlyingEnemy. Erstellt einen Gegner, welcher fliegt und Spieler unten durch muss.
        :param WIDTH: Breite des Fensters
        :param HEIGHT: Höhe des Fensters
        :param DIFFICULTY: Schwierigkeitsgrad des Spiels
        """
        widthObj = 60
        heightObj = 70
        flyImage = self.loadImage(widthObj, heightObj)
        Y = HEIGHT - 240

        super().__init__(WIDTH, HEIGHT, DIFFICULTY, flyImage, widthObj, heightObj, Y)

    @staticmethod
    def loadImage(widthObj, heightObj):
        """
        Läd das Bild für den fliegenden Gegner
        :return: FlyingEnemy Bild
        :test:
            - ist Bild vorhanden
            - wurde Bild geladen
        """
        flyImage = pygame.image.load("images/Objekte/flyMan_fly.png")
        flyImage = pygame.transform.scale(flyImage, (widthObj, heightObj))
        return flyImage

    def place(self, window):
        """
        Der Gegner wird platziert. Funktion muss überschrieben werden,
        weil er eine höhere Geschweindigkeit hat als alle anderen Objekte
        :param window: Pygame Fenster
        :test:
            - Wurde der Gegner platziert?
            - fliegt er schneller als sich das Bild bewegt?
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.image, (self.X, self.Y))
            self.X -= 1 * self.difficulty * 2
            self.drawHitbox(window)
            if self.X <= -self.widthObj:
                self.spawn = False
                self.X = self.ResetX
