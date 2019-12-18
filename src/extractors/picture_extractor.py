import urllib3

from .base_extractor import BaseExtractor


class PicturesExtractor(BaseExtractor):
    def __init__(
        self,
        parser="html5lib",
        possible_headers=("article-header", "article-navigation-wrapper"),
    ):
        self.parser = parser
        self.possible_headers = possible_headers

    def download_picture(self, raw_page):
        picture_url = self._get_url_of_picture(raw_page)
        if picture_url:
            with open("picture.jpg", "wb") as fp:
                fp.write(urllib3.PoolManager().request("GET", picture_url).data)
            print("Picture downloaded!")
        else:
            print("Can't find article's image!")

    def _get_url_of_picture(self, raw_page):
        for header in self.possible_headers:
            header_data = self._make_soup(
                str(self._make_soup(str(raw_page)).find("div", attrs={"class": header}))
            ).find("img")["src"]
            if header_data:
                return header_data
