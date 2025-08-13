# game/menu.py
import pygame

from game.config import *


def draw_menu(screen, font, score, best_score):
    """Dessine le menu et retourne les rectangles cliquables."""

    button_rects = {}

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    card_width, card_height = 300, 300
    card_x = WIDTH // 2 - card_width // 2
    card_y = HEIGHT // 2 - card_height // 2

    pygame.draw.rect(screen, (30, 30, 30), (card_x, card_y, card_width, card_height), border_radius=12)

    # Titre
    title_text = font.render("Menu", True, (255, 255, 255))
    screen.blit(title_text, (card_x + card_width // 2 - title_text.get_width() // 2, card_y + 20))

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
        screen.blit(
            text_surf,
            (
                btn_rect.x + (btn_rect.width - text_surf.get_width()) // 2,
                btn_rect.y + (btn_rect.height - text_surf.get_height()) // 2,
            ),
        )
        button_rects[action] = btn_rect

    return button_rects
