from tasks import result

def test_sum_of_squares():
    assert result == sum(x ** 2 for x in range(1, 101) if x % 2 == 0)