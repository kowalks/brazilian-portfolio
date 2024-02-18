import datetime

import pytest

from portfolio.tesouro import TesouroDireto, TesouroDiretoInvestment


@pytest.fixture
def tesouro_prefixado():
    return TesouroDireto(
        maturity=datetime.date(2027, 1, 1),
        face_value=1000,
    )

@pytest.fixture
def tesouro_prefixado_investment(tesouro_prefixado):
    return TesouroDiretoInvestment(security=tesouro_prefixado)
