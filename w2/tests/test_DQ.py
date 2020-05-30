import io
from contextlib import redirect_stdout
from Deque import Deque


def test_add_first():
    # setup
    ll = Deque()
    # exercise
    ll.addFirst('a')
    s_out = ''
    for i in ll:
        s_out += i
    # verify
    assert ll.size == 1
    assert 'a' == s_out


def test_add_last():
    # setup
    ll = Deque()
    # exercise
    ll.addLast('b')
    s_out = ''
    for i in ll:
        s_out += i
    # verify
    assert ll.size == 1
    assert 'b' == s_out


def test_client():
    # setup
    ll = Deque()
    in_s = 'abcdLADR--__-'
    # exercise
    p = io.StringIO()
    with redirect_stdout(p):
        for i in in_s:
            if i == '-':
                ll.removeFirst()
            elif i == '_':
                ll.removeLast()
            elif i.isupper():
                ll.addLast(i)
            else:
                ll.addFirst(i)
    s_out = p.getvalue()
    # verify
    assert s_out.replace('\n', '') == 'dcRDb'
