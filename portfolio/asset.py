import datetime
from typing import Optional


class Asset:

    def price(self, *args, date: Optional[datetime.date] = None, **kwargs) -> float:
        raise NotImplementedError
