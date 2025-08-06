import pygame

from unittest.mock import patch

from game.graphics import draw_trophy_image


def test_draw_trophy_image_loads_and_blits():
    pygame.init()
    pygame.display.set_mode((1, 1))  # <-- Ajoute cette ligne pour init la vidéo
    screen = pygame.Surface((100, 100))

    with patch("pygame.image.load") as mock_load:
        mock_img = pygame.Surface((100, 50), pygame.SRCALPHA)
        mock_load.return_value = mock_img

        draw_trophy_image(screen, 10, 10)
        # Pas d'exception = succès
