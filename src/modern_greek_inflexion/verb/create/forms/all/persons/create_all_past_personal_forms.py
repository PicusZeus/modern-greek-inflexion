from __future__ import annotations

from modern_greek_inflexion.resources.typing import presentConjugationType, voiceType, aspectType, personal_forms_type
from modern_greek_inflexion.verb.helpers import compound_alternative_forms
from modern_greek_inflexion.verb.create.forms.all.persons.create_all_pers_forms import create_all_pers_forms
from modern_greek_inflexion.verb.create.roots.create_roots_from_past import create_stem_from_augmented_past
from modern_greek_inflexion.verb.recognize import recognize_past_conjugation
from modern_greek_inflexion.resources.variables import PASSIVE, SG, TER, EIMAI_PARATATIKOS, IND, \
    MODAL, PARAT2_ACT, ROOT, IMPERF, CONJUGATION_IND, ULTIMATE
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate
from modern_greek_inflexion.resources import greek_corpus
from modern_greek_accentuation.syllabify import modern_greek_syllabify


def create_all_past_personal_forms(past_basic_form: set[str],
                                   pres_form: str,
                                   aspect: aspectType,
                                   voice: voiceType,
                                   pres_con: presentConjugationType = None) -> dict:
    """
    This function creates all personal forms for past tenses
    :param past_basic_form: a set with one or more basic past forms (that is 1st person sg, or 3rd person if modal)
    :param pres_form: 1st person sg present simple form
    :param aspect: PERF or IMPERF
    :param voice: PASSIVE or ACTIVE
    :param pres_con: present conjugation type
    :return: A dictionary with potentially two keys, under the first one indicative or conjuctive forms,
    under the second imperative forms, if applicable.
    """

    sec_pos = IND
    forms = {}

    simple_aor = True

    for v in past_basic_form:

        v = v.strip()

        data = recognize_past_conjugation(v, pres_form, aspect=aspect, voice=voice, pres_con=pres_con)

        conjugation = data[CONJUGATION_IND]
        if conjugation in [PARAT2_ACT, EIMAI_PARATATIKOS] \
                or (voice == PASSIVE and aspect == IMPERF) \
                or where_is_accent(data[ROOT]) == ULTIMATE:
            simple_aor = False
        stem = data[ROOT]
        deaugmented_stem = create_stem_from_augmented_past(v, pres_form)

        if deaugmented_stem:
            # sometimes augment stays if it wasn't accented
            deaugmented_syllabified = modern_greek_syllabify(deaugmented_stem)
            if len(deaugmented_syllabified) > 1 and deaugmented_syllabified[-2] == modern_greek_syllabify(stem)[-2]:
                deaugmented_stem = None

        if deaugmented_stem:
            if put_accent_on_the_penultimate(deaugmented_stem + 'ω') not in greek_corpus and v[-2:] != 'γα':
                deaugmented_stem = None

        forms_ind = create_all_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem, simple_aor=simple_aor)

        if forms_ind == MODAL:
            forms_ind = {SG: {TER: [v]}}
        forms = compound_alternative_forms(forms, sec_pos, forms_ind, None)

    return forms
