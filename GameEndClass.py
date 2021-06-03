import pygame

from GamePage import GamePage
from World import World
from HighScoreDB import HighScoreDB
from operator import itemgetter

class GameEndClass(GamePage):

    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        """
        :param WIDTH:
        :param HEIGHT:
        :param DIFFICULTY:
        """
        super().__init__(WIDTH, HEIGHT, DIFFICULTY)
        self.gameFont = pygame.font.Font(self.font,20)
        self.mouseHover = False
        self.highscoreDB = HighScoreDB()
        self.highscoreDBContent = self.highscoreDB.returnHighscoreList()



    def printTitle(self, text, heightText, fontSize):
        textFormat = self.textFormat(text, self.font, fontSize, self.black)
        textRect = textFormat.get_rect()
        self.win.blit(textFormat, ((self.WIDTH / 2 - textRect[2]/ 2), heightText))

    def highscoreRowPrint(self, username, score, index):
        text = str(index+1).ljust(10) + username.ljust(20)
        text += score
        textScore = self.textFormat(text,self.font,30,self.black)
        textRect = textScore.get_rect()
        self.win.blit(textScore,((self.WIDTH / 2 - textRect[2]/ 2), (index+1) * 50 + 200))

    def draw(self):
        #self.backgroundWorld.placeBackground(self.win)
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

        self.printTitle("Game Over", 10, 75)
        self.printTitle("Highscore:", 100, 50)
        dbEntries = len(self.highscoreDBContent)
        if dbEntries > 3:
            dbEntries = 3
        for index in range(0,dbEntries):
            self.highscoreRowPrint(self.highscoreDBContent[index][1],str(self.highscoreDBContent[index][2]),index)

        pygame.draw.rect(self.win, self.black,(self.WIDTH/2 - 200, 200, 400,40),2)
        pygame.display.update()


    def loop(self,score):
        user_text = ""
        while True:
            self.draw()
            for event in pygame.event.get():
                xMouse, yMouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if self.startRect.collidepoint(xMouse, yMouse):
                    self.mouseHover = True
                else:
                    self.mouseHover = False
                if event.type == pygame.MOUSEBUTTONUP and self.mouseHover:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text += user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        print("ENTER")
                        self.highscoreDB.insertScore(user_text,score)
                        self.highscoreDBContent = self.highscoreDB.returnHighscoreList()
                        # TODO Upload DB
                    else:
                        if (len(user_text) < 20):
                            user_text += event.unicode

                text_surface = self.gameFont.render(user_text,True,self.black)
                self.win.blit(text_surface,(self.WIDTH/2 - 120,205))

                pygame.display.flip()
                self.clock.tick(60)