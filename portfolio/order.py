import datetime
from dataclasses import dataclass


@dataclass
class Order:
    qty: float
    price: float
    date: datetime.date

    @property
    def total_price(self):
        return self.qty * self.price
