from devine_steve import *
import pytest

def test_decomposer():
    assert decomposer(-100) == False
    assert decomposer(99) == False
    assert decomposer(100) == (1, 0, 0)
    assert decomposer(500) == (5, 0, 0)
    assert decomposer(999) == (9, 9, 9)
    assert decomposer(1000) == False
    assert decomposer(2000) == False

def test_somme():
    assert somme(-100, 3, 4) == False
    assert somme(8, -1, 6) == False
    assert somme(0, 9, 9) == True
    assert somme(1, 2, 10) == False
    assert somme(3, 100, 7) == False

def test_divisible():
    assert divisible("toto") == False
    assert divisible(-100) == False
    assert divisible(0) == False
    assert divisible(9)
    assert divisible(100) == False