import pygame

from gameLoop import gameloop
from gameIntro import gameIntro

if __name__ == "__main__":

    HEIGHT = 500
    WIDTH = 800
    DIFFICULTY = 2

    pygame.init()

    gameIntro(WIDTH, HEIGHT, DIFFICULTY)
    gameloop(WIDTH, HEIGHT, DIFFICULTY)
