import datetime

import pytest

from portfolio import TesouroDireto, TesouroDiretoInvestment


@pytest.fixture
def tesouro_prefixado():
    return TesouroDireto(
        maturity=datetime.date(2027, 1, 1),
        face_value=1000,
    )

@pytest.fixture
def investimento_prefixado_2027(tesouro_prefixado: TesouroDireto):
    return TesouroDiretoInvestment(
        security=tesouro_prefixado,
        buy_date=datetime.date(2024, 2, 16),
        price=759.05,
    )

def test_price_at_zero_yield(tesouro_prefixado: TesouroDireto):
    face_value = tesouro_prefixado.face_value
    assert tesouro_prefixado.yield_to_price(0.0) == face_value

def test_price_at_maturity(tesouro_prefixado: TesouroDireto):
    face_value = tesouro_prefixado.face_value
    maturity = tesouro_prefixado.maturity
    for yield_ in range(0, 100):
        assert tesouro_prefixado.yield_to_price(yield_/100, maturity) == face_value

def test_yield_at_zero_price(tesouro_prefixado: TesouroDireto):
    date = datetime.date(2024, 2, 16)
    assert tesouro_prefixado.price_to_yield(0, date) == float('inf')

def test_yield_at_face_value(tesouro_prefixado: TesouroDireto):
    face_value = tesouro_prefixado.face_value
    assert tesouro_prefixado.price_to_yield(face_value) == 0.0

def test_yield_at_maturity(tesouro_prefixado: TesouroDireto):
    face_value = tesouro_prefixado.face_value
    maturity = tesouro_prefixado.maturity
    assert tesouro_prefixado.price_to_yield(face_value, maturity) == 0.0