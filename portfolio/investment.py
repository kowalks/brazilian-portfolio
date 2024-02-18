import datetime
from typing import Optional


class Investment:

    def theoretical_price(self, date: Optional[datetime.date] = None):
        raise NotImplementedError
