import pytest
from read_data import calculate_mean

def test_mean_standard():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
 # We *assert* that the mean of the above list is 5.5.
 # if the function is implemented correctly, it will pass this test.
 # If not, it will fail and pytest will show us the error.
    assert calculate_mean(numbers) == 5.5
def test_mean_empty():
 # If the list is empty, our code should raise an error (called an exception)
    with pytest.raises(ValueError):
        calculate_mean([])

def test_mean_afterignoring_non_numeric():

    with pytest.raises(TypeError):
        numbers = [1, 2, 'a', 3]
        calculate_mean(numbers)

def test_mean_checks_negative_value():
    numbers = [-4, 2, 8]
    assert calculate_mean(numbers) == 2

def test_mean_checks_for_FloatingPoint():
    numbers = [-3, 4.8, 7.2]
    assert calculate_mean(numbers) == 3

def test_mean_single_value():
    numbers = [20]
    assert calculate_mean(numbers) == 20
