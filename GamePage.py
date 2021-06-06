from abc import abstractmethod

import pygame

from World import World

class GamePage:
    """
    Superklasse für alle Spielseiten (GameIntro, GameEnd, GamePlay)
    Enthält die abstrakten Methoden draw() und loop() die von den Kindklassen implementiert werden müssen.
    """

    def __init__(self, WIDTH, HEIGHT):
        """
        Konstruktor:
        :param WIDTH:
        :param HEIGHT:
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.run = True
        self.clock = pygame.time.Clock()
        self.font = "Font/LEMONCHI.ttf"
        self.backgroundWorld = World(self.WIDTH, self.HEIGHT, 2)

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)


    def textFormat(self, message, textFont, textSize, textColor):
        """
        Funktion, um ein Text zu erzeugen um dieses Später im Spiel darzustellen.
        :param message: Inhalt des Textes
        :param textFont: Schriftart
        :param textSize: Schriftgroeße
        :param textColor:  Schrftfarbe
        :return: Textobjekt
        :test:
            - Rückgabewert ist nicht leer
            - Rückgabewert hat den richtigen Datentyp
        """
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText


    @abstractmethod
    def draw(self):
        """
        Abstrakte Methode. Stellt die Objekte bei jedem Frame im Fenster dar.
        """
        pass

    @abstractmethod
    def loop(self):
        """
        Abstrakte Methode. Spielschleife.
        """
        pass
