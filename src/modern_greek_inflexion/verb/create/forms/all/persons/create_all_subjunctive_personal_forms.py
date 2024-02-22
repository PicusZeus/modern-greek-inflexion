from __future__ import annotations

from modern_greek_inflexion.resources.typing import voiceType, personal_forms_type
from modern_greek_inflexion.verb.helpers import compound_alternative_forms
from modern_greek_inflexion.resources.variables import *
from modern_greek_inflexion.verb.create.forms.all.persons.create_all_pers_forms import create_all_pers_forms
from modern_greek_inflexion.verb.recognize import recognize_active_non_past_conjugation


def create_all_subjunctive_personal_forms(verb: list,
                                          voice: voiceType,
                                          active_root_for_imp: str = None) -> dict:
    """
    This function creates all perfect non past personal forms
    :param voice: PASSIVE or ACTIVE
    :param active_root_for_imp: an array of possible roots
    :param verb: an array of non past perfect basic forms
    :param deponens: if deponens set to True
    :return: A dictionary with potentially two keys, under the first one indicative or conjuctive forms,
    under the second imperative forms, if applicable.
    """

    act_verb = pass_verb = None

    sec_pos = IND
    forms = {}

    for v in verb:

        v = v.strip()
        if voice == ACTIVE and v:
            act_verb = v
        elif voice == PASSIVE and v:
            pass_verb = v
        if act_verb:
            con = recognize_active_non_past_conjugation(act_verb, aspect=PERF, tense=FIN, voice=ACTIVE)
            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]

            if con_ind in [CON1_ACT_MODAL, MODAL, CON2_ACT_MODAL]:

                forms_imp = None
            else:
                con_imp = con[CONJUGATION_IMP]

                forms_imp = create_all_pers_forms(con_imp, root)

            forms_ind = create_all_pers_forms(con_ind, root)

        elif pass_verb:
            con = recognize_active_non_past_conjugation(pass_verb, aspect=PERF, tense=FIN, voice=voice)

            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]
            if con_ind in [CON1_ACT_MODAL, MODAL]:
                forms_ind = {SG: {TER: [v]}}
                forms_imp = None
            else:
                forms_ind = create_all_pers_forms(con_ind, root)
                con_imp = con[CONJUGATION_IMP]
                forms_imp = create_all_pers_forms(con_imp, root, active_root=active_root_for_imp)


        else:
            raise ValueError

        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)

    return forms
