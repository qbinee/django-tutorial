import pytest
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

@pytest.fixture
def tmp_path():
    return 'testpath'


def test_needsfiles(tmp_path):
    print(tmp_path)
    assert tmp_path == 'testpath'