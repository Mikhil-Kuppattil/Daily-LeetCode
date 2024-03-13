import pytest
from pivot_number import PivotNumber

@pytest.fixture
def check_pivot():
    return PivotNumber()

def test_isPrime(check_pivot):
    assert check_pivot.is_pivot_number(8) == 6
    assert check_pivot.is_pivot_number(1) == 1
    assert check_pivot.is_pivot_number(4)==-1

if __name__ == "__main__":
    pytest.main()