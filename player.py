import pygame
from pathlib import Path


class Player:
    def __init__(self, window):
        self.speed = 10
        self.image = pygame.image.load(str(Path('./assets/rocket.png')))
        self.player_width, self.player_height = self.image.get_size()
        self.window = window
        self.window_width, self.window_height = window.get_size()
        self.playerX = (self.window_width/2) - (self.player_width/2)
        self.playerY = (self.window_height/2) - (self.player_height/2)
        self.playerX_change, self.playerY_change = 0, 0
        self.moving = False

    def draw(self):
        self.window.blit(self.image, (self.playerX, self.playerY))

    def moveLeft(self):
        self.playerX_change = -self.speed

    def moveRight(self):
        self.playerX_change = self.speed

    def moveUp(self):
        self.playerY_change = -self.speed

    def moveDown(self):
        self.playerY_change = self.speed

    def move(self):
        if self.playerX + self.playerX_change >= 0 and self.playerX + self.player_width + self.playerX_change <= self.window_width:
            self.playerX += self.playerX_change
        if self.playerY + self.playerY_change >= 0 and self.playerY + self.player_height + self.playerY_change <= self.window_height:
            self.playerY += self.playerY_change

    def toggleMoving(self, isMoving):
        self.moving = isMoving
        self.playerX_change, self.playerY_change = 0, 0
