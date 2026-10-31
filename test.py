from main import multiply, is_positive

def test_multiply():
    assert multiply(4, 5) == 20

def test_is_positive():
    assert is_positive(10) is True
    assert is_positive(-5) is False
