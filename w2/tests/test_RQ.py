from RandomizedQ import RandomizedQueue


def test_add():
    # setup
    ll = RandomizedQueue()
    # exercise
    s = 'abc'
    for i in s:
        ll.enqueue(i)
    # verify
    s_rev = ''
    for i in ll:
        s_rev += i
    assert 3 == ll.size
    assert s_rev == 'cba'


def test_remove():
    # setup
    ll = RandomizedQueue()
    # exercise
    s = 'abcde'
    for i in s:
        ll.enqueue(i)
    a = ll.dequeue()
    # verify
    s_rev = ''
    check_string = s[::-1]
    check_string = check_string.replace(a, '')
    for i in ll:
        s_rev += i
    assert s_rev == check_string
    # assert 4 == num


def test_sample():
    # setup
    ll = RandomizedQueue()
    # exercise
    s = 'abcde'
    for i in s:
        ll.enqueue(i)
    a = ll.sample()
    # verify
    assert a in s
