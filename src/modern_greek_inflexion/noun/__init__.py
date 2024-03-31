from __future__ import annotations

from .create_noun_basic import create_all_basic_forms
from .create_noun_decl import create_all_noun_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources.typing import genderType, noun_basic_forms, genders_declensions_type


class Noun:
    """
    This class can be used to create noun inflected forms.

    :param noun: A noun in nom sg, or, if it's an only plural noun, then in nom pl
    :type noun: str
    :param proper_name: If you know it's a proper name, set this flag to True (it has influence mainly on masc vocative)
    :type proper_name: bool, optional
    :param gender: If you know the gender of a noun you can add it, the acceptable values are: ``MASC, MASC_PL, MASC_SG, FEM_SG, FEM, FEM_PL, NEUT_SG, NEUT, NEUT_PL, MASC_FEM``
    :type gender: str, optional
    :param aklito: If you know that the noun is indeclinable, set it to True
    :type aklito: bool, optional
    :param basic_forms: If you already have basic forms of a noun, you can supply them in the form of a dictionary with the following structure: ``{NOM_SG: str, GEN_SG: str, NOM_PL: str, GENDER: str, proper_name: bool}``
    :type basic_forms: dict, optional

    """
    def __init__(self, noun: str,
                 proper_name: bool = False,
                 gender: genderType = None,
                 aklito: bool | str = False,
                 basic_forms: noun_basic_forms = None):

        self.noun = convert_to_monotonic(noun, one_syllable_rule=False)
        self.proper_name = proper_name
        if not basic_forms:
            self.basic_forms = create_all_basic_forms(noun, gender=gender, proper_name=proper_name, aklito=aklito)
        else:
            self.basic_forms = basic_forms

    def all(self) -> genders_declensions_type:

        """
        Create all the inflected forms as a dictionary

        :return: A dictionary with the following shape: ``{SG: {MASC: {NOM: set(forms), ...}, ...}``
        :rtype: dict
        """

        res = create_all_noun_forms(**self.basic_forms, proper_name=self.proper_name)
        return merging_all_dictionaries(res)

