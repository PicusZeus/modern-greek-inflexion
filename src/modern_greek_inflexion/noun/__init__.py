from __future__ import annotations

from .create_noun_basic import create_all_basic_forms
from .create_noun_decl import create_all_noun_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.typing import genderType


class Noun:
    def __init__(self, noun: str, proper_name: bool = False, gender: genderType = None, aklito: bool | str = False):
        self.noun = convert_to_monotonic(noun, one_syllable_rule=False)
        self.proper_name = proper_name
        self.basic_forms = create_all_basic_forms(noun, gender=gender, proper_name=proper_name, aklito=aklito)

    def all(self):

        res = create_all_noun_forms(**self.basic_forms, proper_name=self.proper_name)
        return merging_all_dictionaries(res)

