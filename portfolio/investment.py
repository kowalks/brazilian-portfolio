import datetime
from typing import List, Optional

from portfolio.asset import Asset
from portfolio.order import Order


class Investment:
    security: Asset
    orders: List[Order] = []

    def invest(self, quantity: float, price: float, date: Optional[datetime.date] = None):
        date = date or datetime.date.today()
        self.orders.append(Order(quantity, price, date))

    def total_price(self) -> float:
        return sum(investment.total_price for investment in self.orders)

    def price(self, date: Optional[datetime.date] = None) -> float:
        raise NotImplementedError
