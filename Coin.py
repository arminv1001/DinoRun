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
        :test:
            - ist Bild vorhanden
            - wurde Bild geladen
        """
        coinImage = pygame.image.load('Images/Objekte/coin.png')
        coinImage = pygame.transform.scale(coinImage, (40, 40))
        return coinImage

    def removeCoin(self):
        """
        Die X-Koordinate wird zurückgesetzt

        test:
            - wird der Coin außerhalb des Fensters platziert
        """
        self.X = self.ResetX

    def place(self,window,fence):
        """
        Fügt den Coin zum Spielfenster hinzu. Coin darf nicht in einem Zaun platziert werden.
        :param window: Pygame Fenster
        :param fence: Zaun
        :test:
            - Wurde der Coin platziert?
            - Liegt der Coin in einem Zaun?
        """
        if not fence.spawn:
            self.randomSpawn()
        if self.spawn:
            window.blit(self.image, (self.X, self.Y))
            self.X -= 1 * self.difficulty
            self.drawHitbox(window)
            if self.X <= -self.widthObj:
                self.spawn = False
                self.X = self.widthFrame + 10
        if fence.hitbox.colliderect(self.hitbox):
            self.X = self.ResetX

