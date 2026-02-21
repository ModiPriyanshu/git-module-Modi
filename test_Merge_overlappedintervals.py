import pytest
from read_data import Merge_overlappedintervals

def test_Merge_overlappedintervals():
    assert Merge_overlappedintervals([[1,3], [2,6], [8,10], [15,18]]) == [[1,6], [8,10], [15,18]]

def test_merge_no_overlap():
    assert Merge_overlappedintervals([[1,2], [3,4]]) == [[1,2], [3,4]]

def test_Merge_overlappedintervals_empty():
    with pytest.raises(ValueError):
        Merge_overlappedintervals([])

def test_Merge_overlappedintervals_invalid_input():
    with pytest.raises(ValueError):
        Merge_overlappedintervals('a')
    
def test_Merge_overlappedintervals_checks_negative_value():
    assert Merge_overlappedintervals([[-3,-1], [-2,2], [8,10], [15,18]]) == [[-3,2], [8,10], [15,18]]

def test_Merge_overlappedintervals_checks_for_FloatingPoint():
    assert Merge_overlappedintervals([[1.6,3.8], [1.87,9.30], [8,10], [15,18]]) == [[1.6,10], [15,18]]