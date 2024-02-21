from .create_pron_basic import create_basic_forms
from .create_pron_decl import create_all_pron_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.typing import declension_forms_type


class Pronoun:
    """
    This class creates pronouns
    """
    def __init__(self, pronoun: str, strong: bool = True):
        """

        :param pronoun: nom sg masc
        :param strong: Applicable only for personal pronouns, which can be strong or weak
        """
        pron = convert_to_monotonic(pronoun, one_syllable_rule=False)
        self.pronoun = pronoun
        self.strong = strong

    def all(self) -> declension_forms_type:
        """

        :return: A dictionary {SG: {MASC: {NOM: set(forms), ...}, ...}
        """
        bas_form = create_basic_forms(self.pronoun)
        return create_all_pron_forms(bas_form, strong=self.strong)
