# Brazilian Portfolio
A collection of portfolio tools for Brazilian investors.

## Usage

The `TesouroDireto` class is a representation of an unique `Asset` from brazilian TreasuryDirect program. For now, we only have implemented the logic for fixed interest bound (Tesouro prefixado). See more at [website][1].

```py
import datetime
from portfolio.tesouro import TesouroDireto

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
```

The `TesouroDiretoInvestment` class aggregates multiple orders for the same security. For example, on day 2023-01-01, one may buy the security for R$ 700. One year later, the same person may buy twice the same security for R$ 800.

```py
investment = TesouroDiretoInvestment(security=security)
investment.invest(1, 700, datetime.date(2023, 1, 1))
investment.invest(2, 800, datetime.date(2024, 1, 1))
```

On day 2025-01-01, this person may look at their personal investment account and see the projected portfolio of R$ 2560.54, consisting of R$ 836.76 for the first order and R$ 1723.78 for the second order

```py
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
```

## Intended design

- `Order` class represents a single buy operation in time and may have multiple quantities into it. For example, I may have a BUY transaction of 10 units for an individual price of R$ 10.00 each at day 2024-01-01. 
- `Asset` represents the unit of an order. Is the underlying security I'm buying. For example, it may be a single stock, a single bond, a single share of some mutual fund. It has to have the ability to give the unity price at any given date.
    - `TesouroDireto` asset, at maturity, have its price equal to its face value.
    - Stocks have market prices, which we can see in the internet
    - Cash have its price always constant in time
- `Investment` class happens when we have a specific `Asset` with many `Order`s relative to it. Multiple investments are grouped into a `Portfolio`. 

[1]: https://www.tesourodireto.com.br