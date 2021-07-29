from decimal import Decimal
import re
from typing import Union
from decimal import Decimal

from .Interface import ScraperInterface


class Kabum(ScraperInterface):
    def __init__(self) -> None:
        self._site = "Kabum"

    def _scrape_avail(self) -> bool:
        if self.soup.find("div", attrs={"class": "botao-comprar"}):
            return True
        return False

    def _scrape_price(self) -> Union[float, None]:
        if price := self.soup.find("span", attrs={"class": "preco_desconto"}):
            return Decimal(re.sub(r"[^\d.]", "", price.find("strong").text[2:].strip()))
        return None
