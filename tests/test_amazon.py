import os
import re

from bs4 import BeautifulSoup
from helper_functions import SAMPLES_FOLDER, from_pickle
from lib.modules import Amazon


class TestAmazon:
    valid_soup = BeautifulSoup(
        from_pickle(os.path.join(SAMPLES_FOLDER, "amazon_valid.pickle")).text,
        "html.parser",
    )
    invalid_soup = BeautifulSoup(
        from_pickle(os.path.join(SAMPLES_FOLDER, "amazon_invalid.pickle")).text,
        "html.parser",
    )
    amz = Amazon()

    def test_dispo_sim(self):
        expected_dispo = True
        real_dispo = self.amz._scrape_avail(self.valid_soup)
        assert expected_dispo == real_dispo, "Dispo deve ser true"

    def test_dispo_nao(self):
        expected_dispo = False
        real_dispo = self.amz._scrape_avail(self.invalid_soup)
        assert expected_dispo == real_dispo, "Dispo deve ser false"

    def test_preco_sim(self):
        real_preco = self.amz._scrape_price(self.valid_soup)
        assert isinstance(real_preco, float)
