from __future__ import annotations

from modern_greek_inflexion.verb.create.forms.basic.create_basic_aorist_active import create_basic_aorist_active
from modern_greek_inflexion.verb.create.forms.basic.create_basic_aorist_passive import create_basic_aorist_passive


def create_basic_aorist_forms(pres_form: str, act_root: str, passive_root: str, deponens: bool = False,
                              not_deponens: bool = True, modal_act: bool = False,
                              modal_med: bool = False, alternative: bool = False) -> str:

    """
    :param pres_form:
    :param act_root:
    :param passive_root:
    :param deponens:
    :param not_deponens:
    :param modal_act:
    :param modal_med:
    :param alternative:
    :return: aorist_basic_forms - active_alt,active_alt/passive_alt,passive_alt'
    """
    aorist_basic_forms = ''

    if not_deponens or act_root:

        if passive_root:
            passive_aor_forms = create_basic_aorist_passive(pres_form, passive_root, modal_med, alternative)
            passive_aor_forms = ','.join(passive_aor_forms)
        else:
            passive_aor_forms = ''

        if act_root:
            active_aor_forms = create_basic_aorist_active(pres_form, act_root, modal_act, alternative)
            active_aor_forms = ','.join(active_aor_forms)
        else:
            active_aor_forms = ''

        aorist_basic_forms = '/'.join([active_aor_forms, passive_aor_forms])

    elif deponens:

        if passive_root:
            passive_aor_forms = create_basic_aorist_passive(pres_form, passive_root, modal_med, alternative)

            passive_aor_forms = ','.join(passive_aor_forms)

            aorist_basic_forms = '/' + passive_aor_forms

    elif modal_act:

        if act_root:
            active_aor_forms = create_basic_aorist_active(pres_form, act_root, modal_act, alternative)
            active_aor_forms = ','.join(active_aor_forms)
        else:
            active_aor_forms = ''

        aorist_basic_forms = active_aor_forms + '/'

    elif modal_med:

        if passive_root:
            active_aor_forms = create_basic_aorist_passive(pres_form, passive_root, modal_med, alternative)
            active_aor_forms = ','.join(active_aor_forms)
        else:
            active_aor_forms = ''

        aorist_basic_forms = '/' + active_aor_forms

    return aorist_basic_forms
