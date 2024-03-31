from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.article import definite_article, indefinite_article
from ..resources.typing import genders_declensions_type, adj_declension_degree_type


class Article:
    """
    This class creates article, it is an overkill, since it returns already created inflected forms, but added
    for the sake of completion of the API. Instantiate it with one of the articles (has to be nominative singular masculine)

    :param article: ο or ένας
    :type article: str
    """
    def __init__(self, article: str):

        article = convert_to_monotonic(article)
        self.article = article

    def all(self) -> adj_declension_degree_type:
        """
        It returns a dictionary with inflected article forms

        :return: A dictionary of the folloing shape ``{SG: {MASC: {NOM: set(forms), ...}, ...}, ...}``
        :rtype: dict
        """
        if self.article not in ['ο', 'ένας']:
            raise Exception("it's not a Greek article")

        if self.article == 'ο':
            return definite_article
        elif self.article == 'ένας':
            return indefinite_article


