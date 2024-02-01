from __future__ import annotations

from typing import Any

from modern_greek_inflexion.exceptions import NotLegalVerbException

from modern_greek_inflexion.resources.variables import *


def recognize_passive_past_continuous_conjugation(lemma: str, verb: str, pres_con: str) -> tuple[str, Any]:
    verb = verb.strip()
    root = None

    if pres_con == CON2F_PASS:
        conjugation_ind = PARAT2F_PASS
        root = verb[:-6]


    elif pres_con == CON2C_PASS:
        root = verb[:-5]
        conjugation_ind = PARAT2C_PASS

    elif len(verb) >= 7 and 'ιόμουν' in verb[-7:]:
        if verb[-1] == 'ν':
            root = verb[:-6]
        else:
            # if iomouna
            root = verb[:-7]
        conjugation_ind = PARAT2A_PASS

    elif verb.endswith('όμουν') and pres_con == CON2AK_PASS:
        root = verb[:-5]
        conjugation_ind = PARAT2AK_PASS

    elif len(verb) >= 6 and 'όμουν' in verb[-6:]:
        if verb[-5:] == 'όμουν':
            root = verb[:-5]
        else:
            # if omouna
            root = verb[:-6]
        conjugation_ind = PARAT1_PASS
        # if koimamai
        if lemma[-4:] == 'άμαι':
            conjugation_ind = PARAT2C_PASS
            root = verb[:-5]
        elif lemma[-4:] == 'έμαι':
            conjugation_ind = PARAT2D_PASS
            root = verb[:-5]
    elif len(verb) >= 7 and 'ούμουν' in verb[-7:]:
        if verb[-6:] == 'ούμουν':
            root = verb[:-6]
        else:
            # if ούmouna
            root = verb[:-7]
        conjugation_ind = PARAT2B_PASS

    # elif len(verb) >= 6 and 'ούμην' in verb[-5:]:
    #     if verb[-5:] == 'ούμην':
    #         root = verb[:-5]
    #
    #     conjugation_ind = PARAT2B_PASS_LOGIA

    elif len(verb) >= 5 and 'έμην' in verb[-4:]:

        if verb[-4:] == 'έμην':
            root = verb[:-4]

        conjugation_ind = PARAT2D_PASS
    elif len(verb) >= 5 and 'άμην' in verb[-4:]:

        if verb[-4:] == 'άμην':
            root = verb[:-4]

        conjugation_ind = PARAT2E_PASS

    elif 'ήμουν' in verb:
        root = ''
        conjugation_ind = EIMAI_PARATATIKOS

    else:
        return verb, MODAL

    if root:
        return root, conjugation_ind
    else:
        raise NotLegalVerbException
