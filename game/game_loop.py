import pygame
import sys

from game.config import (
    WIDTH,
    HEIGHT,
    HEADER_HEIGHT,
    CELL_SIZE,
    TICK_RATE,
)
from game.food import Food
from game.snake import Snake
from game.score_manager import load_best_score, save_best_score


GRID_HEIGHT = (HEIGHT - HEADER_HEIGHT) // CELL_SIZE
GRID_WIDTH = WIDTH // CELL_SIZE

from game.graphics import draw_trophy_image
from game.event_handler import handle_events
from game.draw import draw_game_screen

def run_game(screen):
    snake = Snake()
    food = Food(GRID_WIDTH, GRID_HEIGHT, snake.body)
    score = 0
    best_score = load_best_score()
    game_over = False
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    print("le jeux va se lancer")
    running = True
    while running:

        running, game_over, score, best_score, snake, food = handle_events(running, game_over, score, best_score, snake, food)
        if not game_over:
            snake.move()
            if snake.check_collision(GRID_WIDTH, GRID_HEIGHT):
                game_over = True
        
        if snake.body[0] == food.position:
            snake.grow()
            food.randomize_position(snake.body)
            score += 1

        draw_game_screen(screen, snake, food, score, best_score, game_over, font)

        pygame.display.flip()
        clock.tick(TICK_RATE)

    if score > best_score:
        save_best_score(score)
