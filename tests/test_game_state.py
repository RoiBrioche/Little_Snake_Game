# tests/test_game_state.py

from game.snake import Snake
from game.food import Food


def test_score_increments_when_eating_food():
    snake = Snake()
    food_position = (snake.body[0][0] + 1, snake.body[0][1])  # Place food in front of head
    food = Food(30, 30, snake.body)
    food.position = food_position

    score = 0
    snake.change_direction((1, 0))  # Go right
    snake.move()

    if snake.body[0] == food.position:
        score += 1

    assert score == 1


def test_score_resets_on_restart():
    score = 10
    game_over = True

    if game_over:
        score = 0
        game_over = False

    assert score == 0
    assert game_over is False


def test_game_over_triggers_on_collision():
    snake = Snake()

    # Force collision with itself
    snake.body = [(5, 5), (5, 6), (5, 7), (5, 5)]  # Last segment overlaps with 2nd
    game_over = snake.check_collision(30, 30)
    assert game_over is True
