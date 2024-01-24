from __future__ import annotations

from modern_greek_inflexion.helpers import compound_alternative_forms
from modern_greek_inflexion.verb.recognize import recognize_passive_present_continuous_conjugation, recognize_active_non_past_conjugation, \
    recognize_past_conjugation
from modern_greek_inflexion.resources.resources import ACTIVE, PASSIVE, SG, TER, EIMAI_PARATATIKOS, IND, IMP, \
    MODAL, CON1_ACT_MODAL, CON2_ACT_MODAL, PARAT2_ACT, ROOT, IMPERF, PERF, CONJUGATION_IND, \
    CONJUGATION_IMP, FIN
from modern_greek_accentuation.resources import ULTIMATE
from modern_greek_inflexion.verb.create_verb_con import create_all_pers_forms, create_roots_from_past
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate
from modern_greek_inflexion.resources.resources import greek_corpus




def create_all_past_personal_forms(verb: set, lemma: str, aspect: str, voice: str) -> dict:
    """
    :param voice:
    :param verb: aorist or paratatikos in a set (can be multiple alternative forms)
    :param lemma: that is a present form, needed in order to correctly create augment
    :param aspect:
    :param deponens:
    :return:
    """

    sec_pos = IND
    forms = {}

    simple_aor = True

    for v in verb:

        v = v.strip()

        data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)

        conjugation = data[CONJUGATION_IND]
        if conjugation in [PARAT2_ACT, EIMAI_PARATATIKOS] \
                or (voice == PASSIVE and aspect == IMPERF) \
                or where_is_accent(data[ROOT]) == ULTIMATE:
            simple_aor = False
        stem = data[ROOT]
        deaugmented_stem = create_roots_from_past(v, lemma)

        if deaugmented_stem:
            if put_accent_on_the_penultimate(deaugmented_stem + 'ω') not in greek_corpus and v[-2:] != 'γα':
                deaugmented_stem = None

        forms_ind = create_all_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem, simple_aor=simple_aor)

        if forms_ind == MODAL:
            forms_ind = {SG: {TER: [v]}}
        forms = compound_alternative_forms(forms, sec_pos, forms_ind, None)

    return forms