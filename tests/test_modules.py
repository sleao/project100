from decimal import Decimal
from requests import Session
from betamax import Betamax

from lib.modules import Amazon, Kabum

KBM_URLS = {
    "valid": "https://www.kabum.com.br/produto/128561/",
    "invalid": "https://www.kabum.com.br/produto/128245",
}

AMZ_URLS = {
    "valid": "https://www.amazon.com.br/dp/B08JN2VMGX/",
    "invalid": "https://www.amazon.com.br/dp/B08CWG5K2D",
}


def test_kabum_scrape_avail_true():
    session = Session()
    recorder = Betamax(session, cassette_library_dir="tests/cassettes")

    with recorder.use_cassette("kabum_scrape_true"):
        scraper = Kabum()
        scraper.set_url(KBM_URLS["valid"])
        scraper.update()

        assert scraper.get_avail() == True


def test_kabum_scrape_avail_false():
    session = Session()
    recorder = Betamax(session, cassette_library_dir="tests/cassettes")

    with recorder.use_cassette("kabum_scrape_false"):
        scraper = Kabum()
        scraper.set_url(KBM_URLS["invalid"])
        scraper.update()

        assert scraper.get_avail() == False


def test_kabum_scrape_price():
    session = Session()
    recorder = Betamax(session, cassette_library_dir="tests/cassettes")

    with recorder.use_cassette("kabum_scrape_price"):
        scraper = Kabum()
        scraper.set_url(KBM_URLS["valid"])
        scraper.update()

        assert isinstance(scraper.get_price(), Decimal)


def test_amazon_scrape_avail_true():
    session = Session()
    recorder = Betamax(session, cassette_library_dir="tests/cassettes")

    with recorder.use_cassette("amazon_scrape_true"):
        scraper = Amazon()
        scraper.set_url(AMZ_URLS["valid"])
        scraper.update()

        assert scraper.get_avail() == True


def test_amazon_scrape_avail_false():
    session = Session()
    recorder = Betamax(session, cassette_library_dir="tests/cassettes")

    with recorder.use_cassette("amazon_scrape_false"):
        scraper = Amazon()
        scraper.set_url(AMZ_URLS["invalid"])
        scraper.update()

        assert scraper.get_avail() == False


def test_amazon_scrape_price():
    session = Session()
    recorder = Betamax(session, cassette_library_dir="tests/cassettes")

    with recorder.use_cassette("amazon_scrape_price"):
        scraper = Amazon()
        scraper.set_url(AMZ_URLS["valid"])
        scraper.update()

        assert isinstance(scraper.get_price(), Decimal)
