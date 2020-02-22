class UnionFind:
    def __init__(self, N):
        self.N = N
        self.obj_set = []
        self.sz = []
        for i in range(N):
            self.obj_set.append(i)
            self.sz.append(1)

    def _get_root(self, p):
        r = self.obj_set[p]
        while r != self.obj_set[r]:
            r = self.obj_set[r]
        return r

    def find(self, p, q):
        if self._get_root(p) == self._get_root(q):
            return True
        else:
            return False

    def union(self, q, p):
        if self.find(p, q):
            return
        else:
            new = self._get_root(q)
            old = self._get_root(p)
            if self.sz[new] >= self.sz[old]:
                self.obj_set[old] = new
                self.sz[new] += self.sz[old]
            else:
                self.obj_set[new] = old
                self.sz[old] += self.sz[new]


DC = UnionFind(12)
DC.union(2, 0)
DC.union(1, 3)
DC.union(1, 4)
DC.union(5, 1)
DC.union(0, 1)
DC.union(3, 7)
DC.union(6, 8)
DC.union(6, 9)
DC.union(8, 10)
DC.union(9, 11)
DC.union(9, 12)
DC.union(8, 6)

print(DC.obj_set)
