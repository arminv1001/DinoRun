import pygame
from World import World

def drawGame(window):
    backgroundWorld.placeBackground(window)
    window.blit(backgroundWorld.background, (backgroundWorld.background1X, 0))
    window.blit(backgroundWorld.background, (backgroundWorld.background2X, 0))
    pygame.display.update()

pygame.init()

HEIGHT = 500
WIDTH = 800
DIFFICULTY = 2

win = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
clock = pygame.time.Clock()
#Hintergrund laden
backgroundWorld = World(WIDTH,HEIGHT,DIFFICULTY)

while run:
    # bestimmt die Frames per second
    clock.tick(60)

    #Background
    drawGame(win)
    # Auf die angaben des Benutzers reagieren
    for event in pygame.event.get():

        # Fenster schließen
        if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
pygame.quit()
