import pytest

@pytest.mark.skip
def test_greater():
   num = 100
   assert num > 90
@pytest.mark.tryfirst
def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200