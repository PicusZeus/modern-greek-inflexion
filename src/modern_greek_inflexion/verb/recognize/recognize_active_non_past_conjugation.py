from modern_greek_accentuation.accentuation import *

from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.typing import aspectType, voiceType, tenseType, recognized_conjugation_type
from modern_greek_inflexion.resources.variables import *


def recognize_active_non_past_conjugation(not_past_form: str,
                                          aspect: aspectType = IMPERF,
                                          tense: tenseType = FIN,
                                          voice: voiceType = ACTIVE) -> recognized_conjugation_type:
    """
    This function recognizes non past conjugation.
    :param not_past_form: 1st person sg
    :param aspect: IMPERF of PERF
    :param tense: FIN or PAST
    :param voice: ACTIVE or PASSIVE
    :return: a dictionary with such a structure {ASPECT: aspect, VOICE: voice, TENSE: tense,
            ROOT: root,
            CONJUGATION_IND: conjugation_ind,
            CONJUGATION_IMP: conjugation_imp,
            CONJUGATION_PART: conjugation_part}
    """

    not_past_form = not_past_form.strip()
    root = ''
    conjugation_ind = ''
    conjugation_imp = ''
    conjugation_part = ''

    # recognize conjugation
    if (not_past_form.endswith('έω') and (not not_past_form.endswith('λέω') or not_past_form.endswith('πλέω')) or
            not_past_form.endswith('παλαίω') or not_past_form.endswith('πταίω') or not_past_form.endswith('παίω')):

        root = not_past_form[:-1]
        conjugation_ind = CON1_ACT
        conjugation_imp = IMPER_ACT_CONT_1
        conjugation_part = PRESENT_ACTIVE_PART_1

    elif (not_past_form.endswith('έω') or (
            not_past_form.endswith('άω') and (count_syllables(not_past_form, true_syllabification=False) == 2 or aspect == PERF))
          or not_past_form.endswith('αίω') or not_past_form.endswith('ακούω') or not_past_form.endswith('ώω')):
        root = not_past_form[:-1]
        conjugation_ind = CON2C_ACT
        conjugation_imp = IMPER_ACT_CONT_2C
        conjugation_part = PRESENT_ACTIVE_PART_2C

    elif not_past_form[-2:] == 'άω':
        root = not_past_form[:-2]
        conjugation_ind = CON2A_ACT
        conjugation_imp = IMPER_ACT_CONT_2A
        conjugation_part = PRESENT_ACTIVE_PART_2

    elif (not_past_form[-1] == 'ώ') or (not_past_form[-1:] == 'ω' and count_syllables(not_past_form) == 1):
        root = not_past_form[:-1]

        conjugation_ind = CON2B_ACT
        conjugation_imp = IMPER_ACT_CONT_2B
        conjugation_part = PRESENT_ACTIVE_PART_2

        if (put_accent_on_the_ultimate(not_past_form[:-1] + 'είς', accent_one_syllable=False) not in greek_corpus
            and not_past_form[:-1] + 'ά' in greek_corpus or (not_past_form[:-1] + 'άς' in greek_corpus or
                                                             not_past_form[:-1] + 'άτε' in greek_corpus)) and aspect != PERF:

            if not_past_form[:-1] + 'άω' in greek_corpus or not_past_form[:-1] + 'άει' in greek_corpus:
                conjugation_ind = CON2A_ACT
                conjugation_imp = IMPER_ACT_CONT_2A

            elif (not_past_form[:-1] + 'εί' not in greek_corpus and
                  (not_past_form[:-1] + 'άτε' in greek_corpus)):
                conjugation_ind = CON2AK_ACT
                conjugation_imp = IMPER_ACT_CONT_2A
            elif aspect != PERF and not_past_form[-2] == 'ι' and not_past_form[-3] not in vowels:
                conjugation_ind = CON2AK_ACT
                conjugation_imp = IMPER_ACT_CONT_2A
        elif aspect != PERF and not_past_form[-2] == 'ι' and not_past_form[-3] not in vowels:
            conjugation_ind = CON2AK_ACT
            conjugation_imp = IMPER_ACT_CONT_2A

        archaic_ow = ['πληρώ', 'κυρώ', 'αξιώ', 'βιώ', 'γομώ', 'ζηλώ']
        if aspect != PERF and True in [not_past_form.endswith(v) for v in archaic_ow]:

            conjugation_ind = CON2D_ACT
            conjugation_imp = IMPER_ACT_CONT_2D
            conjugation_part = PRESENT_ACTIVE_PART_2

    elif not_past_form.endswith('ω'):

        root = not_past_form[:-1]
        conjugation_ind = CON1_ACT
        conjugation_imp = IMPER_ACT_CONT_1
        conjugation_part = PRESENT_ACTIVE_PART_1

    elif not_past_form == 'είμαι':
        root = ''
        conjugation_ind = EIMAI
        conjugation_imp = IMPER_ACT_EIMAI
        conjugation_part = PRESENT_ACTIVE_PART_EIMAI

    elif len(not_past_form) > 5 and not_past_form[-5:] == 'είμαι':
        root = not_past_form[:-5]
        conjugation_ind = EIMAI

        conjugation_part = PRESENT_ACTIVE_PART_EIMAI

    elif not_past_form == '':
        # sometimes there is no simple future form
        pass

    elif not_past_form[-2:] in ['ει', 'εί']:
        root = not_past_form[:-2]
        conjugation_ind = CON1_ACT_MODAL
        if not_past_form[-2:] == 'εί':
            conjugation_ind = CON2_ACT_MODAL

    else:
        # else it's assumed it's modal
        return {ASPECT: aspect, TENSE: tense, VOICE: voice, ROOT: not_past_form,
                CONJUGATION_IND: MODAL, CONJUGATION_IMP: '', CONJUGATION_PART: ''}

    if aspect == PERF:
        # con_ind already recognized
        conjugation_part: ''

        conjugation_imp = IMPER_ACT_AOR_A

        if count_syllables(not_past_form) == 1:
            conjugation_imp = IMPER_ACT_AOR_C
        elif conjugation_ind == CON2B_ACT or not_past_form in ['κατέβω', 'ανέβω']:
            conjugation_imp = IMPER_ACT_AOR_D
        elif not_past_form.endswith('βω'):
            # compounds with bainw has either
            conjugation_imp = IMPER_ACT_CONT_1B
        elif root == '':
            # sometimes there is no simple future form
            pass

        elif (root[-1] not in ['σ', 'ψ', 'ξ', 'ρ', 'λ'] or root in ['πέσ']) and not_past_form != 'φάω':
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
