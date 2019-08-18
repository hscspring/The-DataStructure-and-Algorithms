from find_duplication_no_edit import get_duplicate


def test_duplicate_min():
    numbers = [2, 1, 3, 1, 4]
    assert get_duplicate(numbers) == 1


def test_duplicate_max():
    numbers = [2, 4, 3, 1, 4]
    assert get_duplicate(numbers) == 4


def test_duplicate_multi():
    numbers = [2, 4, 2, 1, 4]
    assert get_duplicate(numbers) in [2, 4]


def test_duplicate_order():
    numbers = [0, 1, 1, 2]
    assert get_duplicate(numbers) == 1


def test_duplicate_same():
    numbers = [1, 1]
    assert get_duplicate(numbers) == 1


def test_duplicate_input_cross_upper_same():
    numbers = [3, 3]
    assert get_duplicate(numbers) == None


def test_duplicate_input_cross_lower_same():
    numbers = [-1, -1]
    assert get_duplicate(numbers) == None


def test_duplicate_input_cross_upper():
    numbers = [1, 2, 3, 4]
    assert get_duplicate(numbers) == None


def test_duplicate_input_cross_lower():
    numbers = [-1, 1, 2, 3]
    assert get_duplicate(numbers) == None


def test_duplicate_no():
    numbers = [1, 2, 3, 0]
    assert get_duplicate(numbers) == None


def test_duplicate_none_input():
    numbers = []
    assert get_duplicate(numbers) == None


def test_duplicate_invalid_input():
    numbers = 1
    assert get_duplicate(numbers) == None
