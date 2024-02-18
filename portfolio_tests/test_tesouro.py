import datetime

from portfolio import TesouroDireto


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
