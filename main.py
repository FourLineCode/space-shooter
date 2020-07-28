import pygame
import os
import sys
from pathlib import Path
from game import Game

# Window Size
SIZE = WIDTH, HEIGHT = 800, 600


# Init Window
pygame.init()
pygame.display.set_caption('Space Shooter')
os.environ['SDL_VIDEO_WINDOW_POS'] = '700,80'
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Hack', 14, True)

# Frames Per Second
FPS = 60


def update_fps():
    fps = 'FPS: ' + str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("green"))
    return fps_text


# Set Icon
icon = pygame.image.load(str(Path('./assets/icon.png')))
pygame.display.set_icon(icon)

# Init Game
game = Game(window)

# Main Loop
while game.running:
    # Limit FPS
    clock.tick(FPS)

    # Draw Background
    window.fill(pygame.Color('black'))
    window.blit(game.bg, (0, 0))
    window.blit(update_fps(), (5, 0))

    # Main Game
    game.run()

    pygame.display.update()

pygame.quit()
sys.exit()
