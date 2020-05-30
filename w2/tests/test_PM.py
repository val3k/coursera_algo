import io
import os
from contextlib import redirect_stdout
from Permutation import print_random


def test_pr():
    # setup
    with open('test_pm.txt', 'w+') as f:
        f.write('aaa\nbbb\nccc\nddd\neee\n')

    k = 3
    # exercise
    p = io.StringIO()
    with redirect_stdout(p):
        print_random(k, 'test_pm.txt')
    s_out = p.getvalue()
    # verify
    assert len(s_out.replace('\n', '')) == 9
    # cleanup
    os.remove('test_pm.txt')
