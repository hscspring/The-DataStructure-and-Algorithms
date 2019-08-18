from find_duplication import get_duplicate1, get_duplicate2, get_duplicate3


def test_duplicate_min():
    numbers = [2, 1, 3, 1, 4]
    assert get_duplicate1(numbers) == 1
    assert get_duplicate2(numbers) == 1
    assert get_duplicate3(numbers) == 1


def test_duplicate_max():
    numbers = [2, 4, 3, 1, 4]
    assert get_duplicate1(numbers) == 4
    assert get_duplicate2(numbers) == 4
    assert get_duplicate3(numbers) == 4


def test_duplicate_multi():
    numbers = [2, 4, 2, 1, 4]
    assert get_duplicate1(numbers) in [2, 4]
    assert get_duplicate2(numbers) in [2, 4]
    assert get_duplicate3(numbers) in [2, 4]


def test_duplicate_order():
    numbers = [0, 1, 1, 3]
    assert get_duplicate1(numbers) == 1
    assert get_duplicate2(numbers) == 1
    assert get_duplicate3(numbers) == 1


def test_duplicate_same():
    numbers = [1, 1]
    assert get_duplicate1(numbers) == 1
    assert get_duplicate2(numbers) == 1
    assert get_duplicate3(numbers) == 1


def test_duplicate_input_cross_upper_same():
    numbers = [3, 3]
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None


def test_duplicate_input_cross_lower_same():
    numbers = [-1, -1]
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None


def test_duplicate_input_cross_upper():
    numbers = [1, 2, 3, 4]
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None


def test_duplicate_input_cross_lower():
    numbers = [-1, 1, 2, 3]
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None


def test_duplicate_no():
    numbers = [1, 2, 3, 0]
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None


def test_duplicate_none_input():
    numbers = []
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None


def test_duplicate_invalid_input():
    numbers = 1
    assert get_duplicate1(numbers) == None
    assert get_duplicate2(numbers) == None
    assert get_duplicate3(numbers) == None
