import pygame

from GameEndClass import GameEndClass
from GamePlayClass import GamePlayClass
from GameIntroClass import  GameIntroClass

if __name__ == "__main__":

    HEIGHT = 500
    WIDTH = 800
    DIFFICULTY = 2

    pygame.init()


    #gameIntro(WIDTH, HEIGHT)
    gameIntro = GameIntroClass(WIDTH, HEIGHT, DIFFICULTY)
    gamePlay = GamePlayClass(WIDTH, HEIGHT, DIFFICULTY)
    gameEnd = GameEndClass(WIDTH, HEIGHT, DIFFICULTY)

    run = gameIntro.loop()

    while run:
            run =  gamePlay.loop()
            if run:
                run = gameEnd.loop()

    pygame.quit()



    #gameloop(WIDTH, HEIGHT, DIFFICULTY)


