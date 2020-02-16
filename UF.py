class UnionFind:
    def __init__(self, N):
        self.N = N
        self.obj_set = []
        for i in range(N):
            self.obj_set.append(i)
    
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

    def union(self, p, q):
        if self.find(p,q):
            return
        else:
            new = self._get_root(q)
            old = self._get_root(p)
            self.obj_set[old] = new

DC = UnionFind(10)
DC.union(4, 3)
DC.union(3, 8)
DC.union(6, 5)
DC.union(9, 4)
DC.union(2, 1)
DC.union(5, 0)
DC.union(7, 2)
DC.union(6, 1)
DC.union(7, 3)
print(DC.obj_set)