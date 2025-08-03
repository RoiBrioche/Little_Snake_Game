# main.py

import pygame
import sys

# Initialisation
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Couleurs
BACKGROUND_COLOR = (30, 30, 30)  # Gris foncé

# Boucle principale
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    clock.tick(10)

# Nettoyage
pygame.quit()
sys.exit()
