import re
from typing import Union
from decimal import Decimal

from bs4 import BeautifulSoup

from .Interface import ScraperInterface


class Amazon(ScraperInterface):
    def __init__(self) -> None:
        self._site = "Amazon"

    def _scrape_avail(self):
        if self.soup.find("input", attrs={"id": "add-to-cart-button"}):
            return True
        return False

    def _scrape_price(self) -> Union[float, None]:
        if price := self.soup.find(
            "span",
            attrs={"class": "a-size-medium a-color-price priceBlockSavingsString"},
        ):
            return Decimal(re.sub(r"[^\d.]", "", price.text)[2:].strip())
        return None
