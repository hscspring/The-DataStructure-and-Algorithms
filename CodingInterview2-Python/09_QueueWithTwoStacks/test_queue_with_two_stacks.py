from queue_with_two_stacks import Queue

def test_queue_append_delete():
    que = Queue()
    que.append(1)
    assert que.delete() == 1

def test_not_blank_queue():
    que = Queue()
    que.append(1)
    que.append(2)
    assert que.delete() == 1
    assert que.delete() == 2

def test_delete_to_none():
    que = Queue()
    que.append(1)
    que.delete()
    assert que.delete() == None

def test_delete_blank():
    que = Queue()
    assert que.delete() == None