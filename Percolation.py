import random
from UF import UnionFind


class Percolation:
    def __init__(self, N):
        self.N = N
        self.system = UnionFind(self.N ** 2 + 2)
        self.open_stat = [0 for i in range(self.N ** 2 + 2)]

    def open_site(self, row, col):
        # transform row col to obj_set[i]
        idx = self.N * (row - 1) + col
        # open site
        self.open_stat[idx] = 1

        if row == 1:
            self.system.union(idx, 0)
        if row == self.N:
            self.system.union(idx, self.N ** 2 + 1)

        if col != self.N and self.is_open(row, col+1):
            self.system.union(idx, idx+1)
        if col != 1 and self.is_open(row, col-1):
            self.system.union(idx, idx-1)
        if row != 1 and self.is_open(row-1, col):
            self.system.union(idx, idx-self.N)
        if row != self.N and self.is_open(row+1, col):
            self.system.union(idx, idx+self.N)

    def is_open(self, row, col):
        idx = self.N * (row - 1) + col
        if self.open_stat[idx] == 1:
            return True
        else:
            return False

    def is_full(self, row, col):
        idx = self.N * (row - 1) + col
        if self.open_stat[idx] == 0:
            return True
        else:
            return False

    def n_of_open(self):
        s = 0
        for i in self.open_stat:
            s += i
        return s

    def percolates(self):
        if self.system.find(0, self.N**2 + 1):
            return True
        else:
            return False

