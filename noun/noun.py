from .create_noun_basic import create_all_basic_noun_forms
from .create_noun_decl import create_all_noun_forms


def create_all(noun, proper_name=False, proper_name_gender=None):
    noun = create_all_basic_noun_forms(noun, proper_name_gender=proper_name_gender)
    res = create_all_noun_forms(noun['nom_sg'], noun['gen_sg'], noun['nom_pl'], noun['gender'], proper_name=proper_name)
    return res
