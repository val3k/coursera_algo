from Board import Board


def test_str():
    b = Board()
    str_b = str(b)
    assert str_b == '0 2 3/n 1 4 5/n 6 7 8'