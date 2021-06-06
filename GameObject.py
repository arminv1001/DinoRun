import pygame
import random


class GameObject:
    """
    Superklasse für alle im Spiel vorhandenen Objekte.
    """
    def __init__(self, WIDTH, HEIGHT, difficulty, imageObj, widthObj, heightObj, Y):
        """
        Konstruktor
        :param WIDTH: Breite des Fensters:
        :param HEIGHT: Höhe des Fensters
        :param difficulty: Spielschwierigkeit.
        :param imageObj:  Bildobjekte
        :param widthObj:  Breite des Objektes
        :param heightObj:  Höhe des Objektes
        :param Y: y-Position des Objektes
        """
        self.widthFrame = WIDTH
        self.heightFrame = HEIGHT
        self.widthObj = widthObj
        self.heightObj = heightObj
        self.difficulty = difficulty
        self.Y = Y
        self.ResetX = WIDTH + self.widthObj + 10 + random.randint(10,1000)
        self.X = self.ResetX
        self.image = imageObj
        self.hitbox = pygame.Rect(self.X, self.Y, self.widthObj, self.heightObj)
        self.spawn = False

        self.DEBUG = False

    def randomSpawn(self):
        """
        Funktion setzt die Variable spawn mit einer Wahrscheinlichkeit von 0.01 auf True
        :test:
            - Statistische Untersuchung ob die Wahrscheinlichkeit mit einem Signifikanzniveau von 0.05 übereinstimmt.
            - Es wird der richtige Datentyp in die Variable spawn geschrieben
        """
        if not self.spawn:
            self.spawn = random.random() > 0.99

    def drawHitbox(self, window):
        """
        Erzeugt ein Rechteck um die Spielobjekte. Rechteck dient der Kollisionserkennung
        :param window: Pygame Fenster
        :test:
            - Richtiger Datentyp in die Variable hitbox geschrieben.
            - Parameter window ist nicht leer bzw. ungültig
        """
        self.hitbox = pygame.Rect(self.X, self.Y, self.widthObj, self.heightObj)
        if self.DEBUG:
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def place(self, window):
        """
        Fügt die Objekte zum Spielfenster hinzu.
        :param window: Pygame Fenster
        :test:
            - Parameter window enthält richtigen Datentyp bzw ist nicht leer.
            - Objekt wird nach dem durchlaufen zurückgesetzt
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.image, (self.X, self.Y))
            self.X -= 1 * self.difficulty
            self.drawHitbox(window)
            if self.X <= -self.widthObj:
                self.spawn = False
                self.X = self.ResetX
