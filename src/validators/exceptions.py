class InvalidUrlException(Exception):

    template = "Given article address {} is not belong to {} service!"

    def __init__(self, given_url, proper_url):
        super().__init__(self.template.format(given_url, proper_url))
