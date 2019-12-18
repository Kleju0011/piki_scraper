from abc import ABC

import bs4


class BaseExtractor(ABC):
    def _make_soup(self, text):
        return bs4.BeautifulSoup(text, self.parser)
