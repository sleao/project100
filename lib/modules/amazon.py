import re
from typing import Union

from bs4 import BeautifulSoup

from .Interface import ScraperInterface


class Amazon(ScraperInterface):
    def __init__(self) -> None:
        self._site = "Amazon"

    def _scrape_avail(self, sopa: BeautifulSoup = None):
        soup = sopa if sopa else self.soup
        if soup.find("input", attrs={"id": "add-to-cart-button"}):
            return True
        return False

    def _scrape_price(self, sopa: BeautifulSoup = None) -> Union[float, None]:
        soup = sopa if sopa else self.soup
        if price := soup.find(
            "span",
            attrs={"class": "a-size-medium a-color-price priceBlockSavingsString"},
        ):
            return float(re.sub(",", ".", price.text)[2:])
        else:
            return None
