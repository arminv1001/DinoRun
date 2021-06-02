import pygame

from Coin import Coin
from Fence import Fence
from FlyingEnemy import FlyingEnemy
from GamePage import GamePage
from Player import Player


class GamePlayClass(GamePage):
    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        super().__init__(WIDTH, HEIGHT, DIFFICULTY)

        self.valScore = str(0)

        self.man = Player(WIDTH / 2, HEIGHT - 150, step=4, difficulty=DIFFICULTY)
        self.fence = Fence(WIDTH, HEIGHT, DIFFICULTY)
        self.coin = Coin(WIDTH, HEIGHT, DIFFICULTY)
        self.flyingEnemy = FlyingEnemy(WIDTH, HEIGHT, DIFFICULTY)

        self.objects = [self.fence, self.flyingEnemy, self.coin]

    def collision(self):
        for obj in self.objects:
            if self.man.checkCollision(obj.hitbox):
                if isinstance(obj, Coin):
                    self.valScore = int(self.valScore)
                    self.valScore += 1
                    self.coin.removeCoin()
                    return False
                return True
        return False



    def resetObj(self):
        for obj in self.objects:
            obj.X = obj.ResetX


    def draw(self):
        self.backgroundWorld.placeBackground(self.win)
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background1X, 0))
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background2X, 0))

        score = self.textFormat(str(self.valScore), self.font, 50, self.white)
        scoreRect = score.get_rect()
        self.win.blit(score, (self.WIDTH - (scoreRect[2] + 10), 30))

        self.fence.place(self.win)
        self.flyingEnemy.place(self.win)
        self.coin.place(self.win)
        self.man.draw(self.win)
        self.man.drawHitbox(self.win)
        pygame.display.update()

    def loop(self):
        self.clock.tick(60)

        # Background
        for event in pygame.event.get():
            # Fenster schließen
            if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                self.gameBool = False  # Ends the game loop

        # Key Steuerung Player
        # TODO eventuel auslagern
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.man.left = True
            self.man.right = False
        elif keys[pygame.K_RIGHT] and self.man.x < self.WIDTH:
            self.man.right = True
            self.man.left = False
        else:
            self.man.right = False
            self.man.left = False

        if keys[pygame.K_DOWN]:
            self.man.down = True
        else:
            self.man.down = False

        if not self.man.jump:
            if keys[pygame.K_SPACE]:
                self.man.jump = True

        self.man.move()
        self.draw()

        #TODO Collisions handling
        collBool = self.collision()

        if collBool:
            self.gameBool = False
            self.resetObj()
            self.man.x = self.man.maxX / 2


