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

