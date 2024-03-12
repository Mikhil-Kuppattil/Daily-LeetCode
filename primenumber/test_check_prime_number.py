import pytest
from check_prime_number import PrimeNumber

@pytest.fixture
def check_prime():
    return PrimeNumber()

def test_isPrime(check_prime):
    assert check_prime.is_prime_number(5) == True
    assert check_prime.is_prime_number(7) == True
    assert check_prime.is_prime_number(10)==False

if __name__ == "__main__":
    pytest.main()