from .exceptions import InvalidUrlExcpetion


class UrlValidator:
    def __init__(self, root_address="https://pikio.pl"):
        self.root_address = root_address

    def is_correct(self, url):
        if self.root_address not in url:
            raise InvalidUrlExcpetion(url, self.root_address)
        return True
