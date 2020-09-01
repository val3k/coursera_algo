import numpy as np
from Sorting import mergesort


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
        self.seg_list = []

    def check_rep_seg(self, seg):
        if len(self.seg_list) == 0:
            return True
        for ls in self.seg_list:
            if ls.p1.compareTo(seg.p2) == 0 and ls.p2.compareTo(seg.p1) == 0:
                return False
        return True

    def numberOfSegments(self):
        for p in self.points:
            for q in self.points:
                if q.compareTo(p) == 0:
                    continue
                direction = p.compareTo(q)
                for r in self.points:
                    if q.compareTo(r) != direction:
                        continue
                    for s in self.points:
                        if r.compareTo(s) != direction:
                            continue
                        if p.slopeTo(q) == p.slopeTo(s) == p.slopeTo(r):
                            if self.check_rep_seg(LineSegment(p, s)):
                                self.seg_list.append(LineSegment(p, s))
        return len(self.seg_list)

    def segments(self):
        return self.seg_list


class FastCollinearPoints(BruteCollinearPoints):
    def numberOfSegments(self):
        for p in self.points:
            slopes = []
            point_list = []
            for q in self.points:
                if q.compareTo(p) == 0:
                    continue
                slopes.append(p.slopeTo(q))
                point_list.append(q)

            slopes_sorted = mergesort(zip(slopes, point_list))
            start = slopes_sorted[0][0]
            ls = []
            for sp in slopes_sorted[1:]:
                if start == sp[0]:
                    ls.append(sp[1])
                else:
                    start = sp[0]
                    if len(ls) >= 3:
                        self.seg_list.append(LineSegment(p, ls[-1]))

        return len(self.seg_list)
