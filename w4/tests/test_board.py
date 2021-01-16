from Board import Board


def test_str():
    b = Board()
    b.tiles = [0, 2, 3, 1, 4, 5, 6, 7, 8]
    str_b = str(b)
    print(str_b)
    assert str_b == '0 2 3\n1 4 5\n6 7 8\n'


def test_hamming():
    b = Board()
    b.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    assert b.hamming() == 0
    b.tiles = [0, 2, 3, 1, 4, 5, 6, 7, 8]
    assert b.hamming() == 7


def test_steps():
    b = Board()
    assert b.get_steps(0, 8) == 3
    assert b.get_steps(5, 4) == 2
    assert b.get_steps(6, 3) == 4
    assert b.get_steps(4, 0) == 2


def test_manhattan():
    b = Board()
    b.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    assert b.manhattan() == 0
    b.tiles = [1, 2, 3, 0, 5, 6, 7, 8, 4]
    assert b.manhattan() == 6


def test_equals():
    a = Board()
    a.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    b = Board()
    b.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    c = Board()
    c.tiles = [0, 2, 3, 4, 5, 6, 7, 8, 1]
    assert a.equals(b)
    assert not b.equals(c)


def test_blank():
    b = Board()
    b.tiles = [1, 2, 3, 0, 5, 6, 7, 8, 4]
    pos, moves = b.get_blank()
    assert pos == 3
    assert len(moves) == 3
    b.tiles = [1, 2, 3, 5, 0, 6, 7, 8, 4]
    pos, moves = b.get_blank()
    assert pos == 4
    assert len(moves) == 4


def test_neighbors(): # add test
    b = Board()
    b.tiles = [1, 2, 3, 0, 5, 6, 7, 8, 4]
    assert b.get_blank == 3

