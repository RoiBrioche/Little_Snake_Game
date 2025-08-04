# main.py

import pygame
import sys
from game.snake import Snake
from game.config import WIDTH, HEIGHT, CELL_SIZE, BACKGROUND_COLOR, SNAKE_COLOR, TICK_RATE

# Initialisation
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Logique du jeu
    snake.move()
    if snake.check_collision(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE):
        print("Game Over")
        running = False

    # Affichage
    SCREEN.fill(BACKGROUND_COLOR)
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(SCREEN, SNAKE_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(TICK_RATE)

pygame.quit()
sys.exit()
