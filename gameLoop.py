import random

import pygame

from Coin import Coin
from World import World
from Player import Player
from Fence import Fence
from FlyingEnemy import FlyingEnemy
from gameEnd import gameEnde


def gameloop(WIDTH, HEIGHT, DIFFICULTY):
    '''
    Konstanten definieren 
    '''

    valScore = str(0)

    win = pygame.display.set_mode((WIDTH, HEIGHT))

    run = True
    clock = pygame.time.Clock()

    font = "LEMONCHI.ttf"
    white = (255, 255, 255)

    # Hintergrund laden
    # Fußboden bei 350
    backgroundWorld = World(WIDTH, HEIGHT, DIFFICULTY)
    man = Player(WIDTH / 2, HEIGHT - 150, step=4, difficulty=DIFFICULTY)
    fence = Fence(WIDTH, HEIGHT, DIFFICULTY)
    coin = Coin(WIDTH, HEIGHT, DIFFICULTY)
    flyingEnemy = FlyingEnemy(WIDTH, HEIGHT, DIFFICULTY)

    # TODO dynamische Erstellung von Objekten
    objects = [fence, flyingEnemy, coin]

    '''
    Gameloop Funktionen
    '''
    def resetObj(objects):
        for obj in objects:
            obj.X = obj.ResetX


    def textFormat(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    def testCollision(objects, man, valScore):
        for obj in objects:
            if man.checkCollision(obj.hitbox):
                if isinstance(obj, Coin):
                    print("Coin")
                    valScore = int(valScore)
                    valScore += 1
                    coin.removeCoin()
                    return False, valScore
                return True, valScore
        return False, valScore

    def drawGame(window, valScore):
        backgroundWorld.placeBackground(window)
        window.blit(backgroundWorld.background, (backgroundWorld.background1X, 0))
        window.blit(backgroundWorld.background, (backgroundWorld.background2X, 0))

        score = textFormat(str(valScore), font, 50, white)
        scoreRect = score.get_rect()
        window.blit(score, (WIDTH - (scoreRect[2] + 10), 30))

        fence.place(window)
        flyingEnemy.place(window)
        coin.place(window)
        man.draw(window)
        man.drawHitbox(window)

        pygame.display.update()

    '''
    Gameloop 
    '''
    while run:
        # bestimmt die Frames per second
        clock.tick(60)

        # Background
        for event in pygame.event.get():
            # Fenster schließen
            if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop

        # Key Steuerung Player
        # TODO eventuel auslagern
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            man.left = True
            man.right = False
        elif keys[pygame.K_RIGHT] and man.x < WIDTH:
            man.right = True
            man.left = False
        else:
            man.right = False
            man.left = False

        if keys[pygame.K_DOWN]:
            man.down = True
        else:
            man.down = False

        if not man.jump:
            if keys[pygame.K_SPACE]:
                man.jump = True

        man.move()

        # TODO Collisions handling
        collBool, valScore = testCollision(objects, man, valScore)

        if collBool:
            reset = gameEnde(HEIGHT, WIDTH, win, font)
            if reset:
                resetObj(objects)
                man.x = man.maxX/2
            else:
                run = False
        drawGame(win, valScore)


    pygame.quit()
