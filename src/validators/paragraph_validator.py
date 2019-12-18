class ParagraphValidator:
    def __init__(self, prohibit_tags=("<strong>", "<a")):
        self.prohibit_tags = prohibit_tags

    def validate(self, p):
        p_as_text = str(p)
        if self._check_if_contains_unrelated_links(
            p_as_text
        ) or self._check_if_not_clickbait(p):
            return False
        return True

    def _check_if_contains_unrelated_links(self, p_as_text):
        return all([tag in p_as_text for tag in self.prohibit_tags])

    def _check_if_not_clickbait(self, p):
        return self.prohibit_tags[0] in str(p) and p.text.isupper()
