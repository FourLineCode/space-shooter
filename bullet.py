import pygame
import math
from pathlib import Path


class Bullet:
    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.speed = 10
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

    # Moves Bullet When Shot
    def shoot(self):
        if self.bullet_state is 'shoot':
            if self.bulletY + self.speed > 0:
                self.bulletY -= self.speed
            else:
                self.bullet_state = 'ready'
        self.window.blit(self.image, (self.bulletX, self.bulletY))

    # Locks Bullet X Position When Shot
    def setShootingPos(self, pos):
        self.bulletX = pos + (self.bullet_width/2)

    def checkCollide(self, enemy):
        distance = math.sqrt(
            math.pow((self.bulletX+(self.bullet_width/2))-(enemy.enemyX+(enemy.enemy_width/2)), 2) + math.pow(self.bulletY-(enemy.enemyY+(enemy.enemy_height/2)), 2))

        if distance <= enemy.enemy_height/2:
            self.bullet_state = 'ready'
            return True
        else:
            return False
