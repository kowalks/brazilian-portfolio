import datetime

from portfolio.tesouro import TesouroDireto, TesouroDiretoInvestment

if __name__ == '__main__':

    # Tesouro Prefixado 2027 bond
    security = TesouroDireto(
        maturity=datetime.date(2027, 1, 1),
        face_value=1000,
    )

    # implied annual compound return when buying one year before maturity
    # at R$ 500 price.
    yield_ = security.price_to_yield(
        price=500,
        date=datetime.date(2026, 1, 1),
    )
    print(yield_)  # 1.0

    # theoretical price for security on 2026-07-01
    price = security.price(
        base_date=datetime.date(2026, 1, 1),
        base_price=500,
        date=datetime.date(2026, 7, 1),
    )
    print(price)  # 705.0954182187305

    investment = TesouroDiretoInvestment(security=security)
    investment.invest(1, 700, datetime.date(2023, 1, 1))
    investment.invest(2, 800, datetime.date(2024, 1, 1))

    price = investment.price(datetime.date(2025, 1, 1))
    print(price)  # 2560.54386860047

    first_order_price = security.price(
        base_date=datetime.date(2023, 1, 1),
        base_price=700,
        date=datetime.date(2025, 1, 1)
    )
    print(first_order_price)  # 836.7621599638865

    second_order_price = 2 * security.price(
        base_date=datetime.date(2024, 1, 1),
        base_price=800,
        date=datetime.date(2025, 1, 1)
    )
    print(second_order_price)  # 1723.7817086365837
