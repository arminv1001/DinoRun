from abc import abstractmethod

import pygame

from World import World

class GamePage:

    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.DIFFICULTY = DIFFICULTY

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.run = True
        self.clock = pygame.time.Clock()
        self.font = "LEMONCHI.ttf"
        self.backgroundWorld = World(self.WIDTH, self.HEIGHT, self.DIFFICULTY)

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)


    def textFormat(self, message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText


    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def loop(self):
        pass
