from modern_greek_inflexion.resources.variables import GENDERS


def capitalize_basic_forms(noun_temp: dict) -> dict:
    for key in noun_temp:
        if key != GENDERS:
            noun_temp[key] = ','.join([f.capitalize() for f in noun_temp[key].split(',')])
    return noun_temp


def put_accent_on_unaccented_forms(forms: dict) -> dict:
    # one syllable words
    for number in forms.keys():
        for case in forms[number].keys():
            f = forms[number][case]
            if not where_is_accent(f) and count_syllables(f) > 1:
                forms[number][case] = put_accent(f, PENULTIMATE)
    return forms