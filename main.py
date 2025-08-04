# main.py

import pygame
import sys

from game.config import WIDTH, HEIGHT, HEADER_HEIGHT, CELL_SIZE, BACKGROUND_COLOR, SNAKE_COLOR, FOOD_COLOR, TICK_RATE
from game.food import Food
from game.snake import Snake


GRID_HEIGHT = (HEIGHT - HEADER_HEIGHT) // CELL_SIZE
GRID_WIDTH = WIDTH // CELL_SIZE

# Initialisation
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Création du serpent
snake = Snake()

food = Food(GRID_WIDTH, GRID_HEIGHT, snake.body)

score = 0
font = pygame.font.Font(None, 36)  # Police par défaut, taille 36

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
    if snake.check_collision(GRID_WIDTH, GRID_HEIGHT):
        print("Game Over")
        running = False
    # if snake.check_collision(WIDTH // CELL_SIZE, GRID_HEIGHT // CELL_SIZE):
    #     game_over = True

    # Affichage
    SCREEN.fill(BACKGROUND_COLOR)
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(
            SCREEN, SNAKE_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE)
        )

    pygame.draw.rect(
        SCREEN,
        (255, 0, 0),
        pygame.Rect(
            food.position[0] * CELL_SIZE,
            food.position[1] * CELL_SIZE + HEADER_HEIGHT,
            CELL_SIZE,
            CELL_SIZE,
        ),
    )

    if snake.body[0] == food.position:
        snake.grow()
        food.randomize_position(snake.body)
        score += 1

    # Bandeau
    pygame.draw.rect(SCREEN, (50, 50, 50), pygame.Rect(0, 0, WIDTH, HEADER_HEIGHT))  # gris foncé
    # Affichage du score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(TICK_RATE)

pygame.quit()
sys.exit()
