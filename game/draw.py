import pygame

from game.config import *
from game.graphics import draw_trophy_image

GRID_HEIGHT = (HEIGHT - HEADER_HEIGHT) // CELL_SIZE
GRID_WIDTH = WIDTH // CELL_SIZE

def draw_game_screen(screen, snake, food, score, best_score, game_over, font):
    screen.fill(BACKGROUND_COLOR)

    # Dessiner la grille (damier)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if (row + col) % 2 == 0:
                color = GRID_COLOR_LIGHT
            else:
                color = GRID_COLOR_DARK
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(col * CELL_SIZE, row * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE)
            )

    # Dessiner le serpent
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(
            screen,
            SNAKE_COLOR,
            pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE)
        )

    # Dessiner la nourriture
    pygame.draw.rect(
        screen,
        FOOD_COLOR,
        pygame.Rect(food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE + HEADER_HEIGHT, CELL_SIZE, CELL_SIZE)
    )

    # Dessiner la barre de score
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, 0, WIDTH, HEADER_HEIGHT))
    

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Afficher le trophée à gauche du best score
    draw_trophy_image(screen, WIDTH - 210, 5)

    best_score_text = font.render(f"Best: {best_score}", True, (255, 215, 0))
    screen.blit(best_score_text, (WIDTH - 150, 10))

    if game_over:
        game_over_text = font.render("Game Over - Press R to Restart", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
