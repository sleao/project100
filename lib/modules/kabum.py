import re
from typing import Union

from bs4 import BeautifulSoup

from .Interface import ScraperInterface


class Kabum(ScraperInterface):
    def __init__(self) -> None:
        self._site = "Kabum"

    def _scrape_avail(self, sopa: BeautifulSoup = None) -> bool:
        soup = sopa if sopa else self.soup
        if soup.find("div", attrs={"class": "botao-comprar"}):
            return True
        return False

    def _scrape_price(self, sopa: BeautifulSoup = None) -> Union[float, None]:
        soup = sopa if sopa else self.soup
        if price := soup.find("span", attrs={"class": "preco_desconto"}):
            return float(re.sub(",", ".", price.find("strong").text[2:].strip()))
        return None
