from .create_noun_basic import create_all_basic_noun_forms
from .create_noun_decl import all_noun_forms


def create_all(noun, proper_name=False):
    noun = create_all_basic_noun_forms(noun)
    res = all_noun_forms(noun['nom_sg'], noun['gen_sg'], noun['nom_pl'], noun['gender'], proper_name=proper_name)
    return res
