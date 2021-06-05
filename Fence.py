import pygame

from GameObject import GameObject


class Fence(GameObject):
    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        """
        Konstruktor für die Klasse Fence - erstellt einen Zaun, über den der Spieler
        hnüber springen  soll
        :param WIDTH: Breite des Fensters
        :param HEIGHT: Höhe des Fensters
        :param DIFFICULTY: Schwierigkeitsgrad des Spiels
        """
        widthObj = int(WIDTH / 10)
        heightObj = int(HEIGHT / 10)
        fenceImage = self.loadImage(widthObj, heightObj)
        Y = (HEIGHT * (1 / 2) + heightObj)+70
        super().__init__(WIDTH, HEIGHT, DIFFICULTY, fenceImage, widthObj, heightObj, Y)

    @staticmethod
    def loadImage(widthObj, heightObj):
        """
        Läd das Bild für den Zaun
        :param widthObj: Breite des Bilds
        :param heightObj: Höhe des Bilds
        :return: Fence Bild
        :test:
            - Ist das Bild vorhanden?
            - Wurde das Bild geladen?
        """
        fenceImage = pygame.image.load("images/Objekte/fence.png")
        fenceImage = pygame.transform.scale(fenceImage, (widthObj, heightObj))
        return fenceImage





