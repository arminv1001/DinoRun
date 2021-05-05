import pygame
from World import World

pygame.init()

HEIGHT = 500
WIDTH = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
clock = pygame.time.Clock()
#Hintergrund laden
# TODO Schwierigkeit mit der Zeit erhöhen oder am anfang aushwälen?
backgroundWorld = World(WIDTH,HEIGHT,1)

while run:
    # TODO pygame.time.delay(60) brauchst du das??? -> wenn ja dann probiers mal mit dem clock tick,
    #  weil glaub des war die falsche Funktion die du da verwendet hast
    # bestimmt die Frames per second
    # clock.tick(60)

    #Background
    backgroundWorld.placeBackground(win)
    # Auf die angaben des Benutzers reagieren
    for event in pygame.event.get():

        # Fenster schließen
        if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
pygame.quit()
