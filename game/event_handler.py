import pygame

from game.config import (
    WIDTH,
    HEIGHT,
    HEADER_HEIGHT,
    CELL_SIZE,
)
from game.food import Food
from game.snake import Snake
from game.score_manager import save_best_score


GRID_HEIGHT = (HEIGHT - HEADER_HEIGHT) // CELL_SIZE
GRID_WIDTH = WIDTH // CELL_SIZE



def handle_events(running, game_over, score, best_score, snake, food, show_menu, button_rects):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.MOUSEBUTTONDOWN and show_menu:
            mouse_pos = pygame.mouse.get_pos()
            if button_rects["continue"].collidepoint(mouse_pos):
                show_menu = False
            elif button_rects["restart"].collidepoint(mouse_pos):
                if score > best_score:
                    best_score = score
                    save_best_score(best_score)
                snake = Snake()
                food = Food(GRID_WIDTH, GRID_HEIGHT, snake.body)
                score = 0
                game_over = False
                show_menu = False
            elif button_rects["quit"].collidepoint(mouse_pos):
                running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                show_menu = not show_menu  # Ouvre/Ferme le menu

            if show_menu:
                if event.key == pygame.K_c:  # Continuer
                    show_menu = False
                elif event.key == pygame.K_r:  # Rejouer
                    if score > best_score:
                        best_score = score
                        save_best_score(best_score)
                    snake = Snake()
                    food = Food(GRID_WIDTH, GRID_HEIGHT, snake.body)
                    score = 0
                    game_over = False
                    show_menu = False
                elif event.key == pygame.K_q:  # Quitter
                    running = False

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

    return running, game_over, score, best_score, snake, food, show_menu
