from tasks import Countdown

def test_countdown():
    assert list(Countdown(3)) == [3, 2, 1, 0]
    assert list(Countdown(0)) == [0]
    assert list(Countdown(1)) == [1, 0]
