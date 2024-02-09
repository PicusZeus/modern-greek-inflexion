from __future__ import annotations

from icecream import ic

from .create_noun_basic import create_all_basic_forms
from .create_noun_decl import create_all_noun_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic

from .._typing import Gender
from ..resources.resources import NOM_SG, GEN_SG, GENDERS, NOM_PL


class Noun:
    def __init__(self, noun: str, proper_name: bool = False, gender: Gender = None, aklito: bool | str = False):
        self.noun = convert_to_monotonic(noun, one_syllable_rule=False)
        self.proper_name = proper_name
        self.basic_forms = create_all_basic_forms(noun, gender=gender, proper_name=proper_name, aklito=aklito)

    def all(self):
        if self.noun == 'Βάιος':
            ic(self.basic_forms)
        res = create_all_noun_forms(**self.basic_forms, proper_name=self.proper_name)
        return merging_all_dictionaries(res)


def create_all(noun: str, proper_name: bool = False, gender: Gender = None, aklito: bool | str = False) -> dict:
    """
    :param noun: The noun you want to inflect has to be in its basic form, that is in nominative singular, or if it's
     plural only, in plural
    :param proper_name:
    :param gender: If you know the nouns gender, set one. There are 10 possibilities, outside of standard 'fem', 'masc',
     'neut', if you know it's only plural or signular, it can be 'fem_sg', 'fem_pl' itd. It is also possible to set
     gender to 'masc_fem' if the noun happens to be of these two genders. These gender names can be imported as variables
     from `modern_greek_inflexion.resources.variables`. The default value is None, that is the app will try to guess the
     noun's gender.
    :param aklito: If you know that the noun you want to inflect is not declinable, set this flag to True, the default
     value is False.
    :return:
    """
    noun = convert_to_monotonic(noun, one_syllable_rule=False)
    noun_basic_forms = create_all_basic_forms(noun, gender=gender, proper_name=proper_name, aklito=aklito)
    if noun == 'χρόνος':
        ic(noun_basic_forms)
    res = create_all_noun_forms(**noun_basic_forms)

    all_forms = merging_all_dictionaries(res)

    return all_forms
