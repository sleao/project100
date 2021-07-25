from abc import ABC, abstractmethod
from typing import Union
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


@dataclass
class Status:
    """Dataclass for item status."""

    site: str
    url: str
    available: bool
    price: Union[float, None]


class ScraperInterface(ABC):
    def __init__(self, site) -> None:
        self._price = None
        self._avail = None
        self._url = None
        self._site = site

    def set_url(self, url) -> None:
        self._url = url

    @abstractmethod
    def _scrape_avail(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _scrape_price(self) -> None:
        raise NotImplementedError

    def get_status(self) -> Status:
        return Status(
            site=self._site,
            url=self._url,
            available=self.get_avail(),
            price=self.get_price(),
        )

    def get_avail(self) -> bool:
        return self._avail

    def get_price(self) -> float:
        return self._price

    def _get_page(self) -> requests.Response:
        res = requests.get(self._url, headers=HEADERS)
        return res

    def update(self) -> None:
        page = self._get_page()
        self.soup = BeautifulSoup(page.text, "html.parser")
        self._avail = self._scrape_avail()
        self._price = self._scrape_price()
