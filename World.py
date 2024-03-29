import pygame


class World:

    def __init__(self, WIDTH, HEIGHT, difficulty):
        """
        Erstellt die Spielwelt, bzw den Hintergrund
        :param WIDTH:
        :param HEIGHT:
        :param difficulty:
        """
        self.background = pygame.image.load("images/Hintergrund/background.jpg")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.background1X = 0
        self.background2X = self.width
        self.difficulty = difficulty

    def placeBackground(self, window):
        """
        Erstellt eine unendlich lange Welt und sorgt dafür das die Kamera automatisch läuft.
        :param window: Pygame Fenster
        :return: -
        """
        self.background1X -= 1 * self.difficulty
        self.background2X -= 1 * self.difficulty
        if self.background1X <= (self.width * -1):
            self.background1X = self.width
        if self.background2X <= (self.width * -1):
            self.background2X = self.width
