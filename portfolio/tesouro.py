import datetime
from dataclasses import dataclass, field
from typing import List, Optional

from portfolio.asset import Asset
from portfolio.investment import Investment
from portfolio.order import Order


@dataclass(frozen=True)
class TesouroDireto(Asset):
    maturity: datetime.date
    face_value: float

    def price_to_yield(self, price: float, date: Optional[datetime.date] = None) -> float:
        if price < 0:
            raise ValueError('Price must be non-positive')

        date = date or datetime.date.today()
        days_to_maturity = (self.maturity - date).days

        if days_to_maturity == 0 and price == self.face_value:
            return 0

        try:
            return (self.face_value / price) ** (365 / days_to_maturity) - 1
        except ZeroDivisionError:
            return float('inf')

    def yield_to_price(self, yield_: float, date: Optional[datetime.date] = None) -> float:
        if yield_ < -1:
            raise ValueError('Minimum yield is -100%')

        date = date or datetime.date.today()
        days_to_maturity = (self.maturity - date).days
        return self.face_value / (1 + yield_) ** (days_to_maturity / 365)

    def price(self, base_date: datetime.date, base_price: float, date: Optional[datetime.date] = None) -> float:
        date = date or datetime.date.today()
        yield_ = self.price_to_yield(base_price, base_date)
        return self.yield_to_price(yield_, date)


@dataclass
class TesouroDiretoInvestment(Investment):
    security: TesouroDireto
    orders: List[Order] = field(default_factory=list)

    def price(self, date: Optional[datetime.date] = None) -> float:
        return sum(order.qty * self.security.price(order.date, order.price, date) for order in self.orders)
