import pytest
from main import *


def test_positive_number():
    assert devide(10, 2) == 5


def test_float_result():
    assert devide(7, 2) == 3.5


def test_division_by_zero():
    with pytest.raises(ValueError):
        devide(10, 0)
