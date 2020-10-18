import random


class Board():
    def __init__(self, n_tiles=3):
        self.n = n_tiles
        self.tiles = random.randint(1, self.n**2-1)

    def __str__(self):
        print(self.tiles)