import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
run = True

while run:
    # bestimmt die Frames per second
    pygame.time.delay(100)

    # Auf die angaben des Benutzers reagieren
    for event in pygame.event.get():

        # Fenster schließen
        if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
pygame.quit()
