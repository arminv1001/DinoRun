import pygame
from World import World
from Player import Player

pygame.init()

'''
Konstanten definieren 
'''

HEIGHT = 500
WIDTH = 800
DIFFICULTY = 2

win = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
clock = pygame.time.Clock()

# Hintergrund laden
# Fußboden bei 350
backgroundWorld = World(WIDTH, HEIGHT, DIFFICULTY)
man = Player(WIDTH / 2, HEIGHT - 150, DIFFICULTY, DIFFICULTY)

'''
Gameloop Funktionen
'''


def drawGame(window):
    backgroundWorld.placeBackground(window)
    window.blit(backgroundWorld.background, (backgroundWorld.background1X, 0))
    window.blit(backgroundWorld.background, (backgroundWorld.background2X, 0))
    man.draw(window)
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

    drawGame(win)


pygame.quit()
