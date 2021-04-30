from modules import Amazon, Kabum, ScraperInterface
import modules

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


class ScraperPai:
    def __init__(self) -> None:
        self._products = {}

    def _validate_module(self, module: ScraperInterface):
        if issubclass(module, ScraperInterface):
            return True
        else:
            raise (Exception("não"))

    def _setup_module(self, module: ScraperInterface, produto: str, url: str):
        m = module()
        m.url = url
        m.update()
        return m

    def add_module(self, module: ScraperInterface, produto: str, url: str):
        if self._validate_module(module):
            if not self._products.get(produto):
                self.add_product(produto)
            m = self._setup_module(module, produto, url)
            site = module._site
            self._products[produto][site] = m

    def add_product(self, product):
        if not self._products.get(product):
            self._products[product] = {}

    # def run_all(self):
        # for _, mod in self._modules.items():
            # mod.update()

    # def return_dispos(self):
    #     return [(site, m.get_dispo()) for site, m in self._modules.items()]

    # def return_precos(self):
    #     return [(site, m.get_preco()) for site, m in self._modules.items()]


if __name__ == "__main__":
    url_ps5_kbm = r"https://www.kabum.com.br/produto/128245/console-sony-playstation-5-digital-edition-cfi-1014b"
    url_ps5_amz = (
        r"https://www.amazon.com.br/Console-PlayStation-5-Digital-Edition/dp/B08CWG5K2D"
    )
    p = ScraperPai()
    p.add_module(Kabum, 'Playstation 5', url_ps5_kbm)
    p.add_module(Amazon, 'Playstation 5', url_ps5_amz)
    # print(p.return_dispos())

# r"https://www.magazineluiza.com.br/console-playstation-5-digital-edition-ps5-sony/p/043079600/ga/gps5/"
