import pygame
from pathlib import Path


class Bullet:
    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.speed = 20
        self.image = pygame.image.load(str(Path('./assets/bullet.png')))
        self.bullet_width, self.bullet_height = self.image.get_size()
        self.window_width, self.window_height = window.get_size()
        self.bulletX = self.player.playerX
        self.bulletY = self.player.playerY
        self.bullet_state = 'ready'

    def draw(self):
        self.bulletX = self.player.playerX + (self.bullet_width/2)
        self.bulletY = self.player.playerY + (self.bullet_height/2)

        self.window.blit(self.image, (self.bulletX, self.bulletY))

    def shoot(self):
        if self.bullet_state is 'shoot':
            if self.bulletY + self.speed > 0:
                self.bulletY -= self.speed
            else:
                self.bullet_state = 'ready'
        self.window.blit(self.image, (self.bulletX, self.bulletY))

    def setShootingPos(self, pos):
        self.bulletX = pos + (self.bullet_width/2)
