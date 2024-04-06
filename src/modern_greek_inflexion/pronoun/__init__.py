from .create_pron_basic import create_basic_forms
from .create_pron_decl import create_all_pron_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.typing import genders_declensions_type


class Pronoun:
    """
    This class can be used to create pronouns

    :param pronoun: Has to be nominative singular masculine, if it's an adjectival pronoun, otherwise, if adverbial, there is only one form.
    :type pronoun: str
    :param strong: Applicable only for personal pronouns, which can be strong or weak, defaults to True.
    :type strong: bool, optional
    """
    def __init__(self, pronoun: str, strong: bool = True):

        pronoun = convert_to_monotonic(pronoun, one_syllable_rule=False)
        self.pronoun = pronoun
        self.strong = strong

    def all(self) -> genders_declensions_type:
        """
        This method should be used to generate all the inflected forms

        :return: A dictionary with the following shape ``{SG: {MASC: {NOM: set(forms), ...}, ...}``. If the pronoun is adverbial, the shape is the same, but the values of grammatical variables are all 'nd': ``{'nd': {'nd': {'nd': {'πού'}}}}``
        :rtype: dict
        """
        bas_form = create_basic_forms(self.pronoun)

        return create_all_pron_forms(bas_form, strong=self.strong)

