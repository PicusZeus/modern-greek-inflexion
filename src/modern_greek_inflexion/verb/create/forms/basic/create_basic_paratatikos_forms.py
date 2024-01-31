from __future__ import annotations

from modern_greek_inflexion.verb.create.forms.basic.create_basic_paratatikos_active import \
    create_basic_paratatikos_active
from modern_greek_inflexion.verb.create.forms.basic.create_basic_paratatikos_passive import \
    create_basic_paratatikos_passive


def create_basic_paratatikos_forms(pres_form: str, root: str, pres_conjugation: str, deponens: bool = False,
                                   not_deponens: bool = True, modal_act: bool = False,
                                   modal_med: bool = False, has_passive: bool = True,
                                   alternative: bool = False) -> str | None:
    paratatikos_basic_forms = None

    if not_deponens:

        pass_par = ''
        if has_passive:
            pass_par = create_basic_paratatikos_passive(pres_form, root, pres_conjugation, modal_med, alternative)
        act_par = create_basic_paratatikos_active(pres_form, root, pres_conjugation, modal_act, alternative)

        paratatikos = '/'.join([act_par, pass_par])

        paratatikos_basic_forms = paratatikos

    elif deponens:

        # pass_par = set(pass_par)
        pass_par = create_basic_paratatikos_passive(pres_form, root, pres_conjugation, modal_med, alternative)
        # if root[-3:] == 'ποι':
        #     pass_par = root + 'ούμουν,' + root + 'όμουν'
        if pass_par:
            paratatikos_basic_forms = '/' + pass_par

    elif modal_act:

        parat_act_forms = create_basic_paratatikos_active(pres_form, root, pres_conjugation, modal_act, alternative)
        if parat_act_forms:
            paratatikos_basic_forms = parat_act_forms + '/'

    elif modal_med:

        parat_med_forms = create_basic_paratatikos_passive(pres_form, root, pres_conjugation, modal_med, alternative)
        if parat_med_forms:
            paratatikos_basic_forms = '/' + parat_med_forms

    return paratatikos_basic_forms
