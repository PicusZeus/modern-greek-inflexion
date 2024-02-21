from __future__ import annotations

from modern_greek_inflexion.resources.typing import presentConjugationType
from modern_greek_inflexion.verb.create.forms.basic.create_basic_paratatikos_active import \
    create_basic_paratatikos_active
from modern_greek_inflexion.verb.create.forms.basic.create_basic_paratatikos_passive import \
    create_basic_paratatikos_passive


def create_basic_paratatikos_forms(pres_form: str,
                                   root: str,
                                   pres_conjugation: presentConjugationType,
                                   deponens: bool = False,
                                   not_deponens: bool = True,
                                   modal_act: bool = False,
                                   modal_med: bool = False,
                                   has_passive: set[str] = False,
                                   ) -> str:
    """
    This function creates basic paratatikos forms
    :param pres_form: 1st person sg present simple
    :param root: present tense verb stem
    :param pres_conjugation: present tense conjugation type
    :param deponens: If it's a deponens set to True
    :param not_deponens: If it's not a deponens set to True
    :param modal_act: If it's modal active verb set to True
    :param modal_med: If it's modal passive verb set to True
    :param has_passive: if a verb has a passive voice, set with basic present passive forms
    :return: active and passive basic forms separated by a slash ('/'), if there are multiple forms
    for a voice, then forms separated by a coma.
    """
    paratatikos_basic_forms = None

    if not_deponens:

        pass_par = ''
        if has_passive:
            pass_par = create_basic_paratatikos_passive(pres_form, root, pres_conjugation, has_passive, modal_med)

        act_par = create_basic_paratatikos_active(pres_form, root, pres_conjugation, modal_act)

        paratatikos = '/'.join([act_par, pass_par])

        paratatikos_basic_forms = paratatikos

    elif deponens:

        pass_par = create_basic_paratatikos_passive(pres_form, root, pres_conjugation, has_passive, modal_med)

        if pass_par:
            paratatikos_basic_forms = '/' + pass_par

    elif modal_act:

        parat_act_forms = create_basic_paratatikos_active(pres_form, root, pres_conjugation, modal_act)
        if parat_act_forms:
            paratatikos_basic_forms = parat_act_forms + '/'

    elif modal_med:

        parat_med_forms = create_basic_paratatikos_passive(pres_form, root, pres_conjugation, has_passive, modal_med)
        if parat_med_forms:
            paratatikos_basic_forms = '/' + parat_med_forms

    return paratatikos_basic_forms
