from .create_noun_basic import create_all_basic_noun_forms
from .create_noun_decl import all_noun_forms


def create_all(noun, proper_name=False):
    nom_sg, gen_sg, nom_pl, gender = create_all_basic_noun_forms(noun)

    res = all_noun_forms(nom_sg, gen_sg, nom_pl, gender, proper_name=proper_name)
    print(res)