import os

import game.config


def load_best_score():
    """Charge le meilleur score depuis le fichier, ou retourne 0 si inexistant."""
    if not os.path.exists(game.config.BEST_SCORE_FILE):
        with open(game.config.BEST_SCORE_FILE, "w") as f:
            f.write("0")
        return 0

    try:
        with open(game.config.BEST_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return 0


def save_best_score(score):
    """Enregistre un nouveau meilleur score dans le fichier."""
    with open(game.config.BEST_SCORE_FILE, "w") as f:
        f.write(str(score))
