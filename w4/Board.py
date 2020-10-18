import random


class Board():
    def __init__(self, n_tiles=3):
        self.n = n_tiles
        self.tiles = random.sample(range(self.n**2), self.n**2)
        self.dim = n_tiles ** 2
        self.goal = [i for i in range(1, self.dim)] + [0]

    def __str__(self):
        s = ''
        for i, j in enumerate(self.tiles):
            s += str(j)
            if (i+1) % 3 == 0:
                s += '\n'
            else:
                s += ' '
        return s

    def hamming(self):
        h = 0
        for i in range(self.dim):
            if self.tiles[i] != self.goal[i]:
                h += 1
        return h

    def manhattan(self):
        m = 0
        for i in range(self.dim):
            if self.tiles[i] != self.goal[i]:
                m += self.get_steps(i, self.tiles[i])
        return m

    def get_steps(self, position, element):
        row = position // self.n
        col = position % self.n
        if element != 0:
            trow = (element - 1) // self.n
            tcol = (element - 1) % self.n
        else:
            trow = self.n - 1
            tcol = self.n - 1
        return abs(tcol - col) + abs(trow - row)

    def isGoal(self):
        return self.hamming == 0

    def equals(self, board):
        assert self.n == board.n
        if self.tiles == board.tiles:
            return True
        else:
            return False






            