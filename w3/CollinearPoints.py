class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def compareTo(self, p):
        if self.y < p.y or (self.y == p.y and self.x < p.x):
            return -1
        elif self.y == p.y and self.x == p.x:
            return 0
        else:
            return 1

    def slopeTo(self, p):
        if self.y == p.y:
            return 1e-9
        elif self.x == p.x:
            return float('inf')
        elif self.compareTo(p) == 0:
            return float('-inf')
        else:
            return (p.y - self.y)/(p.x - self.x)

    def slopeOrder(self, p1, p2):
        if self.slopeTo(p1) < self.slopeTo(p2):
            return -1
        elif self.slopeTo(p1) == self.slopeTo(p2):
            return 0
        else:
            return 1


class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'{str(self.p1)} -> {str(self.p2)}'


class BruteCollinearPoints:
    def __init__(self, points):
        self.points = points
        self.ls = []

    def numberOfSegments(self):
        for p in self.points:
            for q in self.points:
                for r in self.points:
                    for s in self.points:
                        if p.slopeTo(q) == p.slopeTo(s) == p.slopeTo(r):
                            self.ls.append(LineSegment(p, s))

    def segments(self):
        return self.ls
            

