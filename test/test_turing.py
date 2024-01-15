from devine_turing import *
import pytest

def test_decomposer():
    assert decomposer(-100) == None
    assert decomposer(99) == None
    assert decomposer(100) == (1, 0, 0)
    assert decomposer(500) == (5, 0, 0)
    assert decomposer(999) == (9, 9, 9)
    assert decomposer(1000) == None
    assert decomposer(2000) == None

def test_somme():
    assert somme(-100, 3, 4) == None
    assert somme(8, -1, 6) == None
    assert somme(0, 9, 9) == True
    assert somme(1, 2, 10) == None
    assert somme(3, 100, 7) == None

def test_divisible():
    assert divisible("toto") == False
    assert divisible(-100) == False
    assert divisible(0) == False
    assert divisible(9)
    assert divisible(100) == False