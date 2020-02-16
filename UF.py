class UnionFind:
    def __init__(self, N):
        self.N = N
        self.obj_set = []
        for i in range(N):
            self.obj_set.append(i)

    def find(self, p, q):
        if self.obj_set[p] == self.obj_set[q]:
            return True
        else:
            return False

    def union(self, p, q):
        if self.find(p,q):
            return
        else:
            new = self.obj_set[q]
            old = self.obj_set[p]
            for i in range(len(self.obj_set)):
                if self.obj_set[i] == old:
                    self.obj_set[i] = new

DC = UnionFind(10)
print(DC.obj_set)
DC.union(4, 3)
DC.union(3, 8)   
DC.union(6, 5)
DC.union(9, 4)
DC.union(8, 9)
DC.union(2, 1)
print(DC.obj_set)
print(DC.find(2, 3))     