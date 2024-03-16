import pytest
from sqrt import Sqrt

@pytest.fixture
def check_sqrt():
    return Sqrt()

def test_isPrime(check_sqrt):
    assert check_sqrt.mySqrt(8) == 2
    assert check_sqrt.mySqrt(8) == 2
   
if __name__ == "__main__":
    pytest.main()