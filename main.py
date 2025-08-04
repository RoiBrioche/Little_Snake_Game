# main.py

import pygame
import sys
from game.snake import Snake

# Initialisation
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20  # Taille d'une cellule de la grille
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Couleurs
BACKGROUND_COLOR = (30, 30, 30)  # Gris foncé
SNAKE_COLOR = (0, 255, 0)        # Vert

# Création du serpent
snake = Snake()

# Boucle principale
clock = pygame.time.Clock()
running = True

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gestion des touches
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Mettre à jour la logique du jeu
    snake.move()

    # Affichage
    SCREEN.fill(BACKGROUND_COLOR)
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(
            SCREEN,
            SNAKE_COLOR,
            pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    pygame.display.flip()
    clock.tick(10)

# Nettoyage
pygame.quit()
sys.exit()
