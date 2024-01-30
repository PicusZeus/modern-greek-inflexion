from modern_greek_accentuation.accentuation import put_accent, where_is_accent
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.resources import PENULTIMATE


def put_accent_in_all_forms(forms: dict, accent: str) -> dict:
    for num in forms.keys():
        for gender in forms[num].keys():
            for case, form in forms[num][gender].items():
                forms[num][gender][case] = put_accent(form, accent_name=accent, true_syllabification=True)
    return forms


def put_accent_on_unaccented_forms(forms: dict) -> dict:
    if not forms:
        return forms

    for number in forms.keys():
        for gender in forms[number].keys():
            for case in forms[number][gender].keys():
                f = forms[number][gender][case]

                if not where_is_accent(f) and count_syllables(f) > 1:
                    forms[number][gender][case] = put_accent(f, PENULTIMATE)

    return forms

