import pygame

from Coin import Coin
from Fence import Fence
from FlyingEnemy import FlyingEnemy
from GamePage import GamePage
from Player import Player

# todo spawn

class GamePlayClass(GamePage):
    """
    Klasse für das Spielfenster.
    """
    def __init__(self, WIDTH, HEIGHT, DIFFICULTY):
        """
        Konstruktor
        :param WIDTH: Breite des Fensters
        :param HEIGHT: Höhe des Fensters
        :param DIFFICULTY: Schwierigkeitsgrad des Spiels
        """
        super().__init__(WIDTH, HEIGHT, DIFFICULTY)

        self.valScore = str(0)

        self.man = Player(WIDTH / 2, HEIGHT - 150, step=4, difficulty=DIFFICULTY)
        self.fence = Fence(WIDTH, HEIGHT, DIFFICULTY)
        self.coin = Coin(WIDTH, HEIGHT, DIFFICULTY)
        self.flyingEnemy = FlyingEnemy(WIDTH, HEIGHT, DIFFICULTY)

        self.objects = [self.fence, self.flyingEnemy, self.coin]

    def collision(self):
        """
        Händelt die Kollision zwischen dem Player und einem Spielobjekt.

        """
        for obj in self.objects:
            if self.man.checkCollision(obj.hitbox):
                if isinstance(obj, Coin):
                    pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds/CoinCollect.wav"))
                    self.valScore = int(self.valScore)
                    self.valScore += 1
                    self.coin.removeCoin()
                    return False
                return True
        return False



    def resetObj(self):
        """
        Bei einem Neustart des Spiels, müssen alle Objekte auf ihre Ursprüngliche Position gesetzt werden.
        """
        for obj in self.objects:
            obj.X = obj.ResetX
        self.man.dead = False
        self.man.deadEnd = False
        self.man.y = self.man.yConst

    def draw(self):
        """
        Spielobjekte werden dargestellt
        """
        # Hintergrund
        self.backgroundWorld.placeBackground(self.win)
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background1X, 0))
        self.win.blit(self.backgroundWorld.background, (self.backgroundWorld.background2X, 0))

        # Coinscore
        score = self.textFormat(str(self.valScore), self.font, 50, self.white)
        scoreRect = score.get_rect()
        self.win.blit(score, (self.WIDTH - (scoreRect[2] + 10), 30))

        # Objekte instanziieren
        self.fence.place(self.win)
        self.flyingEnemy.place(self.win)
        self.coin.place(self.win)
        self.man.draw(self.win)
        self.man.drawHitbox(self.win)

        pygame.display.update()

    def loop(self):
        """
        Spielschleife.
        Fragt in jedem Frame Nutzereingaben und Kollision ab.
        :returns: Spielscore und Kollisionsboolean
        """
        gameLoop = True
        while gameLoop:
            self.clock.tick(60)

            # Background
            for event in pygame.event.get():
                # Fenster schließen
                if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                    return False

            # Key Steuerung Player
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
            #Spieler bewegung verarbeiten
            self.man.move()
            #Spiel neu Zeichnen
            self.draw()

            #Kollisionshandhabung
            collBool = self.collision()
            if collBool:
                # Tot-Animation
                self.man.dead = True
                pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds/HumanHurt.wav"))

            if self.man.deadEnd:
                #Spiel beenden, Objekte zurücksetzen und Score speichern.
                self.resetObj()
                self.man.x = self.man.maxX / 2
                tmp_score = self.valScore
                self.valScore = str(0)
                return True,tmp_score


