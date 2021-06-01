import pygame

from World import World
from pygame.locals import *


def gameIntro(WIDTH, HEIGHT, DIFFICULTY):
    """
    Konstanten 
    """
    global mouseHover
    mouseHover = False
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    clock = pygame.time.Clock()
    font = "LEMONCHI.ttf"

    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    backgroundWorld = World(WIDTH, HEIGHT, DIFFICULTY)

    def textFormat(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    def draw():
        backgroundWorld.placeBackground(win)
        win.blit(backgroundWorld.background, (backgroundWorld.background1X, 0))
        win.blit(backgroundWorld.background, (backgroundWorld.background2X, 0))

        if mouseHover:
            textStart = textFormat("START", font, 75, black)
        else:
            textStart = textFormat("START", font, 75, white)

        startRect = textStart.get_rect()
        koord = (WIDTH / 2 - (startRect[2] / 2), 300)
        startRect = startRect.move(koord)
        win.blit(textStart, koord)

        textTitle = textFormat("Emmas Adventure", font, 75, black)
        titleRect = textTitle.get_rect()
        win.blit(textTitle, (WIDTH / 2 - (titleRect[2] / 2), 50))

        pygame.display.update()
        return startRect

    """
    Loop
    """

    while run:
        startRect = draw()
        for event in pygame.event.get():
            xMouse, yMouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if startRect.collidepoint(xMouse, yMouse):
                mouseHover = True
            else:
                mouseHover = False
            if event.type == pygame.MOUSEBUTTONUP and mouseHover:
                run = False
