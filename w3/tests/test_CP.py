from CollinearPoints import BruteCollinearPoints, Point


# def test_BF():
#     inp = [(10000, 0), (0, 10000), (3000, 7000), (7000, 3000), (20000, 21000), (3000, 4000), (14000, 15000), (6000, 7000)]
#     points = []
#     for p in inp:
#         points.append(Point(p[0], p[1]))
#     bcp = BruteCollinearPoints(points)
#     assert bcp.numberOfSegments() == 2


def test_slope():
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    p3 = Point(2, 4)
    #assert p1.slopeTo(p2) == float('inf')
    assert p1.slopeOrder(p2, p3) == 0
