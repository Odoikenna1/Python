from x import y

def test_y_function():
    assert y("") == 0
    assert y(" ") == 1
    assert y("hello") == 5
    assert y(" hello ") == 7
    assert y("!@#$%") == 5