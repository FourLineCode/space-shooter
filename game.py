import pygame
from pathlib import Path
from player import Player


class Game:
    def __init__(self, window):
        self.window = window
        self.running = True
        self.bg = pygame.image.load(str(Path('./assets/bg.jpg')))
        self.player = Player(self.window)
        self.font = pygame.font.SysFont('Hack', 14, True)

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
            if event.type is pygame.KEYUP:
                self.player.toggleMoving(False)

        if self.player.moving:
            self.player.move()
        self.player.draw()

    def update_pos(self):
        pos = f'X: {self.player.playerX} Y: {self.player.playerY}'
        pos_text = self.font.render(pos, 1, pygame.Color("white"))
        return pos_text
