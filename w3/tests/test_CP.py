from CollinearPoints import BruteCollinearPoints, Point, FastCollinearPoints


def test_brute():
    inp = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 2),
           (4, 1), (3, 2), (2, 3), (1, 4)]
    points = []
    for p in inp:
        points.append(Point(p[0], p[1]))
    bcp = BruteCollinearPoints(points)
    assert bcp.numberOfSegments() == 2


def test_fast():
    inp = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 2),
           (4, 1), (3, 2), (2, 3), (1, 4)]
    points = []
    for p in inp:
        points.append(Point(p[0], p[1]))
    fcp = FastCollinearPoints(points)
    assert fcp.numberOfSegments() == 2
