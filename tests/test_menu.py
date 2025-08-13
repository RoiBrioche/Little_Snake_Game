import pygame
import pytest
from game.graphics.menu import draw_menu
from game.config import WIDTH, HEIGHT


@pytest.fixture
def screen():
    pygame.init()
    return pygame.Surface((WIDTH, HEIGHT))


@pytest.fixture
def font():
    pygame.font.init()
    return pygame.font.SysFont(None, 24)


def test_draw_menu_returns_buttons(screen, font):
    score = 10
    best_score = 50
    buttons = draw_menu(screen, font, score, best_score)

    # On attend bien 3 boutons
    assert set(buttons.keys()) == {"continue", "restart", "quit"}

    # Vérifier que chaque bouton est bien un pygame.Rect
    for rect in buttons.values():
        assert isinstance(rect, pygame.Rect)
        assert rect.width > 0
        assert rect.height > 0
