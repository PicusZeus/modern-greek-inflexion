from modern_greek_inflexion.resources.variables import GENDERS


def capitalize_basic_forms(noun_temp: dict) -> dict:
    for key in noun_temp:
        if key not in [GENDERS, "aklito"]:
            noun_temp[key] = ','.join([f.capitalize() for f in noun_temp[key].split(',')])
    return noun_temp

