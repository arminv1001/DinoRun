import pygame
import logging
from GamePage import GamePage
from HighScoreDB import HighScoreDB


class GameEndClass(GamePage):
    """
    Klasse für die letzte Seite.
    Die letzte Seite beinhaltet ein Eingabefeld und die Bestenliste.
    """

    def __init__(self, WIDTH, HEIGHT):
        """
        Konstruktor der letzten Seite
        :param WIDTH: Breite des Fensters
        :param HEIGHT: Höhe des Fensters
        """
        super().__init__(WIDTH, HEIGHT)
        self.scoreInsert = False
        self.gameFont = pygame.font.Font(self.font, 20)
        self.mouseHover = False
        self.highscoreDB = HighScoreDB()
        self.highscoreDBContent = self.highscoreDB.returnHighscoreList()

    def printTitle(self, text, heightText, fontSize):
        """
        Zeigt einen Text auf der GUI an
        :param text: String der angezeigt werden soll
        :param heightText: Höhe des Textes
        :param fontSize: Schriftgröße
        :test:
            - Wird der Text auf der GUI angezeigt?
            - Stimmt die Größe des Textes?
        """
        textFormat = self.textFormat(text, self.font, fontSize, self.black)
        textRect = textFormat.get_rect()
        self.win.blit(textFormat, ((self.WIDTH / 2 - textRect[2] / 2), heightText))

    def highscoreRowPrint(self, username, score, index):
        """
        Erstellt eine Zeile für die Visualisierung der Highscore Liste
        :param username: Username aus der DB
        :param score: Score aus der DB
        :param index: Platzierung
        :test:
            - Wird der Text richtig konkateniert?
            - Wird der Text auf der GUI angezeigt?
        """
        text = str(index + 1).ljust(10) + username.ljust(20)
        text += score
        textScore = self.textFormat(text, self.font, 30, self.black)
        textRect = textScore.get_rect()
        self.win.blit(textScore, ((self.WIDTH / 2 - textRect[2] / 2), (index + 1) * 50 + 200))

    def draw(self):
        """
        Zuständig für das Zeichnen aller grafischen Objekte
        :test:
            - Werden alle Elemente angezeigt?
            - Werde die richtigen Score-Einträge angezeigt?
        """
        # self.backgroundWorld.placeBackground(self.win)
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background1X, 0))
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background2X, 0))

        if self.mouseHover:
            textStart = self.textFormat("RESTART", self.font, 75, self.black)
        else:
            textStart = self.textFormat("RESTART", self.font, 75, self.white)

        startRect = textStart.get_rect()
        koord = (self.WIDTH / 2 - (startRect[2] / 2), 400)
        self.startRect = startRect.move(koord)
        self.win.blit(textStart, koord)

        textSurface = self.textFormat(self.userText, self.font, 30, self.black)
        surfaceRect = textSurface.get_rect()
        self.win.blit(textSurface, (self.WIDTH / 2 - (surfaceRect[2] / 2), 200))

        self.printTitle("Game Over", 10, 75)
        self.printTitle("Highscore:", 100, 50)

        dbEntries = len(self.highscoreDBContent)
        if dbEntries > 3:
            dbEntries = 3
        for index in range(0, dbEntries):
            self.highscoreRowPrint(self.highscoreDBContent[index][1], str(self.highscoreDBContent[index][2]), index)

        pygame.draw.rect(self.win, self.black, (self.WIDTH / 2 - 200, 200, 400, 40), 2)
        pygame.display.update()

    def loop(self, score):
        # TODO Logging - Fehler
        """
        Diese Funktion managt:
            -das Game-Over-Bild
            -die Eingabe des Namens (https://www.youtube.com/watch?v=Rvcyf4HsWiw&t=608s)

        :param score: Anzahl der Münzen, die der User eingesammlet hat
        :return: Ob User das Fenster geschlossen hat oder nicht
        :test:
            - Text überschreitet nicht die größe 20
            - Funktion gibt den Rückgabewert True zurück, wenn der Restart Button betätigt
        """
        self.userText = ""
        while True:
            self.draw()
            for event in pygame.event.get():
                xMouse, yMouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    logging.info("Fenster geschlossen")
                    return False
                if self.startRect.collidepoint(xMouse, yMouse):
                    self.mouseHover = True
                else:
                    self.mouseHover = False
                if event.type == pygame.MOUSEBUTTONUP and self.mouseHover:
                    logging.info("Restart")
                    self.scoreInsert = False
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.userText = self.userText[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(self.userText) > 20:
                            logging.error("Text größer als 20!")
                        elif len(self.userText) > 0 and self.scoreInsert == False:
                            self.scoreInsert = True
                            self.highscoreDB.insertScore(self.userText, score)
                            self.highscoreDBContent = self.highscoreDB.returnHighscoreList()
                        elif self.scoreInsert == True:
                            logging.error("Score wurde schon in der DB gespeichert")
                        else:
                            logging.error("Wort hat die Länge 0")
                    else:
                        if (len(self.userText) < 20):
                            self.userText += event.unicode
                pygame.display.flip()
                self.clock.tick(60)
