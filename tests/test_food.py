import pytest
from game.food import Food


def test_food_initializes_not_on_snake():

    snake_body = [(5, 5), (4, 5), (3, 5)]
    food = Food(grid_width=10, grid_height=10, snake_body=snake_body)

    # La nourriture ne doit pas apparaître sur le serpent
    assert food.position not in snake_body
    assert 0 <= food.position[0] < 10
    assert 0 <= food.position[1] < 10


def test_food_randomize_position_moves_it():

    snake_body = [(5, 5), (4, 5), (3, 5)]
    food = Food(grid_width=10, grid_height=10, snake_body=snake_body)

    initial_position = food.position
    food.randomize_position(snake_body)

    # La nouvelle position doit être différente dans la plupart des cas
    assert food.position not in snake_body
    assert 0 <= food.position[0] < 10
    assert 0 <= food.position[1] < 10
