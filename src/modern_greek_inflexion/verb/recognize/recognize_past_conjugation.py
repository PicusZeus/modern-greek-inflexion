from __future__ import annotations

from modern_greek_inflexion.resources.variables import *
from .recognize_passive_past_continuous_conjugation import recognize_passive_past_continuous_conjugation


def recognize_past_conjugation(verb: str, lemma: str, aspect: str = IMPERF,
                               voice: str = ACTIVE, pres_con: str = None) -> dict:
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

    return {'aspect': aspect, 'voice': voice, 'tense': PAST, ROOT: root,
            'conjugation_ind': conjugation_ind}
