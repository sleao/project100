import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


class ScraperMeta(type):
    def __instancecheck__(cls, instance: any) -> bool:
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass: type) -> bool:
        return (
            hasattr(subclass, "_scrape_dispo")
            and callable(subclass._scrape_dispo)
            and hasattr(subclass, "_scrape_preco")
            and callable(subclass._scrape_preco)
        )


class ScraperInterface(metaclass=ScraperMeta):
    def __init__(self, site) -> None:
        self._preco = None
        self._dispo = None
        self._url = None
        self._site = site

    def __str__(self) -> str:
        resp = (
            f"{self._site} - Disponível: {self._preco}"
            if self._dispo
            else f"{self._site} - Indisponível"
        )
        return f"{resp}"

    def __repr__(self) -> str:
        resp = (
            f"{self._site} - Disponível: {self._preco}"
            if self._dispo
            else f"{self._site} - Indisponível"
        )
        return f"{resp}"

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    
    @property
    def produto(self):
        return self._produto

    @produto.setter
    def produto(self, value):
        self._produto = value

    @property
    def preco(self):
        return self._preco

    @property
    def dispo(self):
        return self._dispo

    def update(self):
        self.soup = BeautifulSoup(
            requests.get(self.url, headers=HEADERS).text, "html.parser"
        )
        self._dispo = self._scrape_dispo()
        self._preco = self._scrape_preco()
