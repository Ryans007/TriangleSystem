# Membros da Equipe:
# 1. Ryan Soares
# 2. Kevin Ryan
# 3. Luiz Neto
# 4. Gabriel Domingos
# 5. Thiago Barbosa

import pytest
from _class import Triangle

def test_value_not_integer():
    """Testa passando um valor não inteiro"""
    triagle = Triangle(
        2,
        3,
        "a"
    )
    result = triagle.triangle_type()
    expected = "Os números devem ser inteiro."
    assert result == expected

def test_value_not_positive():
    """Testa passando um valor negativo"""
    triagle = Triangle(
        2,
        3,
        -5
    )
    result = triagle.triangle_type()
    expected = "Os números devem ser positivos."
    assert result == expected

def test_triangle_invalid():
    """Testa passando valores inválidos para um triângulo"""
    triagle = Triangle(
        1,
        2,
        5
    )
    result = triagle.triangle_type()
    expected = "Os valores não formam um triângulo."
    assert result == expected

def test_is_quilateral():
    """Teste colocando valores de um triângulo equilátero"""
    triagle = Triangle(
        6,
        6,
        6
    )
    result = triagle.triangle_type()
    expected = "Equilátero"
    assert result == expected

def test_is_isosceles():
    """Teste colocando valores de um triângulo Isósceles"""
    triagle = Triangle(
        7,
        7,
        4
    )
    result = triagle.triangle_type()
    expected = "Isósceles"
    assert result == expected

def test_is_scalene():
    """Teste colocando valores de um triângulo Escaleno"""
    triagle = Triangle(
        3,
        4,
        5
    )
    result = triagle.triangle_type()
    expected = "Escaleno"
    assert result == expected

