from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.article import definite_article, indefinite_article
from ..resources.typing import declension_forms_type


class Article:
    """
    This class creates articles, it is of course overkill, since it returns preexisting inflected forms, but added
    for the sake of completion of the API
    """
    def __init__(self, article: str):
        """
        :param article: ο or ένας
        """
        article = convert_to_monotonic(article)
        self.article = article

    def all(self) -> declension_forms_type:
        """
        It returns existing dictionary with inflected article
        :return: A dictionary {ADJ: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...},
        """
        if self.article not in ['ο', 'ένας']:
            raise Exception("it's not a Greek article")

        if self.article == 'ο':
            return definite_article
        elif self.article == 'ένας':
            return indefinite_article


