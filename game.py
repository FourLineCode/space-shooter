import pygame
from pathlib import Path
from entities.player import Player
from entities.bullet import Bullet
from entities.enemy import Enemy


class Game:
    def __init__(self, window):
        self.window = window
        self.running = True
        self.score = 0
        self.bg = pygame.image.load(str(Path('./assets/bg.jpg')))
        self.font = pygame.font.SysFont('Hack', 14, True)
        self.player = Player(self.window)
        self.bullet = Bullet(self.window, self.player)
        self.enemy = Enemy(self.window)

    def run(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self.running = False
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_TAB:
                    self.running = False
                if event.key is pygame.K_a:
                    self.player.toggleMoving(True)
                    self.player.moveLeft()
                if event.key is pygame.K_d:
                    self.player.toggleMoving(True)
                    self.player.moveRight()
                if event.key is pygame.K_w:
                    self.player.toggleMoving(True)
                    self.player.moveUp()
                if event.key is pygame.K_s:
                    self.player.toggleMoving(True)
                    self.player.moveDown()
                if event.key is pygame.K_SPACE:
                    if self.bullet.bullet_state == 'ready':
                        self.bullet.setShootingPos(self.player.playerX)
                        self.bullet.bullet_state = 'shoot'
            if event.type is pygame.KEYUP:
                self.player.toggleMoving(False)

        self.draw_window()

    def draw_window(self):
        # Moves Player When Key Pressed
        if self.player.moving:
            self.player.move()

        # Draws Bullet On State
        self.bullet.draw()

        # Draws Enemy
        self.enemy.move()
        self.enemy.draw()

        # Checks Bullet-Enemy Collide
        if self.bullet.checkCollide(self.enemy):
            self.enemy.randomizePosition()
            self.score += 1

        # Draws Player
        self.player.draw()

        # Draw Score
        self.window.blit(self.update_score(), (5, 20))

    def update_pos(self):
        pos = f'X: {self.player.playerX} Y: {self.player.playerY}'
        pos_text = self.font.render(pos, 1, pygame.Color("white"))
        return pos_text

    def update_score(self):
        score = f'Score: {self.score}'
        score_text = self.font.render(score, 1, pygame.Color("white"))
        return score_text
