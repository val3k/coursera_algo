class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def distanceTo(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5

    def distanceSquaredTo(self, point):
        return self.distanceTo(self, point) ** 2

    def compareTo(self, point):
        if self.y < point.y or (self.y == point.y and self.x < point.x):
            return -1
        elif self.y == point.y and self.x == point.x:
            return 0
        else:
            return 1

    def equals(self, point):
        if self.y == point.y and self.x == point.x:
            return True
        else:
            return False


class RectHV:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
    
    def contains(self, point):
        if (self.xmin <= point.x <= self.xmax) and (self.ymin <= point.y <= self.ymax):
            return True
        else:
            return False

    def intersects(self, rect):
        p1 = Point(rect.xmin, rect.ymin)
        p2 = Point(rect.xmin, rect.ymax)
        p3 = Point(rect.xmax, rect.ymax)
        p4 = Point(rect.xmax, rect.ymin)
        _points = [p1, p2, p3, p4]
        for p in _points:
            if self.contains(self, p):
                return True
        return False
