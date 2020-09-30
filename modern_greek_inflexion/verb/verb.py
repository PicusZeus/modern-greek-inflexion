from .create_verb_list import create_all_basic_forms
from .create_verb_forms import create_all_imperfect_personal_forms

def create_basic_forms(verb):
    return create_all_basic_forms(verb)


def create_all_forms(verb):
    basic_forms = create_all_basic_forms(verb)
    deponens = False
    "present"
    present_basic_forms = basic_forms['present']
    print(present_basic_forms)
    try:
        pres_act_forms = create_all_imperfect_personal_forms(present_basic_forms['active'], 'active')
        pres_passive_forms = create_all_imperfect_personal_forms(present_basic_forms['passive'], 'passive')
        present = (pres_act_forms, pres_passive_forms)

    except:
        pres_passive_forms = create_all_imperfect_personal_forms(present_basic_forms['passive'], 'passive')
        present = (pres_passive_forms,)
        deponens = True


    'conjunctive'
    try:
        conjunctive_basic_forms = basic_forms['conjunctive']

    conjunctive = {}

    aorist = {}

    paratatikos = {}

    act_pres_participle = {}

    arch_act_pres_participle = {}

    pass_pres_participle = {}

    active_aorist_participle = {}

    passive_perfect_participle = {}

    passive_aorist_participle = {}



    return {'present': present}