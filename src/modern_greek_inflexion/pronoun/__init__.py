from .create_pron_basic import create_basic_forms
from .create_pron_decl import create_all_pron_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic


class Pronoun:
    """

    """
    def __init__(self, pronoun: str, strong: bool = True):
        """

        :param pronoun:
        :param strong:
        """
        pron = convert_to_monotonic(pronoun, one_syllable_rule=False)
        self.pronoun = pronoun
        self.strong = strong

    def all(self):
        """

        :return:
        """
        bas_form = create_basic_forms(self.pronoun)
        return create_all_pron_forms(bas_form, strong=self.strong)
