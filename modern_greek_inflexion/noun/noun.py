from .create_noun_basic import create_all_basic_noun_forms
from .create_noun_decl import create_all_noun_forms
from ..helping_functions import merging_all_dictionaries


def create_all_basic_forms(noun, proper_name=False, proper_name_gender=None):
    return create_all_basic_noun_forms(noun, proper_name_gender=proper_name_gender, proper_name=proper_name)

def create_all(noun, proper_name=False, proper_name_gender=None):
    noun = create_all_basic_noun_forms(noun, proper_name_gender=proper_name_gender, proper_name=proper_name)
    res = create_all_noun_forms(noun['nom_sg'], noun['gen_sg'], noun['nom_pl'], noun['gender'], proper_name=proper_name)
    res = merging_all_dictionaries(res)

    return res
