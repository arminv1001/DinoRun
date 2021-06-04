import pygame

from GamePage import GamePage
from World import World


class GameIntroClass(GamePage):
    """
    Klasse für die erste Seite des Spiels.
    """
    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        """
        Konstruktor fuer die erste Seite.
        :param WIDTH: Breite des Fensters
        :param HEIGHT: Höhe des Fensters
        :param DIFFICULTY: Schwierigkeitsgrad des Spiels
        """
        super().__init__(WIDTH, HEIGHT, DIFFICULTY)

        self.mouseHover = False


    def draw(self):
        """
        Funktion zeichnet alle grafischen Objekte der ersten Seite.
        """
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background1X, 0))
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background2X, 0))

        if self.mouseHover:
            textStart = self.textFormat("START", self.font, 75, self.black)
        else:
            textStart = self.textFormat("START", self.font, 75, self.white)

        startRect = textStart.get_rect()
        koord = (self.WIDTH / 2 - (startRect[2] / 2), 300)
        self.startRect = startRect.move(koord)
        self.win.blit(textStart, koord)

        textTitle = self.textFormat("Emmas Adventure", self.font, 75, self.black)
        titleRect = textTitle.get_rect()
        self.win.blit(textTitle, (self.WIDTH / 2 - (titleRect[2] / 2), 50))

        pygame.display.update()


    def loop(self):
        """
        Spielschleife, reagiert auf eingaben und ruft die draw()-Funktion auf.
        """
        while True:
            self.draw()
            for event in pygame.event.get():
                xMouse, yMouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    return False
                if self.startRect.collidepoint(xMouse, yMouse):
                    self.mouseHover = True
                else:
                    self.mouseHover = False
                if event.type == pygame.MOUSEBUTTONUP and self.mouseHover:
                    return True
