import pygame
import sys

from game.config import (
    WIDTH,
    HEIGHT,
    HEADER_HEIGHT,
    CELL_SIZE,
    BACKGROUND_COLOR,
    SNAKE_COLOR,
    FOOD_COLOR,
    TICK_RATE,
    GRID_COLOR_LIGHT,
    GRID_COLOR_DARK,
)
from game.food import Food
from game.snake import Snake
from game.score_manager import load_best_score, save_best_score


GRID_HEIGHT = (HEIGHT - HEADER_HEIGHT) // CELL_SIZE
GRID_WIDTH = WIDTH // CELL_SIZE

from game.graphics import draw_trophy_image

# Initialisation
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = Snake()
food = Food(GRID_WIDTH, GRID_HEIGHT, snake.body)

game_over = False
score = 0
best_score = load_best_score()
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
            else:
                if event.key == pygame.K_r:
                    if score > best_score:
                        best_score = score
                        save_best_score(best_score)

                    snake = Snake()
                    food = Food(GRID_WIDTH, GRID_HEIGHT, snake.body)
                    score = 0
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

    if not game_over:
        snake.move()
        if snake.check_collision(GRID_WIDTH, GRID_HEIGHT):
            game_over = True

        # --- Dessin du damier ---
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if (row + col) % 2 == 0:
                    color = GRID_COLOR_LIGHT
                else:
                    color = GRID_COLOR_DARK
                pygame.draw.rect(
                    SCREEN,
                    color,
                    pygame.Rect(col * CELL_SIZE, row * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE)
                )

        for segment in snake.body:
            x, y = segment
            pygame.draw.rect(
                SCREEN,
                SNAKE_COLOR,
                pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE),
            )

    pygame.draw.rect(
        SCREEN,
        FOOD_COLOR,
        pygame.Rect(food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE),
    )

    if snake.body[0] == food.position:
        snake.grow()
        food.randomize_position(snake.body)
        score += 1

    pygame.draw.rect(SCREEN, (50, 50, 50), pygame.Rect(0, 0, WIDTH, HEADER_HEIGHT))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    SCREEN.blit(score_text, (10, 10))

    # Affichage du trophée à gauche du meilleur score
    draw_trophy_image(SCREEN, WIDTH - 200, 5)
    best_score_text = font.render(f"{best_score}", True, (255, 215, 0))
    SCREEN.blit(best_score_text, (WIDTH - 140, 15))

    if game_over:
        game_over_text = font.render("Game Over - Press R to Restart", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(TICK_RATE)

if score > best_score:
    save_best_score(score)

pygame.quit()
sys.exit()
