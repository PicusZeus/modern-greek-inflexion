from .create_verb_list import create_all_basic_forms
from .create_verb_forms import create_all_imperfect_personal_forms, create_all_perf_non_past_personal_forms
from .greek_tables import deponens_with_active_perf_forms

def create_basic_forms(verb):
    return create_all_basic_forms(verb)


def create_all_forms(verb):
    basic_forms = create_all_basic_forms(verb)
    # print(basic_forms)
    deponens = False

    all_forms = {}

    "present"
    present = {}

    present_basic_forms = basic_forms['present']
    # print(present_basic_forms)
    if 'active' in present_basic_forms:
        pres_act_forms = create_all_imperfect_personal_forms(present_basic_forms['active'], 'active')
        present['active'] = pres_act_forms
    if 'passive' in present_basic_forms:
        pres_passive_forms = create_all_imperfect_personal_forms(present_basic_forms['passive'], 'passive')
        present['passive'] = pres_passive_forms

        if not 'active' in present_basic_forms:
            deponens = True
    all_forms['present'] = present
    'conjunctive'
    # try:
    conjunctive_basic_forms = basic_forms['conjunctive']
    # print(conjunctive_basic_forms, 'SYNERXOMAI')
    conjunctive = {}
    active_root = None
    if 'active' in conjunctive_basic_forms:
        con_active_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms['active'], 'active')
        active_root=list(conjunctive_basic_forms['active'])[0][:-1]
        conjunctive['active'] = con_active_forms
    if 'passive' in conjunctive_basic_forms:

        con_passive_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms['passive'], 'passive', active_root_for_imp=active_root, deponens=deponens)

        if verb in deponens_with_active_perf_forms:
            conjunctive['active'] = con_passive_forms
            print(con_passive_forms)
        else:
            conjunctive['passive'] = con_passive_forms

    all_forms['conjunctive'] = conjunctive
    # except Exception as e:
    #     print(e)
    #     pass

    conjunctive = {}

    aorist = {}

    paratatikos = {}

    act_pres_participle = {}

    arch_act_pres_participle = {}

    pass_pres_participle = {}

    active_aorist_participle = {}

    passive_perfect_participle = {}

    passive_aorist_participle = {}



    return all_forms