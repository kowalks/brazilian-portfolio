import datetime
from typing import List, Optional

from portfolio.asset import Asset
from portfolio.order import Order


class Investment:
    security: Asset
    orders: List[Order] = []

    def invest(self, quantity: float, price: float, date: Optional[datetime.date] = None) -> Order:
        date = date or datetime.date.today()
        order = Order(quantity, price, date)
        self.orders.append(order)
        return order

    def total_price(self) -> float:
        return sum(investment.total_price for investment in self.orders)

    def price(self, date: Optional[datetime.date] = None) -> float:
        raise NotImplementedError
