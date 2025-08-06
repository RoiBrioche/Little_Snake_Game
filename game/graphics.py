import pygame

from game.config import BACKGROUND_COLOR

import pygame
import os

# Charger l'image une seule fois au lancement (global)
_trophy_img = None


def draw_trophy_image(screen, x, y):
    global _trophy_img

    if _trophy_img is None:
        image_path = os.path.join("assets", "Trophy_PNG.png")
        img = pygame.image.load(image_path).convert_alpha()

        # Récupérer la taille originale
        original_width, original_height = img.get_size()

        # Largeur souhaitée (exemple)
        target_width = 40

        # Calcul hauteur pour garder le ratio
        target_height = int(target_width * original_height / original_width)

        _trophy_img = pygame.transform.scale(img, (target_width, target_height))

    screen.blit(_trophy_img, (x + 20, y + 5))  # Ajuster la position Y pour le centrer


def draw_trophy(surface, x, y):
    # Pied du trophée - plus fin et petit
    pygame.draw.rect(surface, (255, 215, 0), (x + 12, y + 35, 15, 6))
    # Base du socle - plus fin et allongé
    pygame.draw.rect(surface, (218, 165, 32), (x + 7, y + 25, 30, 10))

    pygame.draw.ellipse(surface, (255, 223, 0), (x + 7, y + 2, 30, 30))
    pygame.draw.rect(surface, BACKGROUND_COLOR, (x + 7, y + 2, 30, 15))  # recouvre moitié haute

    # Anse gauche arrondie avec plusieurs segments
    pygame.draw.line(surface, (255, 215, 0), (x + 7, y + 12), (x - 5, y + 18), 3)
    pygame.draw.line(surface, (255, 215, 0), (x - 5, y + 18), (x - 7, y + 24), 3)
    pygame.draw.line(surface, (255, 215, 0), (x - 7, y + 24), (x - 5, y + 28), 3)

    # Anse droite arrondie
    pygame.draw.line(surface, (255, 215, 0), (x + 37, y + 12), (x + 48, y + 18), 3)
    pygame.draw.line(surface, (255, 215, 0), (x + 48, y + 18), (x + 50, y + 24), 3)
    pygame.draw.line(surface, (255, 215, 0), (x + 50, y + 24), (x + 48, y + 28), 3)
