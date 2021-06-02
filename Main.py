import pygame

from GameEndClass import GameEndClass
from GamePlayClass import GamePlayClass
from GameIntroClass import  GameIntroClass

if __name__ == "__main__":

    HEIGHT = 500
    WIDTH = 800
    DIFFICULTY = 2

    pygame.init()
    run = True

    #gameIntro(WIDTH, HEIGHT)
    gameIntro = GameIntroClass(WIDTH, HEIGHT, DIFFICULTY)
    gamePlay = GamePlayClass(WIDTH, HEIGHT, DIFFICULTY)
    gameEnd = GameEndClass(WIDTH, HEIGHT, DIFFICULTY)

    gameIntro.setGameBool(True)

    while run:
        if gameIntro.gameBool:
            gameIntro.loop()
            gamePlay.setGameBool(not gameIntro.gameBool)
        elif gamePlay.gameBool:
            gamePlay.loop()
            gameEnd.setGameBool(not gamePlay.gameBool)
        elif gameEnd.gameBool:
            gameEnd.loop()
            gamePlay.setGameBool(not gameEnd.gameBool)
        else:
            run = False

    pygame.quit()



    #gameloop(WIDTH, HEIGHT, DIFFICULTY)


