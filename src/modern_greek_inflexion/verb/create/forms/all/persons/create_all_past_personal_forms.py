from __future__ import annotations

from modern_greek_inflexion.verb.helpers import compound_alternative_forms
from modern_greek_inflexion.verb.create.forms.all.persons.create_all_pers_forms import create_all_pers_forms
from modern_greek_inflexion.verb.create.roots.create_roots_from_past import create_roots_from_past
from modern_greek_inflexion.verb.recognize import recognize_past_conjugation
from modern_greek_inflexion.resources.resources import PASSIVE, SG, TER, EIMAI_PARATATIKOS, IND, \
    MODAL, PARAT2_ACT, ROOT, IMPERF, CONJUGATION_IND, ULTIMATE
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate
from modern_greek_inflexion.resources.resources import greek_corpus
from modern_greek_accentuation.syllabify import modern_greek_syllabify


def create_all_past_personal_forms(verb: set, lemma: str, aspect: str, voice: str, pres_con: str = None) -> dict:
    """
    :param pres_con:
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

        data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice, pres_con=pres_con)

        conjugation = data[CONJUGATION_IND]
        if conjugation in [PARAT2_ACT, EIMAI_PARATATIKOS] \
                or (voice == PASSIVE and aspect == IMPERF) \
                or where_is_accent(data[ROOT]) == ULTIMATE:
            simple_aor = False
        stem = data[ROOT]
        deaugmented_stem = create_roots_from_past(v, lemma)

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
