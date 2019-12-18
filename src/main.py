import json

import click

from extractors.site_extractor import SiteExtractor
from validators.url_validator import UrlValidator


class ArticlesScraper:
    def __init__(
        self,
        is_json=None,
        is_file=None,
        is_title=None,
        is_date=False,
        is_picture=False,
        url_validator=UrlValidator,
        extractor=SiteExtractor,
    ):
        self.url_validator = url_validator()
        self.site_extractor = extractor(is_title, is_date, is_picture)
        self.is_json = is_json
        self.is_file = is_file

    def get_article_from_given_url(self, url):
        if self.url_validator.is_correct(url):
            article = self.site_extractor.extract_data(url)
            if self.is_json:
                return self._prepare_json(article)
            return self._prepare_text(article)

    def _prepare_file(self, file_extension, article):
        with open(f"article_output.{file_extension}", "w+") as file:
            file.write(article)
        return f"Results has been saved to file in {file_extension} format."

    def _prepare_json(self, article):
        if self.is_file:
            self._prepare_file("json", json.dumps(article))
        return article

    def _prepare_text(self, article):
        text = ""
        for key, content in article.items():
            text += f"{key}:\t{content}\n"
        if self.is_file:
            self._prepare_file("txt", text)
        return text


@click.command()
@click.option("-url", help="Url with article to extract", required=True)
@click.option("-j", help="Get ouput in Json format.", is_flag=True)
@click.option("-f", help="Save output to file.", is_flag=True)
@click.option("-t", help="Get article with title.", is_flag=True)
@click.option("-d", help="Get article with published date.", is_flag=True)
@click.option("-p", help="Get article with picture.", is_flag=True)
def main(url, j, f, t, d, p):
    print(
        ArticlesScraper(
            is_json=j, is_file=f, is_title=t, is_date=d, is_picture=p
        ).get_article_from_given_url(url)
    )


if __name__ == "__main__":
    main()
