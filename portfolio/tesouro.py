import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TesouroDireto:
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


@dataclass
class TesouroDiretoInvestment:
    security: TesouroDireto
    buy_date: datetime.date
    price: float

    def __post_init__(self):
        self.days_to_maturity = (self.security.maturity - self.buy_date).days
        self.annualized_return = self.security.price_to_yield(self.price, self.buy_date)

    def theoretical_price(self, date: Optional[datetime.date] = None) -> float:
        date = date or datetime.date.today()
        return self.security.yield_to_price(self.annualized_return, date)
