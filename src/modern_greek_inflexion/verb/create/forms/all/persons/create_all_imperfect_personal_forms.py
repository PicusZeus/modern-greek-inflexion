from modern_greek_inflexion.verb.helpers import compound_alternative_forms
from modern_greek_inflexion.resources import ACTIVE, PASSIVE, IND, ROOT, CONJUGATION_IND, CONJUGATION_IMP, \
    CON1_ACT_MODAL, SG, TER, MODAL
from modern_greek_inflexion.verb.create.forms.all.persons.create_all_pers_forms import create_all_pers_forms
from modern_greek_inflexion.verb.recognize import recognize_active_non_past_conjugation, \
    recognize_passive_present_continuous_conjugation


def create_all_imperfect_personal_forms(verb: str, voice: str) -> tuple[dict, str]:
    """
    :param verb: it needs to be an array or set of alternative forms, active or passive,
    :param voice: voice has to be active or passive.
    :return: a dictionary {'voice': voice, 'sec_pos': secondary POS (here ind for indicative), 'forms_ind': all forms in a dictionary, 'forms_imp': all imper forms in a dictionary}
    """
    act_verbs = pass_verbs = None

    if voice == ACTIVE:
        act_verbs = verb
    elif voice == PASSIVE:
        pass_verbs = verb
    else:
        print('voice can be only passive or active')
        raise ValueError

    sec_pos = IND
    forms = None
    con_ind = None

    for v in verb:

        if act_verbs:
            voice = ACTIVE
            sec_pos = IND
            v = v.strip()
            # to be safe, sometimes list, especially if created manually, can have some white spaces
            con = recognize_active_non_past_conjugation(v, voice=voice)

            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]
            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con[CONJUGATION_IMP]
            forms_imp = create_all_pers_forms(con_imp, root)

            if con_ind == CON1_ACT_MODAL:
                forms_ind = {SG: {TER: [v]}}
                forms_imp = None
            if forms_imp == MODAL:
                forms_imp = None

        elif pass_verbs:

            con = recognize_passive_present_continuous_conjugation(v)

            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]
            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con[CONJUGATION_IMP]
            forms_imp = create_all_pers_forms(con_imp, root)

            if forms_ind == MODAL:
                forms_ind = {SG: {TER: [v]}}
                forms_imp = None
        else:
            raise ValueError

        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)
    return forms, con_ind
