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
