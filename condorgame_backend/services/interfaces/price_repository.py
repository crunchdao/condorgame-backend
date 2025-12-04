from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeAlias

Prices: TypeAlias = list[tuple[int, float]]

class PriceRepository(ABC):

    # todo define resolution type
    @abstractmethod
    def fetch_historical_prices(self, asset, from_: datetime, to: datetime, resolution) -> Prices:
        pass
