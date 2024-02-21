from __future__ import annotations

from modern_greek_inflexion.resources.variables import *
from .recognize_passive_past_continuous_conjugation import recognize_passive_past_continuous_conjugation
from ...resources.typing import aspectType, voiceType, presentConjugationType, recognized_conjugation_type


def recognize_past_conjugation(verb: str,
                               lemma: str,
                               aspect: aspectType = IMPERF,
                               voice: voiceType = ACTIVE,
                               pres_con: presentConjugationType = None) -> recognized_conjugation_type:
    """
    This function tries to recognize a type of inflection for a verb in past continuous (paratatikos) tense
    :param verb: verb in 1st person sg passive in paratatikos
    :param lemma: 1st person sg in present tense
    :param aspect: should be 'imperf'
    :param voice: 'active' or 'passive'
    :param pres_con: Present conjugation type
    :return: a dictionary with the following structure {ASPECT: aspect, VOICE: voice, TENSE: PAST, ROOT: root,
            CONJUGATION_IND: conjugation_ind}
    """
    verb = verb.strip()
    root = verb[:-1]

    conjugation_ind = AOR_ACT

    if root[-3:] == 'ούσ':
        conjugation_ind = PARAT2_ACT

    elif verb in ['ήμουν', 'παραήμουν']:
        conjugation_ind = EIMAI_PARATATIKOS
        root = verb[:-5]

    elif verb[-1] in ['ν', 'η']:
        conjugation_ind = ARCH_PASS_AOR
        if lemma.endswith('ται'):
            conjugation_ind = MODAL
        if verb[-2:] == 'ον':
            conjugation_ind = ARCH_SEC_AOR
            root = verb[:-2]

    elif verb[-1] != 'α':
        conjugation_ind = MODAL
        root = verb
        if verb[-1] == 'ε':
            conjugation_ind = PARAT_ACT_MODAL
            root = verb[:-1]

    if voice == PASSIVE and aspect == IMPERF:
        root, conjugation_ind = recognize_passive_past_continuous_conjugation(lemma, verb, pres_con)

    return {ASPECT: aspect, VOICE: voice, TENSE: PAST, ROOT: root,
            CONJUGATION_IND: conjugation_ind}
