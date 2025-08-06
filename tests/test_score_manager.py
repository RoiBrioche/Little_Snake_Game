import os
import tempfile

from game.score_manager import load_best_score, save_best_score


def test_load_best_score_file_not_exists(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        fake_file = os.path.join(tmpdir, "best_score.txt")
        monkeypatch.setattr("game.config.BEST_SCORE_FILE", fake_file)
        score = load_best_score()
        assert score == 0
        assert os.path.exists(fake_file)


def test_load_best_score_file_valid(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        fake_file = os.path.join(tmpdir, "best_score.txt")
        with open(fake_file, "w") as f:
            f.write("42")
        monkeypatch.setattr("game.config.BEST_SCORE_FILE", fake_file)
        score = load_best_score()
        assert score == 42


def test_load_best_score_file_invalid(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        fake_file = os.path.join(tmpdir, "best_score.txt")
        with open(fake_file, "w") as f:
            f.write("not_a_number")
        monkeypatch.setattr("game.config.BEST_SCORE_FILE", fake_file)
        score = load_best_score()
        assert score == 0


def test_save_best_score(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        fake_file = os.path.join(tmpdir, "best_score.txt")
        monkeypatch.setattr("game.config.BEST_SCORE_FILE", fake_file)
        save_best_score(123)
        with open(fake_file, "r") as f:
            content = f.read().strip()
        assert content == "123"
