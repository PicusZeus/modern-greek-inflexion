from modern_greek_accentuation._helpers import AccentType

from modern_greek_accentuation.accentuation import put_accent, where_is_accent
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.resources import PENULTIMATE
from modern_greek_inflexion.resources.typing import genders_declensions_type


def put_accent_on_all_forms(forms: genders_declensions_type, accent: AccentType) -> dict:
    """
    Put stress on all adjective forms
    :param forms: Dictionary {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}
    :param accent: Accent name
    :return: Dictionary {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}
    """
    for num in forms.keys():
        for gender in forms[num].keys():
            for case, form in forms[num][gender].items():
                forms[num][gender][case] = put_accent(form, accent_name=accent, true_syllabification=True)
    return forms


def put_accent_on_unaccented_forms(forms: dict) -> dict:
    """
    Put stress on forms without accent, used for cases where basic forms are single syllables, and so inflected
    two syllable forms needs an accent to be put on them.
    :param forms: Dictionary {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}
    :return: forms: Dictionary {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}
    """
    if not forms:
        return forms

    for number in forms.keys():
        for gender in forms[number].keys():
            for case in forms[number][gender].keys():
                f = forms[number][gender][case]

                if not where_is_accent(f) and count_syllables(f) > 1:
                    forms[number][gender][case] = put_accent(f, PENULTIMATE)

    return forms

