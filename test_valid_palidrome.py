import pytest
from valid_palidrome import Solution

@pytest.fixture
def solution():
    return Solution()

def test_isPalindrome(solution):
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome("race a car") == False
    assert solution.isPalindrome("") == True
    assert solution.isPalindrome("a") == True
    assert solution.isPalindrome("ab") == False
    assert solution.isPalindrome("aba") == True
    assert solution.isPalindrome("abcba") == True
    assert solution.isPalindrome("ABCBA") == True
    assert solution.isPalindrome("Able was I, ere I saw Elba") == True
    assert solution.isPalindrome("Madam, in Eden, I'm Adam") == True

if __name__ == "__main__":
    pytest.main()
