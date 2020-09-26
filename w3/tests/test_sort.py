import numpy as np
from Sorting import merge, mergesort


def test_sort():
    # setup
    n = np.random.randint(3, 10, size=1)[0]
    in_ls = np.arange(n)
    np.random.shuffle(in_ls)
    # exercise
    sort_ls = mergesort(in_ls)
    # verify
    assert np.array_equal(sort_ls, np.arange(n))


def test_trivial():
    # setup
    ls = np.array([2, 1])
    # ex
    out = mergesort(ls)
    # verify
    assert np.array_equal(out, np.array([1, 2]))


def test_merge():
    a1 = [2, 5]
    a2 = [1, 3, 4]
    a = merge(a1, a2, comp_function=lambda x, y: x <= y)
    assert np.array_equal(a, np.arange(1, 6))

