from stack_with_min import StackMin


st = StackMin()

def test_push1():
    st.push(3)
    assert st.min == 3

def test_push2():
    st.push(4)
    assert st.min == 3

def test_push3():
    st.push(2)
    assert st.min == 2

def test_push4():
    st.push(8)
    assert st.min == 2

def test_push5():
    st.push(1)
    assert st.min == 1

def test_push6():
    st.push(7)
    assert st.min == 1

def test_data_stack():
    assert st.data_stack == [3,4,2,8,1,7]

def test_min_stack():
    assert st.min_stack == [3,2,1]

def test_pop1():
    assert st.pop() == 7
    assert st.min == 1

def test_pop2():
    assert st.pop() == 1
    assert st.min == 2

def test_pop3():
    assert st.pop() == 8
    assert st.min == 2

def test_pop4():
    assert st.pop() == 2
    assert st.min == 3

def test_pop5():
    assert st.pop() == 4
    assert st.min == 3

def test_pop6():
    assert st.pop() == 3
    assert st.min == None

def test_pop7():
    assert st.pop() == None


