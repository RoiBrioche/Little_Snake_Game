import pygame
import sys

from game.config import *
from game.game_loop import run_game

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

run_game(SCREEN)

pygame.quit()
sys.exit()
