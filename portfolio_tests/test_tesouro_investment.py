import datetime

from portfolio.tesouro import TesouroDireto, TesouroDiretoInvestment


def test_multiple_invests_equals_single(tesouro_prefixado: TesouroDireto):
    invest = TesouroDiretoInvestment(security=tesouro_prefixado)
    invest.invest(1, 1000)
    invest.invest(1, 1000)
    invest.invest(1, 1000)

    invest2 = TesouroDiretoInvestment(security=tesouro_prefixado)
    invest2.invest(3, 1000)

    maturity = tesouro_prefixado.maturity
    for days in range(0, 100, 10):
        date = maturity - datetime.timedelta(days=days)
        assert invest.price(date) == invest2.price(date)

    assert invest.price() == invest2.price()


def test_multiple_invests_at_maturity(tesouro_prefixado_investment: TesouroDiretoInvestment):
    tesouro_prefixado_investment.invest(0.5, 500)
    tesouro_prefixado_investment.invest(1.5, 200)
    tesouro_prefixado_investment.invest(2.5, 400)
    tesouro_prefixado_investment.invest(0.5, 100)

    maturity = tesouro_prefixado_investment.security.maturity
    assert tesouro_prefixado_investment.price(maturity) == 5000
