import pytest

from mymath import add_numbers
from mymath import mult_numbers

def test_add_positive():
    assert add_numbers(1, 2) == 3

def test_add_zero():
    assert add_numbers(1, 0) == 1

def test_add_negative():
    assert add_numbers(4, -100) == -96

def test_add_string__expect_exception():
    with pytest.raises(TypeError):
        add_numbers(4, 'I DO NOT BELONG HERE')

def test_mult_positive():
    assert mult_numbers(1, 2) == 2

def test_mult_zero():
    assert mult_numbers(1, 0) == 0
