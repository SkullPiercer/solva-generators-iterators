from tasks import fibonacci

def test_fibonacci():
    assert list(fibonacci(0)) == []
    assert list(fibonacci(1)) == [0]
    assert list(fibonacci(5)) == [0, 1, 1, 2, 3]
    assert list(fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]
