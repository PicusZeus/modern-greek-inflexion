from __future__ import annotations

from modern_greek_inflexion.exceptions import NotLegalVerbException
from modern_greek_inflexion.resources.typing import presentConjugationType

from modern_greek_inflexion.resources.variables import *


def recognize_passive_past_continuous_conjugation(pres_form: str,
                                                  pass_paratatikos_form: str,
                                                  pres_con: presentConjugationType) -> tuple[str, str]:
    """
    This function recognizes passive paratatikos conjugation type
    :param pres_form: 1st person sg present simple tense
    :param pass_paratatikos_form: 1st person sg of passive paratatikos
    :param pres_con: present tense conjugation type
    :return: two element tuple, the first element is a passive paratatikos stem and the second one is passive paratatikos conjugation type
    """
    pass_paratatikos_form = pass_paratatikos_form.strip()
    root = None

    if pres_con == CON2F_PASS:
        conjugation_ind = PARAT2F_PASS
        root = pass_paratatikos_form[:-6]

    elif pres_con == CON2C_PASS:
        root = pass_paratatikos_form[:-5]
        conjugation_ind = PARAT2C_PASS

    elif len(pass_paratatikos_form) >= 7 and 'ιόμουν' in pass_paratatikos_form[-7:]:
        if pass_paratatikos_form[-1] == 'ν':
            root = pass_paratatikos_form[:-6]
        else:
            # if iomouna
            root = pass_paratatikos_form[:-7]
        conjugation_ind = PARAT2A_PASS

    elif pass_paratatikos_form.endswith('όμουν') and pres_con == CON2AK_PASS:
        root = pass_paratatikos_form[:-5]
        conjugation_ind = PARAT2AK_PASS

    elif len(pass_paratatikos_form) >= 6 and 'όμουν' in pass_paratatikos_form[-6:]:
        if pass_paratatikos_form[-5:] == 'όμουν':
            root = pass_paratatikos_form[:-5]
        else:
            # if omouna
            root = pass_paratatikos_form[:-6]
        conjugation_ind = PARAT1_PASS
        # if koimamai
        if pres_form[-4:] == 'άμαι':
            conjugation_ind = PARAT2C_PASS
            root = pass_paratatikos_form[:-5]
        elif pres_form[-4:] == 'έμαι':
            conjugation_ind = PARAT2D_PASS
            root = pass_paratatikos_form[:-5]
    elif len(pass_paratatikos_form) >= 7 and 'ούμουν' in pass_paratatikos_form[-7:]:
        if pass_paratatikos_form[-6:] == 'ούμουν':
            root = pass_paratatikos_form[:-6]
        else:
            # if ούmouna
            root = pass_paratatikos_form[:-7]
        conjugation_ind = PARAT2B_PASS

    elif len(pass_paratatikos_form) >= 5 and 'έμην' in pass_paratatikos_form[-4:]:

        if pass_paratatikos_form[-4:] == 'έμην':
            root = pass_paratatikos_form[:-4]

        conjugation_ind = PARAT2D_PASS
    elif len(pass_paratatikos_form) >= 5 and 'άμην' in pass_paratatikos_form[-4:]:

        if pass_paratatikos_form[-4:] == 'άμην':
            root = pass_paratatikos_form[:-4]

        conjugation_ind = PARAT2E_PASS

    elif 'ήμουν' in pass_paratatikos_form:
        root = ''
        conjugation_ind = EIMAI_PARATATIKOS

    else:
        return pass_paratatikos_form, MODAL

    if root:
        return root, conjugation_ind
    else:
        raise NotLegalVerbException
