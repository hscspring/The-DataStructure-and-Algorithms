from cutting_rope import max_production_dp, max_production_greedy

def test_n0():
    assert max_production_dp(0) == 0
    assert max_production_greedy(0) == 0

def test_n1():
    assert max_production_dp(1) == 0
    assert max_production_greedy(1) == 0

def test_n2():
    assert max_production_dp(2) == 1
    assert max_production_greedy(2) == 1

def test_n3():
    assert max_production_dp(3) == 2
    assert max_production_greedy(3) == 2

def test_n4():
    assert max_production_dp(4) == 4
    assert max_production_greedy(4) == 4

def test_n5():
    assert max_production_dp(5) == 6
    assert max_production_greedy(5) == 6

def test_n6():
    assert max_production_dp(6) == 9
    assert max_production_greedy(6) == 9

def test_n7():
    assert max_production_dp(7) == 12
    assert max_production_greedy(7) == 12

def test_n8():
    assert max_production_dp(8) == 18
    assert max_production_greedy(8) == 18

def test_n9():
    assert max_production_dp(9) == 27
    assert max_production_greedy(9) == 27

def test_n10():
    assert max_production_dp(10) == 36
    assert max_production_greedy(10) == 36

def test_n50():
    assert max_production_dp(50) == 86093442
    assert max_production_greedy(50) == 86093442


