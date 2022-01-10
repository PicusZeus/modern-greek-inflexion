from .create_noun_basic import create_all_basic_noun_forms
from .create_noun_decl import create_all_noun_forms
from ..helping_functions import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic


def create_all_basic_forms(noun, proper_name=False, gender=None, inflection=None):
    return create_all_basic_noun_forms(noun, gender=gender, inflection=inflection, proper_name=proper_name)


def create_all(noun, proper_name=False, gender=None, inflection=None):
    noun = convert_to_monotonic(noun)
    noun = create_all_basic_noun_forms(noun, gender=gender, proper_name=proper_name, inflection=inflection)
    res = create_all_noun_forms(noun['nom_sg'], noun['gen_sg'], noun['nom_pl'], noun['gender'], proper_name=proper_name)
    res = merging_all_dictionaries(res)

    return res
