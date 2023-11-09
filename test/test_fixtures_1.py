import pytest

# Fixture 1: List of even numbers
@pytest.fixture
def even_numbers():
    return [2, 4, 6, 8, 10]

# Fixture 2: List of odd numbers
@pytest.fixture
def odd_numbers():
    return [1, 3, 5, 7, 9]

# Test function 1: Test sum of even numbers
def test_sum_even_numbers(even_numbers):
    assert sum(even_numbers) == 30

# Test function 2: Test sum of odd numbers
def test_sum_odd_numbers(odd_numbers):
    assert sum(odd_numbers) == 25

# Test function 3: Test if even numbers are greater than odd numbers
def test_even_greater_than_odd(even_numbers, odd_numbers):
    assert max(even_numbers) > max(odd_numbers)
