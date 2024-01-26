from modern_greek_inflexion.resources import IND, ACTIVE, PASSIVE, DEPONENS, IMPERF, ROOT, PARAT2_ACT
from modern_greek_inflexion.verb.create.forms.all.persons.create_all_pers_forms import create_all_pers_forms
from modern_greek_inflexion.verb.create.roots.create_roots_from_past import create_roots_from_past
from modern_greek_inflexion.verb.recognize import recognize_past_conjugation


def create_all_past_forms(verb: str, lemma: str, aspect: str,
                          deponens: bool = False) -> list[dict]:
    verb = verb.split('/')
    if len(verb) > 1:
        act_verbs, pass_verbs = verb
    else:
        act_verbs = verb[0]
        pass_verbs = None

    sec_pos = IND
    forms = []

    if act_verbs:
        simple_aor = True
        voice = ACTIVE
        diathesis = ACTIVE
        for v in act_verbs.split(','):
            v = v.strip()
            if deponens and v not in ['έγινα', 'κάθισα', 'έκατσα', 'ήρθα', 'ήλθα']:
                voice = PASSIVE
                diathesis = DEPONENS
                simple_aor = aspect != IMPERF
            data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)
            conjugation = data['conjugation_ind']
            if conjugation == PARAT2_ACT:
                simple_aor = False

            stem = data[ROOT]
            deaugmented_stem = create_roots_from_past(v, lemma)

            forms_ind = create_all_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem,
                                              simple_aor=simple_aor)
            forms.append({'voice': diathesis, 'sec_pos': sec_pos, 'forms_ind': forms_ind})

    if pass_verbs:
        voice = PASSIVE
        diathesis = PASSIVE
        for v in pass_verbs.split(','):
            v = v.strip()

            data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)
            conjugation = data['conjugation_ind']
            stem = data[ROOT]

            not_paratatikos = aspect != IMPERF

            forms_ind = create_all_pers_forms(conjugation, stem, simple_aor=not_paratatikos)
            forms.append({'voice': diathesis, 'sec_pos': sec_pos, 'forms_ind': forms_ind})

    return forms
