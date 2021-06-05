import pygame

# todo Kommentare
# todo Test
# todo Readme
# todo Logs
# todo Requirements
# todo Ordner Struktur


from GameEndClass import GameEndClass
from GamePlayClass import GamePlayClass
from GameIntroClass import GameIntroClass
import logging

if __name__ == "__main__":

    # Konstanten
    HEIGHT = 500
    WIDTH = 800
    DIFFICULTY = 2

    pygame.init()
    pygame.mixer.music.load("Sounds/theme_music.wav")
    # Musik auskommentieren wenn nicht erwünscht
    pygame.mixer.music.play(-1)
    logging.basicConfig(level=logging.INFO, filename='LogFile/sentiment_scrapper_log.txt', format='%(levelname)s - %(message)s')
    # Objekte instanziieren
    logging.info("----------------------------")
    logging.info("GUI Start")
    gameIntro = GameIntroClass(WIDTH, HEIGHT)
    gamePlay = GamePlayClass(WIDTH, HEIGHT, DIFFICULTY)
    gameEnd = GameEndClass(WIDTH, HEIGHT)

    # Spielschleife
    run = gameIntro.loop()
    while run:
        run, score = gamePlay.loop()
        if run:
            run = gameEnd.loop(score)

    pygame.quit()
    gameEnd.highscoreDB.conn.close()
