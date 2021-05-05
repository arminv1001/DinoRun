import pygame
from World import World

pygame.init()

HEIGHT = 500
WIDTH = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

#Hintergrund laden
backgroundWorld = World(WIDTH,HEIGHT)

while run:
    # bestimmt die Frames per second
    pygame.time.delay(60)

    #Background
    backgroundWorld.placeBackground(win)
    # Auf die angaben des Benutzers reagieren
    for event in pygame.event.get():

        # Fenster schließen
        if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
pygame.quit()
