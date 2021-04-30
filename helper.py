import os
import pickle

import requests

SAMPLES_FOLDER = "./tests/samples/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


def to_pickle(site: str, case: str, req: requests.Response):
    dest = os.path.join(SAMPLES_FOLDER, f"{site}_{case}.pickle")
    pickle.dump(req, open(dest, "wb"))


def from_pickle(path) -> requests.Response:
    req = pickle.load(open(path, "rb"))
    return req


def generate_samples(site, valid_url, invalid_url):
    valid_req = requests.get(
        valid_url,
        headers=HEADERS,
    )
    to_pickle(site, "valid", valid_req)

    invalid_req = requests.get(
        invalid_url,
        headers=HEADERS,
    )
    to_pickle(site, "invalid", invalid_req)


if __name__ == "__main__":
    ...
    # valid = r"https://www.kabum.com.br/produto/129359/super-trunfo-dinossauros"
    # invalid = r"https://www.kabum.com.br/produto/128245/console-sony-playstation-5-digital-edition-cfi-1014b"
    # site = "kabum"
    # generate_samples(site, valid, invalid)
