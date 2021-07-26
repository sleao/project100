from lib.modules import ScraperInterface, Kabum, Amazon
from datetime import datetime

TIME_FORMAT = "%B %d, %Y - %H:%M:%S"

URL_PS5_KBM = r"https://www.kabum.com.br/produto/128245/console-sony-playstation-5-digital-edition-cfi-1014b"
URL_PS5_AMZ = (
    r"https://www.amazon.com.br/Console-PlayStation-5-Digital-Edition/dp/B08CWG5K2D"
)


class ScraperManager:
    """This class manages the Scrapers"""

    def __init__(self) -> None:
        self._modules: list[ScraperInterface] = []
        self.lastUpdate = datetime.now()

    def _setup_module(self, module: ScraperInterface, url: str):
        """Instantiates a module and updates it"""
        m: ScraperInterface = module()
        m.set_url(url)
        m.update()
        return m

    def add_module(self, module: ScraperInterface, url: str):
        """Add a new ScraperInterface module"""
        m = self._setup_module(module, url)
        self._modules.append(m)

    def run_all(self):
        """Updates all the instantiated modules"""
        for mod in self._modules:
            mod.update()
        self.lastUpdate = datetime.now()

    def get_status(self):
        """Returns both availability and price"""
        return (
            [(m.get_status()) for m in self._modules],
            self.lastUpdate.strftime(TIME_FORMAT),
        )

    def get_avails(self):
        """Returns the item availability in every store"""
        return [(m.get_avail()) for m in self._modules]

    def get_prices(self):
        """Returns the item price in every store"""
        return [(m.get_price()) for m in self._modules]


def setup() -> ScraperManager:
    p = ScraperManager()
    # setup modules
    p.add_module(Kabum, URL_PS5_KBM)
    p.add_module(Amazon, URL_PS5_AMZ)
    return p
