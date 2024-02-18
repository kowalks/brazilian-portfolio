import datetime

from portfolio.tesouro import TesouroDireto, TesouroDiretoInvestment

tesouro_prefixiado = TesouroDireto(
    maturity=datetime.date(2027, 1, 1),
    face_value=1000,
)

invest = TesouroDiretoInvestment(
    security=tesouro_prefixiado,
)
