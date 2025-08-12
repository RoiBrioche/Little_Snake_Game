import pygame

from game.config import *
from game.graphics import draw_trophy_image

GRID_HEIGHT = (HEIGHT - HEADER_HEIGHT) // CELL_SIZE
GRID_WIDTH = WIDTH // CELL_SIZE

def draw_game_screen(screen, snake, food, score, best_score, game_over, font, show_menu):
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

    # Barre de score
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, 0, WIDTH, HEADER_HEIGHT))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    draw_trophy_image(screen, WIDTH - 210, 5)
    best_score_text = font.render(f"Best: {best_score}", True, (255, 215, 0))
    screen.blit(best_score_text, (WIDTH - 150, 10))

    
    button_rects = {}

    # --- Menu ---
    if show_menu:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        card_width, card_height = 300, 300
        card_x = WIDTH // 2 - card_width // 2
        card_y = HEIGHT // 2 - card_height // 2

        pygame.draw.rect(screen, (30, 30, 30), (card_x, card_y, card_width, card_height), border_radius=12)

        # Titre
        title_text = font.render("Menu", True, (255, 255, 255))
        screen.blit(title_text, (card_x + card_width//2 - title_text.get_width()//2, card_y + 20))

        # Score
        score_text = font.render(f"Score: {score}", True, (200, 200, 200))
        best_text = font.render(f"Best: {best_score}", True, (255, 215, 0))
        screen.blit(score_text, (card_x + 30, card_y + 70))
        screen.blit(best_text, (card_x + 30, card_y + 110))

        # Boutons
        options = [("Continuer", "continue"), ("Rejouer", "restart"), ("Quitter", "quit")]
        for i, (label, action) in enumerate(options):
            btn_rect = pygame.Rect(card_x + 30, card_y + 160 + i * 40, card_width - 60, 30)
            pygame.draw.rect(screen, (70, 70, 70), btn_rect, border_radius=6)
            text_surf = font.render(label, True, (255, 255, 255))
            screen.blit(text_surf, (btn_rect.x + (btn_rect.width - text_surf.get_width()) // 2,
                                    btn_rect.y + (btn_rect.height - text_surf.get_height()) // 2))
            button_rects[action] = btn_rect

    if game_over:
        game_over_text = font.render("Game Over - Press R to Restart", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

    return button_rects