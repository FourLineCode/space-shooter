import pygame
from pathlib import Path
from entities.player import Player
from entities.bullet import Bullet
from entities.enemy import Enemy


class Game:
    def __init__(self, window):
        self.state = 'start'
        self.window = window
        self.window_width, self.window_height = window.get_size()
        self.running = True
        self.score = 0
        self.bg = pygame.image.load(str(Path('./assets/bg.jpg')))
        self.font = pygame.font.SysFont('Hack', 14, True)
        self.midFont = pygame.font.SysFont('Hack', 24, True)
        self.bigFont = pygame.font.SysFont('Hack', 80, True)
        self.player = Player(self.window)
        self.bullet = Bullet(self.window, self.player)
        self.enemy = Enemy(self.window)
        self.display = True
        self.count = 0

    def run(self):
        if self.state == 'menu':
            pass
        elif self.state == 'start':
            self.start()
        elif self.state == 'over':
            self.game_over()

    def start(self):
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

    # Draws All Entities On Window
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

        if self.enemy.isGameOver():
            self.state = 'over'

        # Draws Player
        self.player.draw()

        # Update Player Position
        self.window.blit(self.update_pos(), (self.window_width - 140, 0))

        # Draw Score
        self.window.blit(self.update_score(), (5, 20))

    def game_over(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self.running = False
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_TAB:
                    self.running = False
                if event.key is pygame.K_SPACE:
                    self.__init__(self.window)
                    self.state = 'start'

        text = 'GAME OVER'
        game_over_text = self.bigFont.render(text, 1, pygame.Color('white'))
        over_width, over_height = game_over_text.get_size()
        over_x, over_y = self.window_width / 2 - over_width / \
            2, self.window_height/2 - over_height/2

        con = 'Press Space To Continue'
        continue_text = self.midFont.render(
            con, 1, pygame.Color('white'))
        con_width, con_height = continue_text.get_size()
        con_x, con_y = self.window_width / 2 - con_width / \
            2, self.window_height/2 - con_height/2 + (over_height/2) + 10

        score = f'Score: {self.score}'
        score_text = self.midFont.render(
            score, 1, pygame.Color('white'))
        score_width, score_height = score_text.get_size()
        score_x, score_y = self.window_width / 2 - score_width / \
            2, self.window_height/2 - score_height/2 - (over_height/2) - 10

        self.window.blit(game_over_text, (over_x, over_y))
        self.window.blit(score_text, (score_x, score_y))
        self.count += 1
        if self.count > 20:
            self.count = 0
            self.display = not self.display
        if self.display:
            self.window.blit(continue_text, (con_x, con_y))

    def update_pos(self):
        pos = f'X: {self.player.playerX} Y: {self.player.playerY}'
        pos_text = self.font.render(pos, 1, pygame.Color("white"))
        return pos_text

    def update_score(self):
        score = f'Score: {self.score}'
        score_text = self.font.render(score, 1, pygame.Color("white"))
        return score_text
