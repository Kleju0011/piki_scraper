from validators.paragraph_validator import ParagraphValidator
from .base_extractor import BaseExtractor


class ArticleExtractor(BaseExtractor):
    def __init__(
        self,
        parser="html5lib",
        last_lines_with_trash=-4,
        paragraph_validator=ParagraphValidator,
    ):
        self.parser = parser
        self.last_lines_with_trash = last_lines_with_trash
        self.validator = paragraph_validator()

    def get_article(self, raw_page):
        article = self._get_only_part_with_article(raw_page)
        paragraph = self._get_paragraph_without_class(str(article))
        validated_paragraph = " ".join(
            [
                p.text
                for p in paragraph[: self.last_lines_with_trash]
                if self.validator.validate(p)
            ]
        )
        return validated_paragraph

    def _get_only_part_with_article(self, raw_page):
        return self._make_soup(raw_page).find_all(
            "div", attrs={"class": "article-container"}
        )

    def _get_paragraph_without_class(self, raw_page):
        return self._make_soup(raw_page).find_all("p", attrs={"class": None})
