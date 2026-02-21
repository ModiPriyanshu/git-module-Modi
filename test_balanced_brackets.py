import pytest
from read_data import Balanced_brackets

def test_balanced_brackets():
    assert Balanced_brackets('{[()]}') == True
    assert Balanced_brackets('{[(])}') == False

def test_balanced_brackets_empty():
    with pytest.raises(ValueError):
        Balanced_brackets([])

def test_balanced_brackets_simplepai():
    assert Balanced_brackets('()') == True
    assert Balanced_brackets('{}') == True
    assert Balanced_brackets('[]') == True

def test_balanced_brackets_checks_allpossible_wrong_brackets():
    assert Balanced_brackets('(') == False
    assert Balanced_brackets(')') == False
    assert Balanced_brackets('{') == False
    assert Balanced_brackets('}') == False
    assert Balanced_brackets('[') == False
    assert Balanced_brackets(']') == False