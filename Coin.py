import random

import pygame
from GameObject import GameObject


class Coin(GameObject):
    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        """
        Konstruktor für Coin. Erstellt eine Münze, welche von dem Spieler eingesammlt werden kann.
        :param WIDTH: Breite des Fensters
        :param HEIGHT: Höhe des Fensters
        :param DIFFICULTY: Schwierigkeitsgrad des Spiels
        """
        widthObj = 40
        heightObj = 40
        coinImage = self.loadImage()
        Y = 370

        super().__init__(WIDTH, HEIGHT, DIFFICULTY, coinImage, widthObj, heightObj, Y)

    @staticmethod
    def loadImage():
        """
        Läd das Bild für den Coin
        :return: Coin Bild
        """
        coinImage = pygame.image.load('Images/Objekte/coin.png')
        coinImage = pygame.transform.scale(coinImage, (40, 40))
        return coinImage

    def removeCoin(self):
        """
        Die X-Koordinate wird zurückgesetzt
        """
        self.X = self.ResetX

    def randomSpawn(self):
        """
        #todo rs
        """
        if not self.spawn:
            self.spawn = random.random() > 0.99

    def place(self,window,fence):
        """
        Fügt die Objekte zum Spielfenster hinzu.
        :param window: Pygame Fenster
        """
        if fence.spawn == False or fence.X < self.widthFrame/2:
            self.randomSpawn()
        if self.spawn:
            window.blit(self.image, (self.X, self.Y))
            self.X -= 1 * self.difficulty
            self.drawHitbox(window)
            if self.X <= -self.widthObj:
                self.spawn = False
                self.X = self.widthFrame + 10

