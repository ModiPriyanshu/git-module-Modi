import pytest
from read_data import calculate_fibonacci

def test_calculate_fibonacci():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1

def test_fibonacci_standard():
    assert calculate_fibonacci(10) == 55

def test_fibonacci_empty():
    with pytest.raises(ValueError):
        calculate_fibonacci([])

def test_fibonacci_afterignoring_non_numeric():
    with pytest.raises(ValueError):
        calculate_fibonacci('a')

def test_fibonacci_checks_negative_value():
    with pytest.raises(ValueError):
        calculate_fibonacci(-1)

def test_fibonacci_checks_for_FloatingPoint():
    with pytest.raises(ValueError):
        calculate_fibonacci(9.3)
