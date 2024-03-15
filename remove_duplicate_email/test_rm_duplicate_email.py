import pandas as pd
import pytest
from remove_duplicate import remove_duplicate

@pytest.fixture
def sample_data():
    return [
        [1, 'john@example.com'],
        [2, 'bob@example.com'],
        [3, 'john@example.com']
    ]

def test_remove_duplicate_email(sample_data):
    expected_output = pd.DataFrame(sample_data, columns=['id', 'email']).drop_duplicates(subset=['email'], keep='first')
    assert remove_duplicate(sample_data).equals(expected_output)

if __name__ == "__main__":
    pytest.main()