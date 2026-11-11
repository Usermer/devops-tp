import pytest

from app import addition, division, moyenne, multiplication, soustraction


def test_addition():
    assert addition(2, 3) == 5


def test_addition_with_negative_numbers():
    assert addition(-2, -3) == -5


def test_addition_with_zero():
    assert addition(7, 0) == 7


def test_addition_with_floats():
    assert addition(2.5, 1.5) == 4.0


def test_soustraction():
    assert soustraction(10, 4) == 6


def test_soustraction_result_can_be_negative():
    assert soustraction(3, 8) == -5


def test_multiplication():
    assert multiplication(6, 7) == 42


def test_multiplication_by_zero():
    assert multiplication(25, 0) == 0


def test_division():
    assert division(10, 4) == 2.5


def test_division_by_zero():
    with pytest.raises(ValueError, match="diviser par zéro"):
        division(10, 0)


def test_moyenne():
    assert moyenne([10, 12, 14]) == 12


def test_moyenne_with_floats():
    assert moyenne([1.5, 2.5]) == 2.0


def test_moyenne_with_empty_list():
    with pytest.raises(ValueError, match="liste ne peut pas être vide"):
        moyenne([])