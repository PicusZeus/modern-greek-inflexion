from __future__ import annotations

from modern_greek_accentuation.accentuation import *

from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.typing import aspectType, voiceType, tenseType, recognized_conjugation_type
from modern_greek_inflexion.resources.variables import *


def recognize_active_non_past_conjugation(verb: str,
                                          aspect: aspectType = IMPERF,
                                          tense: tenseType = FIN,
                                          voice: voiceType = ACTIVE) -> recognized_conjugation_type:
    """
    can be used for aspects: 'continuous', 'simple', 'simple_passive'
    verb is expected to be in 1st person sg, else it's assumed it's modal verb
    :param verb:
    :param aspect:
    :param tense:
    :param voice:
    :return:
    """

    verb = verb.strip()
    root = ''
    conjugation_ind = ''
    conjugation_imp = ''
    conjugation_part = ''

    # recognize conjugation
    if (verb.endswith('έω') and (not verb.endswith('λέω') or verb.endswith('πλέω')) or
            verb.endswith('παλαίω') or verb.endswith('πταίω') or verb.endswith('παίω')):

        root = verb[:-1]
        conjugation_ind = CON1_ACT
        conjugation_imp = IMPER_ACT_CONT_1
        conjugation_part = PRESENT_ACTIVE_PART_1

    elif (verb.endswith('έω') or (
            verb.endswith('άω') and (count_syllables(verb, true_syllabification=False) == 2 or aspect == PERF))
          or verb.endswith('αίω') or verb.endswith('ακούω') or verb.endswith('ώω')):
        root = verb[:-1]
        conjugation_ind = CON2C_ACT
        conjugation_imp = IMPER_ACT_CONT_2C
        conjugation_part = PRESENT_ACTIVE_PART_2C

    elif verb[-2:] == 'άω':
        root = verb[:-2]
        conjugation_ind = CON2A_ACT
        conjugation_imp = IMPER_ACT_CONT_2A
        conjugation_part = PRESENT_ACTIVE_PART_2

    elif (verb[-1] == 'ώ') or (verb[-1:] == 'ω' and count_syllables(verb) == 1):
        root = verb[:-1]

        conjugation_ind = CON2B_ACT
        conjugation_imp = IMPER_ACT_CONT_2B
        conjugation_part = PRESENT_ACTIVE_PART_2

        if (put_accent_on_the_ultimate(verb[:-1] + 'είς', accent_one_syllable=False) not in greek_corpus
            and verb[:-1] + 'ά' in greek_corpus or (verb[:-1] + 'άς' in greek_corpus or
                                                    verb[:-1] + 'άτε' in greek_corpus)) and aspect != PERF:

            if verb[:-1] + 'άω' in greek_corpus or verb[:-1] + 'άει' in greek_corpus:
                conjugation_ind = CON2A_ACT
                conjugation_imp = IMPER_ACT_CONT_2A

            elif (verb[:-1] + 'εί' not in greek_corpus and
                  (verb[:-1] + 'άτε' in greek_corpus)):
                conjugation_ind = CON2AK_ACT
                conjugation_imp = IMPER_ACT_CONT_2A
            elif aspect != PERF and verb[-2] == 'ι' and verb[-3] not in vowels:
                conjugation_ind = CON2AK_ACT
                conjugation_imp = IMPER_ACT_CONT_2A
        elif aspect != PERF and verb[-2] == 'ι' and verb[-3] not in vowels:
            conjugation_ind = CON2AK_ACT
            conjugation_imp = IMPER_ACT_CONT_2A

        archaic_ow = ['πληρώ', 'κυρώ', 'αξιώ', 'βιώ', 'γομώ', 'ζηλώ']
        if aspect != PERF and True in [verb.endswith(v) for v in archaic_ow]:

            conjugation_ind = CON2D_ACT
            conjugation_imp = IMPER_ACT_CONT_2D
            conjugation_part = PRESENT_ACTIVE_PART_2

    elif verb.endswith('ω'):

        root = verb[:-1]
        conjugation_ind = CON1_ACT
        conjugation_imp = IMPER_ACT_CONT_1
        conjugation_part = PRESENT_ACTIVE_PART_1

    elif verb == 'είμαι':
        root = ''
        conjugation_ind = EIMAI
        conjugation_imp = IMPER_ACT_EIMAI
        conjugation_part = PRESENT_ACTIVE_PART_EIMAI

    elif len(verb) > 5 and verb[-5:] == 'είμαι':
        root = verb[:-5]
        conjugation_ind = EIMAI

        conjugation_part = PRESENT_ACTIVE_PART_EIMAI

    elif verb == '':
        # sometimes there is no simple future form
        pass

    elif verb[-2:] in ['ει', 'εί']:
        root = verb[:-2]
        conjugation_ind = CON1_ACT_MODAL
        if verb[-2:] == 'εί':
            conjugation_ind = CON2_ACT_MODAL

    else:
        # else it's assumed it's modal
        return {ASPECT: aspect, TENSE: tense, VOICE: voice, ROOT: verb,
                CONJUGATION_IND: MODAL, CONJUGATION_IMP: '', CONJUGATION_PART: ''}

    if aspect == PERF:
        # con_ind already recognized
        conjugation_part: ''

        conjugation_imp = IMPER_ACT_AOR_A

        if count_syllables(verb) == 1:
            conjugation_imp = IMPER_ACT_AOR_C
        elif conjugation_ind == CON2B_ACT or verb in ['κατέβω', 'ανέβω']:
            conjugation_imp = IMPER_ACT_AOR_D
        elif verb.endswith('βω'):
            # compounds with bainw has either
            conjugation_imp = IMPER_ACT_CONT_1B
        elif root == '':
            # sometimes there is no simple future form
            pass

        elif (root[-1] not in ['σ', 'ψ', 'ξ', 'ρ', 'λ'] or root in ['πέσ']) and verb != 'φάω':
            conjugation_imp = IMPER_ACT_AOR_B
            # anebainw
            if conjugation_ind == CON2B_ACT and put_accent_on_the_penultimate(root + 'α') in greek_corpus:
                conjugation_imp = IMPER_ACT_AOR_CA

    if aspect == 'perf' and voice == PASSIVE:
        # for future passive participle logic is implemented separately
        conjugation_part = ''

        conjugation_imp = IMPER_PASS_AOR_A
    return {ASPECT: aspect, VOICE: voice, TENSE: tense,
            ROOT: root,
            CONJUGATION_IND: conjugation_ind,
            CONJUGATION_IMP: conjugation_imp,
            CONJUGATION_PART: conjugation_part}
