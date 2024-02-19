"""
simply a list
"""
from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.article import definite_article, indefinite_article
from ..resources.typing import adjective_basic_forms


class Article:
    def __init__(self, article: str):
        article = convert_to_monotonic(article)
        self.article = article

    def all(self) -> adjective_basic_forms:
        if self.article not in ['ο', 'ένας']:
            raise Exception("it's not a Greek article")
        """
        So that API is consistent
        :param article: o or enas
        :return:
        """
        if self.article == 'ο':
            return definite_article
        elif self.article == 'ένας':
            return indefinite_article


