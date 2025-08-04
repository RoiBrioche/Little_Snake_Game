"""This file containt the class Snake, which represents the snake logic for the game."""


class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]  # Le serpent est une liste de "blocs"
        self.direction = (1, 0)  # (x, y) => ici il va vers la droite
        self.grow_pending = False  # Vaudra True quand le serpent doit grandir

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)  # ajoute la nouvelle tête au début

        if self.grow_pending:
            self.grow_pending = False  # on laisse le segment ajouté
        else:
            self.body.pop()  # on retire la queue

    def change_direction(self, new_dir):
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir

    def grow(self):
        self.grow_pending = True
