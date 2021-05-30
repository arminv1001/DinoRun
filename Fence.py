import random
import pygame

from GameObject import GameObject


class Fence(GameObject):
    def __init__(self, WIDTH, HEIGHT, difficulty):
        super().__init__(WIDTH, HEIGHT, difficulty)
        self.width = int(WIDTH / 7)
        self.height = int(HEIGHT / 7)
        self.hillPic = pygame.image.load("images/Objekte/fence.png")
        self.hillPic = pygame.transform.scale(self.hillPic, (self.width, self.height))
        self.spawn = False
        self.ResetX = WIDTH + self.width + 10
        super().setX(self.ResetX)
        super().setY((HEIGHT * (1 / 2) + self.height) + 30)
        self.difficulty = difficulty
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)




    def placeFence(self, window):
        """
        :param window: Pygame Fenster
        :return: -
        """
        self.randomSpawn()
        if self.spawn:
            window.blit(self.hillPic, (self.X, self.Y))
            self.X -= 1 * self.difficulty
            self.drawHitbox(window)
            if self.X <= -self.width:
                self.spawn = False
                self.X = self.ResetX

