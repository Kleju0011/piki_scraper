import datetime

import urllib3

from .article_extractor import ArticleExtractor
from .base_extractor import BaseExtractor
from .picture_extractor import PicturesExtractor


class SiteExtractor(BaseExtractor):
    def __init__(
        self,
        is_title=None,
        is_date=False,
        is_picture=False,
        parser="html5lib",
        last_lines_with_trash=-4,
        article_extractor=ArticleExtractor,
        picture_extractor=PicturesExtractor,
    ):
        self.is_title = is_title
        self.is_date = is_date
        self.is_picture = is_picture
        self.parser = parser
        self.last_lines_with_trash = last_lines_with_trash
        self.article_extractor = article_extractor()
        self.picture_extractor = picture_extractor()

    def extract_data(self, url):
        raw_page = urllib3.PoolManager().request("GET", url).data
        data_to_return = {"article": self.article_extractor.get_article(raw_page)}
        if self.is_title:
            data_to_return["title"] = self._get_title(raw_page)
        if self.is_picture:
            self.picture_extractor.download_picture(raw_page)
        if self.is_date:
            data_to_return["date"] = self._get_date(raw_page)
        return data_to_return

    def _get_date(self, raw_data):
        line_with_data = self._make_soup(str(raw_data)).find(
            "div", attrs={"class": "article-date"}
        )
        if self._make_soup(str(line_with_data)).find("time"):
            return self._make_soup(str(line_with_data)).find("time")["datetime"]
        return str(datetime.datetime.today().date())

    def _get_title(self, raw_data):
        return (
            self._make_soup(raw_data).find("h1", attrs={"class": "page-heading"}).text
        )
