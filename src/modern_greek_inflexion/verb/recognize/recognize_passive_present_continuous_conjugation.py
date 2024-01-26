from __future__ import annotations

from typing import Any

from modern_greek_inflexion.exceptions import NotLegalVerbException
from modern_greek_inflexion.resources.resources import greek_corpus
from modern_greek_inflexion.resources.variables import *


def recognize_passive_present_continuous_conjugation(verb: str) -> dict[str | Any, str | Any]:
    verb = verb.strip()

    if verb != 'είμαι' and len(verb) < 6:
        # maybe unnecessary, but one more way to catch problematic input
        print(verb + ' doesnt seem to be a correct verb form')
        raise NotLegalVerbException

    elif verb[-4:] == 'ομαι':
        root = verb[:-4]
        conjugation_ind = CON1_PASS
        conjugation_imp = IMPER_PASS_CONT_1
        conjugation_part = PRESENT_PASSIVE_PART_1


    elif verb[-5:] == "ιέμαι":
        root = verb[:-5]
        conjugation_ind = CON2A_PASS
        conjugation_imp = IMPER_PASS_CONT_2A
        conjugation_part = PRESENT_PASSIVE_PART_2A

    elif verb[-5:] == 'ούμαι':
        root = verb[:-5]
        conjugation_ind = CON2B_PASS
        conjugation_imp = IMPER_PASS_CONT_2B
        conjugation_part = PRESENT_PASSIVE_PART_2B
        # con_act = recognize_active_non_past_conjugation(verb[:-5] + 'ώ')
        if root + 'οίς' in greek_corpus or root + 'ούται' in greek_corpus:
            conjugation_ind = CON2SA_PASS
            conjugation_imp = IMPER_PASS_CONT_2SA


    elif verb[-4:] == 'άμαι':
        root = verb[:-4]
        conjugation_ind = CON2C_PASS
        conjugation_imp = IMPER_PASS_CONT_2C
        conjugation_part = PRESENT_PASSIVE_PART_2B

    elif verb[-4:] == 'ώμαι':
        root = verb[:-4]
        conjugation_ind = CON2AB_PASS
        conjugation_imp = IMPER_PASS_CONT_2C
        conjugation_part = PRESENT_PASSIVE_PART_2AB

    elif verb[-4:] in ['εμαι', 'υμαι'] or verb[-5:] in ['είμαι', 'ειμαι']:
        root = verb[:-3]
        conjugation_ind = CON2D_PASS
        conjugation_imp = IMPER_PASS_CONT_2D
        conjugation_part = PRESENT_PASSIVE_PART_2D

    elif verb[-4:] == 'αμαι':
        root = verb[:-4]
        conjugation_ind = CON2E_PASS
        conjugation_imp = IMPER_PASS_CONT_2E
        conjugation_part = PRESENT_PASSIVE_PART_2E

    elif verb[-4:] in ['εται', 'άται', 'υται'] or verb[-5:] in ['είται', 'ειται', 'ιέται']:
        root = verb[:-4]
        if verb[-5:] in ['είται', 'ειται', 'ιέται']:
            root = verb[:-5]
        conjugation_ind = CON1_PASS_MODAL
        conjugation_imp = ''
        conjugation_part = ''

    elif verb[-5:] in ['είται', 'ειται', 'ιέται'] or verb[-4:] in ['άται', 'υται']:
        root = verb[:-5]
        if verb[-4:] in ['άται', 'εται']:
            root = verb[:-4]
        conjugation_ind = CON2_PASS_MODAL
        conjugation_imp = ''
        conjugation_part = ''

    else:
        return {'aspect': IMPERF, 'voice': PASSIVE, 'tense': FIN, ROOT: verb,
                'conjugation_ind': MODAL, 'conjugation_imp': '', 'conjugation_part': ''}

    return {'aspect': IMPERF, 'voice': PASSIVE, 'tense': FIN, ROOT: root,
            'conjugation_ind': conjugation_ind, 'conjugation_imp': conjugation_imp,
            'conjugation_part': conjugation_part}
