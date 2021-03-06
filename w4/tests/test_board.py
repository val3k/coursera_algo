from Board import Board
from Solver import Solver


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


def test_goal():
    b = Board()
    b.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    assert b.isGoal()
    b.tiles = [0, 2, 3, 1, 4, 5, 6, 7, 8]
    assert not b.isGoal()


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


def test_move():
    b = Board()
    b.tiles = [0, 1, 2, 3, 5, 6, 7, 8, 4]
    bp, mv = b.get_blank()
    b.blank_move(bp, 'right')
    assert b.tiles == [1, 0, 2, 3, 5, 6, 7, 8, 4]
    bp, mv = b.get_blank()
    b.blank_move(bp, 'left')
    assert b.tiles == [0, 1, 2, 3, 5, 6, 7, 8, 4]
    bp, mv = b.get_blank()
    b.blank_move(bp, 'down')
    assert b.tiles == [3, 1, 2, 0, 5, 6, 7, 8, 4]


def test_neighbors():
    b = Board()
    b.tiles = [0, 1, 2, 3, 5, 6, 7, 8, 4]
    list_neighbors = b.neighbors()
    assert len(list_neighbors) == 2
    b1 = list_neighbors[0]
    assert b1.tiles == [1, 0, 2, 3, 5, 6, 7, 8, 4]
    b2 = list_neighbors[1]
    assert b2.tiles == [3, 1, 2, 0, 5, 6, 7, 8, 4]


def test_heap():
    b = Board()
    b.tiles = [0, 1, 3, 4, 2, 5, 7, 8, 6]
    s = Solver(b)
    game_tree = s.solution()
    a = []
    if game_tree is not None:
        for node in game_tree:
            a.append(str(node[1]))
    assert len(game_tree) == 5

    b = Board()
    b.tiles = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    s = Solver(b)
    game_tree = s.solution()
    assert len(game_tree) == 2

    b = Board()
    b.tiles = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    s = Solver(b)
    game_tree = s.solution()
    assert len(game_tree) == 4

    b = Board()
    b.tiles = [1, 2, 0, 3, 4, 6, 7, 5, 8]
    s = Solver(b)
    game_tree = s.solution()
    assert game_tree is None
