import pygame

# todo Kommentare
# todo Test
# todo Readme
# todo requirement
# TODO Difficulty in abhänigkeit von der Ges

from GameEndClass import GameEndClass
from GamePlayClass import GamePlayClass
from GameIntroClass import  GameIntroClass

if __name__ == "__main__":

    # Konstanten
    HEIGHT = 500
    WIDTH = 800
    DIFFICULTY = 2

    pygame.init()
    pygame.mixer.music.load("Sounds/theme_music.wav")
    # Musik auskommentieren wenn nicht erwünscht
    pygame.mixer.music.play(-1)

    #Objekte instanziieren
    gameIntro = GameIntroClass(WIDTH, HEIGHT, DIFFICULTY)
    gamePlay = GamePlayClass(WIDTH, HEIGHT, DIFFICULTY)
    gameEnd = GameEndClass(WIDTH, HEIGHT, DIFFICULTY)

    # Spielschleife
    run = gameIntro.loop()

    while run:
            run,score =  gamePlay.loop()
            if run:
                run = gameEnd.loop(score)

    pygame.quit()
    gameEnd.highscoreDB.conn.close()


