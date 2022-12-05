import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1

def test_with_fixture2():
    print("this is second fixture")
