from src.concat_str import concat_str


def test_hello_world():
    assert "Hello, World!" == "Hello, World!"


def test_math():
    assert 2 + 3 == 5


def test_concat_str():
    assert concat_str('a', 'b', 'c') == 'abc'
