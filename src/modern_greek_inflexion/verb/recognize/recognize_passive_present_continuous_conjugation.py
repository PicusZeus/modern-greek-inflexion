from __future__ import annotations

from modern_greek_accentuation.resources import vowels

from modern_greek_inflexion.exceptions import NotLegalVerbException
from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.typing import recognized_conjugation_type
from modern_greek_inflexion.resources.variables import *
from modern_greek_inflexion.resources.verb import ancient_oomai


def recognize_passive_present_continuous_conjugation(verb: str) -> recognized_conjugation_type:
    """
    This function recognizes present conjugation type
    :param verb: 1st person sg present tense passive voice or, if modal, 3rd person sg.
    :return: A dictionary with the following structure: {ASPECT: IMPERF, VOICE: PASSIVE, TENSE: FIN, ROOT: root,
            CONJUGATION_IND: conjugation_ind, CONJUGATION_IMP: conjugation_imp, CONJUGATION_PART: conjugation_part}
    """
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

    elif verb[-5:] in ["ιέμαι", 'υέμαι']:
        root = verb[:-5]
        conjugation_ind = CON2A_PASS
        conjugation_imp = IMPER_PASS_CONT_2A
        conjugation_part = PRESENT_PASSIVE_PART_2A

    elif verb.endswith('ιούμαι') and verb[-7] not in vowels and verb.replace('ιούμαι', 'ιέμαι') in greek_corpus:
        root = verb[:-6]
        conjugation_ind = CON2A_PASS
        conjugation_imp = IMPER_PASS_CONT_2A
        conjugation_part = PRESENT_PASSIVE_PART_2A

    elif verb.endswith('ούμαι') and True in [verb.endswith(v) for v in ancient_oomai]:
        root = verb[:-5]
        conjugation_ind = CON2F_PASS
        conjugation_imp = IMPER_PASS_CONT_2SA
        conjugation_part = PRESENT_PASSIVE_PART_2B

    elif verb[-5:] == 'ούμαι':
        root = verb[:-5]
        conjugation_ind = CON2B_PASS
        conjugation_imp = IMPER_PASS_CONT_2B
        conjugation_part = PRESENT_PASSIVE_PART_2B
        if verb[:-5] + 'άμαι' in greek_corpus:
            conjugation_ind = CON2C_PASS
            conjugation_imp = IMPER_PASS_CONT_2C
            conjugation_part = PRESENT_PASSIVE_PART_2B

    elif verb[-4:] == 'άμαι':
        root = verb[:-4]
        conjugation_ind = CON2C_PASS
        conjugation_imp = IMPER_PASS_CONT_2C
        conjugation_part = PRESENT_PASSIVE_PART_2B

    elif verb.endswith('ώμαι'):
        root = verb[:-4]
        conjugation_ind = CON2AK_PASS
        conjugation_imp = IMPER_PASS_CONT_2AB
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

    elif verb[-4:] in ['εται']:
        root = verb[:-4]
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
        return {ASPECT: IMPERF, VOICE: PASSIVE, TENSE: FIN, ROOT: verb,
                CONJUGATION_IND: MODAL, CONJUGATION_IMP: '', CONJUGATION_PART: ''}

    return {ASPECT: IMPERF, VOICE: PASSIVE, TENSE: FIN, ROOT: root,
            CONJUGATION_IND: conjugation_ind, CONJUGATION_IMP: conjugation_imp,
            CONJUGATION_PART: conjugation_part}
