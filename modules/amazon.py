import re
from typing import Union

from bs4 import BeautifulSoup

from .Interface import ScraperInterface


class Amazon(ScraperInterface):
    _site = "Amazon"

    def __init__(self) -> None:
        super().__init__(self._site)

    def _scrape_dispo(self, sopa: BeautifulSoup = None):
        soup = sopa if sopa else self.soup
        if soup.find("input", attrs={"id": "add-to-cart-button"}):
            return True
        return False

    def _scrape_preco(self, sopa: BeautifulSoup = None) -> Union[float, None]:
        soup = sopa if sopa else self.soup
        if preco := soup.find(
            "span",
            attrs={"class": "a-size-medium a-color-price priceBlockSavingsString"},
        ):
            return float(re.sub(",", ".", preco.text)[2:])
        else:
            return None
