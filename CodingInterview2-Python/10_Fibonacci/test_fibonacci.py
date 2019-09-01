from fibonacci import fib, fib_loop, fib_matrix

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(40) == 102334155

def test_fib_loop():
    assert fib_loop(0) == 0
    assert fib_loop(1) == 1
    assert fib_loop(2) == 1
    assert fib_loop(3) == 2
    assert fib_loop(40) == 102334155

def test_fib_matrix():
    assert fib_matrix(0) == 0
    assert fib_matrix(1) == 1
    assert fib_matrix(2) == 1
    assert fib_matrix(3) == 2
    assert fib_matrix(40) == 102334155