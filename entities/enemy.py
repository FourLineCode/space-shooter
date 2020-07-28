import pygame
import random
from pathlib import Path


class Enemy:
    def __init__(self, window):
        self.window = window
        self.speed = 2
        self.image = pygame.image.load(str(Path('./assets/monster1.png')))
        self.enemy_width, self.enemy_height = self.image.get_size()
        self.window_width, self.window_height = window.get_size()
        self.enemyX = self.randomizePosition()
        self.enemyY = -10

    def draw(self):
        self.window.blit(self.image, (self.enemyX, self.enemyY))

    def randomizePosition(self):
        randomPos = random.randint(20, 720)
        self.enemyX = randomPos
        self.enemyY = -10
        return randomPos

    def move(self):
        self.enemyY += self.speed
        if self.enemyY + self.enemy_height > self.window_height:
            self.randomizePosition()

    # Checks If Enemy Reached End Of Screen
    def isGameOver(self):
        if self.enemyY + self.enemy_height >= self.window_height:
            return True
        return False
