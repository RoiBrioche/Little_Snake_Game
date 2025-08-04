# tests/test_snake.py

import pytest
from game.snake import Snake


def test_snake_moves_forward():

    snake = Snake()
    initial_head = snake.body[0]

    snake.move()

    new_head = snake.body[0]
    expected_head = (initial_head[0] + snake.direction[0], initial_head[1] + snake.direction[1])

    assert new_head == expected_head
    assert len(snake.body) == 3  # car il n’a pas grandi


def test_collision_with_wall():

    snake = Snake()
    snake.body[0] = (-1, 5)  # Hors limite à gauche

    assert snake.check_collision(20, 20) is True


def test_no_collision():

    snake = Snake()
    snake.body = [(5, 5), (5, 6), (5, 7)]

    assert snake.check_collision(20, 20) is False


def test_collision_with_body():

    snake = Snake()
    # La tête est sur un segment du corps
    snake.body = [(5, 5), (5, 6), (5, 5)]

    assert snake.check_collision(20, 20) is True


def test_grow():

    snake = Snake()
    initial_length = len(snake.body)

    snake.grow()
    snake.move()

    assert len(snake.body) == initial_length + 1
