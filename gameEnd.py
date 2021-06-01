import pygame
from gameIntro import textFormat


def gameEnde(HEIGHT, WIDTH, window, font):
    # Background
    mouseHover = False
    white = (255, 255, 255)
    black = (0, 0, 0)
    while True:

        if mouseHover:
            textRestart = textFormat("RESTART", font, 75, black)
        else:
            textRestart = textFormat("RESTART", font, 75, white)

        restartRect = textRestart.get_rect()
        koord = (WIDTH / 2 - (restartRect[2] / 2), 300)
        restartRect = restartRect.move(koord)
        window.blit(textRestart, koord)

        textGameOver = textFormat("GAME OVER", font, 75, black)
        rectGameOver = textGameOver.get_rect()
        window.blit(textGameOver, (WIDTH / 2 - (rectGameOver[2] / 2), 50))

        mouseHover = False

        for event in pygame.event.get():
            # Fenster schließen
            xMouse, yMouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                return False  # Ends the game loop
            if restartRect.collidepoint(xMouse, yMouse):
                mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and mouseHover:
                return True
        pygame.display.update()
