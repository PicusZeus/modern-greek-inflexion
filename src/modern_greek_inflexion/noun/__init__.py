from __future__ import annotations

from .create_noun_basic import create_all_basic_noun_forms
from .create_noun_decl import create_all_noun_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources.resources import NOM_SG, GEN_SG, GENDER, NOM_PL


def create_all_basic_forms(noun: str, proper_name: bool = False, gender: str | None = None,
                           aklito: bool | str = False) -> dict:
    return create_all_basic_noun_forms(noun, gender=gender, aklito=aklito, proper_name=proper_name)


def create_all(lemma: str, proper_name: bool = False, gender: str | None = None, aklito: bool | str = False) -> dict:
    noun = convert_to_monotonic(lemma, one_syllable_rule=False)
    noun = create_all_basic_noun_forms(noun, gender=gender, proper_name=proper_name, aklito=aklito)

    res = create_all_noun_forms(noun[NOM_SG], noun[GEN_SG], noun[NOM_PL], noun[GENDER], proper_name=proper_name)

    res = merging_all_dictionaries(res)

    return res
