import unittest

from encryptApp import ceasar


def test_encrypt():
    assert ceasar("password",3) == 'sdvvzrug'
    assert ceasar("Zapzap",1) == 'Abqabq' 
    assert ceasar("Test Space",1) == 'Uftu Tqbdf' 
