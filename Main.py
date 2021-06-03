import pygame

from GameEndClass import GameEndClass
from GamePlayClass import GamePlayClass
from GameIntroClass import  GameIntroClass

if __name__ == "__main__":

    HEIGHT = 500
    WIDTH = 800
    DIFFICULTY = 2

    pygame.init()
    pygame.mixer.music.load("Sounds/theme_music.wav")
    # TODO Finn hier auskommentieren wenn kein bock auf Musik
    pygame.mixer.music.play(-1)

    #gameIntro(WIDTH, HEIGHT)
    gameIntro = GameIntroClass(WIDTH, HEIGHT, DIFFICULTY)
    gamePlay = GamePlayClass(WIDTH, HEIGHT, DIFFICULTY)
    gameEnd = GameEndClass(WIDTH, HEIGHT, DIFFICULTY)

    run = gameIntro.loop()

    while run:
            run,score =  gamePlay.loop()
            if run:
                run = gameEnd.loop(score)

    pygame.quit()



    #gameloop(WIDTH, HEIGHT, DIFFICULTY)


