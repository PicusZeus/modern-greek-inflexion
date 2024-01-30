from __future__ import annotations

from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate

from modern_greek_inflexion.verb.helpers import check_personal_forms
from modern_greek_inflexion.resources import CONJUGATION_IND, ROOT, CON2A_PASS, CON2B_PASS, CON2AB_PASS, CON2A_ACT, \
    CON2A_ACT_LOGIA, CON2B_ACT, CON2D_ACT, CON2C_ACT, CON1_ACT
from modern_greek_inflexion.verb.recognize import recognize_passive_present_continuous_conjugation, \
    recognize_active_non_past_conjugation


def create_basic_present_forms(base_form: str, deponens: bool = False, not_deponens: bool = True,
                               intransitive_active: bool = False, modal_act: bool = False,
                               modal_med: bool = False) -> tuple[str, str, str, bool]:
    """
    :param base_form:
    :param deponens:
    :param not_deponens:
    :param intransitive_active:
    :param modal_act:
    :param modal_med:
    :return: present_basic_forms: str, pres_conjugation: str, root: str, intransitive_active: bool
    """

    present_basic_forms = ''
    pres_conjugation = ''
    root = ''

    if deponens:
        passive_conjugation = recognize_passive_present_continuous_conjugation(base_form)

        pres_dep_forms = [base_form]
        pres_conjugation = passive_conjugation[CONJUGATION_IND]
        root = passive_conjugation[ROOT]
        f_p = None
        f_p_alt = None
        th_p = None
        th_p_alt = None

        if pres_conjugation == CON2A_PASS:
            f_p = root + 'ιέμαι'
            th_p = root + 'ιέται'
            f_p_alt = root + 'ούμαι'
            th_p_alt = root + 'είται'

        elif pres_conjugation == CON2B_PASS:
            f_p = root + 'ούμαι'
            th_p = root + 'είται'
            f_p_alt = root + 'ιέμαι'
            th_p_alt = root + 'ιέται'

        elif pres_conjugation == CON2AB_PASS:
            f_p = root + 'ώμαι'
            th_p = root + 'άται'
            f_p_alt = root + 'ιέμαι'
            th_p_alt = root + 'ιέται'

        if check_personal_forms(f_p, th_p):
            pres_dep_forms.append(f_p)

        if check_personal_forms(f_p_alt, th_p_alt):
            pres_dep_forms.append(f_p_alt)

        present_basic_forms = ','.join(pres_dep_forms)

    elif not_deponens:

        passive_conjugation = recognize_active_non_past_conjugation(base_form)

        pres_conjugation = passive_conjugation[CONJUGATION_IND]
        root = passive_conjugation[ROOT]

        pres_pass_forms = []
        f_p_pass = None
        f_p_pass_alt_1 = None
        f_p_pass_alt_2 = None
        f_p_pass_alt_3 = None
        th_p_pass = None
        th_p_pass_alt_1 = None
        th_p_pass_alt_2 = None
        th_p_pass_alt_3 = None
        # check conjugation

        if pres_conjugation == CON2A_ACT:

            f_p_pass = root + 'ιέμαι'
            th_p_pass = root + 'ιέται'

            f_p_pass_alt_1 = root + 'ούμαι'
            th_p_pass_alt_1 = root + 'είται'
            f_p_pass_alt_2 = root + 'ώμαι'
            th_p_pass_alt_2 = root + 'άται'
            f_p_pass_alt_3 = put_accent_on_the_antepenultimate(root + 'αμαι')
            th_p_pass_alt_3 = put_accent_on_the_antepenultimate(root + 'αται')
        elif pres_conjugation == CON2A_ACT_LOGIA:
            f_p_pass_alt_3 = put_accent_on_the_antepenultimate(root + 'αμαι')
            th_p_pass_alt_3 = put_accent_on_the_antepenultimate(root + 'αται')
            f_p_pass_alt_1 = root + 'ιέμαι'
            th_p_pass_alt_1 = root + 'ιέται'
            f_p_pass_alt_2 = root + 'ώμαι'
            th_p_pass_alt_2 = root + 'άται'

        elif pres_conjugation == CON2B_ACT:
            f_p_pass = root + 'ούμαι'
            th_p_pass = root + 'είται'
            f_p_pass_alt_1 = root + 'ιέμαι'
            th_p_pass_alt_1 = root + 'ιέται'

            f_p_pass_alt_2 = root + 'ώμαι'
            th_p_pass_alt_2 = root + 'άται'

        elif pres_conjugation == CON2D_ACT:
            f_p_pass = root + 'ούμαι'
            th_p_pass = root + 'οίται'

        elif pres_conjugation == CON2C_ACT:
            f_p_pass = root + 'γομαι'
            th_p_pass = root + 'γεται'
        elif pres_conjugation == CON1_ACT:
            f_p_pass = root + 'ομαι'

            th_p_pass = root + 'εται'

        if f_p_pass and check_personal_forms(f_p_pass, th_p_pass):
            pres_pass_forms.append(f_p_pass)

        elif base_form in ['ρρέω', 'πηγνύω', 'ομνύω', 'βαίνω']:
            pres_pass_forms.append(f_p_pass)

        if f_p_pass_alt_1 and check_personal_forms(f_p_pass_alt_1, th_p_pass_alt_1):
            pres_pass_forms.append(f_p_pass_alt_1)
        if f_p_pass_alt_2 and check_personal_forms(f_p_pass_alt_2, th_p_pass_alt_2):
            pres_pass_forms.append(f_p_pass_alt_2)
        if f_p_pass_alt_3 and check_personal_forms(f_p_pass_alt_3, th_p_pass_alt_3):
            pres_pass_forms.append(f_p_pass_alt_3)

        pres_pass_forms = ','.join(pres_pass_forms)

        if pres_pass_forms:
            present_basic_forms = base_form + '/' + pres_pass_forms
        else:
            present_basic_forms = base_form
            intransitive_active = True

    elif modal_act:
        passive_conjugation = recognize_active_non_past_conjugation(base_form)
        pres_conjugation = passive_conjugation[CONJUGATION_IND]
        root = passive_conjugation[ROOT]
        present_basic_forms = base_form

    elif modal_med:
        passive_conjugation = recognize_passive_present_continuous_conjugation(base_form)
        pres_conjugation = passive_conjugation[CONJUGATION_IND]
        root = passive_conjugation[ROOT]
        # modals and others
        present_basic_forms = base_form

    return present_basic_forms, pres_conjugation, root, intransitive_active
