from modern_greek_inflexion.verb.create.forms.basic.create_basic_aorist_active import create_basic_aorist_active
from modern_greek_inflexion.verb.create.forms.basic.create_basic_aorist_passive import create_basic_aorist_passive


def create_basic_aorist_forms(pres_form: str,
                              act_root: str,
                              passive_root: str,
                              deponens: bool = False,
                              not_deponens: bool = True,
                              modal_act: bool = False,
                              modal_pass: bool = False) -> str:

    """
    This function creates basic aorist forms
    :param pres_form: 1st person sg present simple active or if deponens passive
    :param act_root: active perfect stem
    :param passive_root: passive perfect stem
    :param deponens: if deponens set to True
    :param not_deponens: if not deponens set to True
    :param modal_act: if modal active set to True
    :param modal_pass: if modal passive set to True
    :return: aorist_basic_forms, str "active_alt,active_alt/passive_alt,passive_alt"
    """

    aorist_basic_forms = ''

    if not_deponens or act_root:

        if passive_root:
            passive_aor_forms = create_basic_aorist_passive(pres_form, passive_root, modal_pass)
            passive_aor_forms = ','.join(passive_aor_forms)
        else:
            passive_aor_forms = ''

        if act_root:
            act_aor_forms = []
            for a_r in act_root.split(','):
                act_aor_forms.extend(create_basic_aorist_active(pres_form, a_r, modal_act))

            active_aor_forms = ','.join(set(act_aor_forms))
        else:
            active_aor_forms = ''

        aorist_basic_forms = '/'.join([active_aor_forms, passive_aor_forms])

    elif deponens:

        if passive_root:
            passive_aor_forms = create_basic_aorist_passive(pres_form, passive_root, modal_pass)

            passive_aor_forms = ','.join(passive_aor_forms)

            aorist_basic_forms = '/' + passive_aor_forms

    elif modal_act:

        if act_root:
            active_aor_forms = create_basic_aorist_active(pres_form, act_root, modal_act)
            active_aor_forms = ','.join(active_aor_forms)
        else:
            active_aor_forms = ''

        aorist_basic_forms = active_aor_forms + '/'

    elif modal_pass:

        if passive_root:
            active_aor_forms = create_basic_aorist_passive(pres_form, passive_root, modal_pass)
            active_aor_forms = ','.join(active_aor_forms)
        else:
            active_aor_forms = ''

        aorist_basic_forms = '/' + active_aor_forms

    return aorist_basic_forms
