import datetime
from typing import Optional


class Asset:

    def price(self, date: Optional[datetime.date] = None) -> float:
        raise NotImplementedError
