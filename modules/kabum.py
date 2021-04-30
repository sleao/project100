import re
from typing import Union

from bs4 import BeautifulSoup

from .Interface import ScraperInterface


class Kabum(ScraperInterface):
    _site = "Kabum"

    def __init__(self) -> None:
        super().__init__(self._site)

    def _scrape_dispo(self, sopa: BeautifulSoup = None) -> bool:
        soup = sopa if sopa else self.soup
        if soup.find("div", attrs={"class": "botao-comprar"}):
            return True
        return False

    def _scrape_preco(self, sopa: BeautifulSoup = None) -> Union[float, None]:
        soup = sopa if sopa else self.soup
        if preco := soup.find("span", attrs={"class": "preco_desconto"}):
            return float(re.sub(",", ".", preco.find("strong").text[2:].strip()))
        return None
