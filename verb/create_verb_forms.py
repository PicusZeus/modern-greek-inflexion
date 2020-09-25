
from .conjugations import recognize_passive_present_continuous_conjugation, recognize_active_non_past_conjugation, recognize_past_conjugation

from .create_verb_con import create_all_pers_forms, create_roots_from_past


def create_all_imperfect_non_passive_personal_forms(verb):
    """
    :param verb: it can be a single verb or active and passive forms divided by '/'. There can also be alternative forms
    for both voices separated by coma
    :return:
    """
    deponens = False
    verb = verb.split('/')
    if len(verb) > 1:
        act_verbs, pass_verbs = verb
    else:
        act_verbs = verb[0]
        pass_verbs = None
        # depoonens are dealt with later

    sec_pos = 'ind'
    forms = []
    if act_verbs:
        voice = 'active'
        sec_pos = 'ind'
        for v in act_verbs.split(','):
            v = v.strip()
            # to be safe, sometimes list, especially if created manually, can have some white spaces
            if v[-3:] == 'μαι' and v != 'είμαι':
                voice = 'passive'
                deponens = True
                con = recognize_passive_present_continuous_conjugation(v)
            else:
                con = recognize_active_non_past_conjugation(v, voice=voice)

            root = con['root']
            con_ind = con['conjugation_ind']
            if con_ind in ['con1_act_modal', 'modal']:
                sec_pos = 'modal'
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = {}
            else:
                forms_ind = create_all_pers_forms(con_ind, root)

                con_imp = con['conjugation_imp']
                forms_imp = create_all_pers_forms(con_imp, root)

            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind, 'forms_imp': forms_imp})

    if pass_verbs:
        voice = 'passive'
        for v in pass_verbs.split(','):
            con = recognize_passive_present_continuous_conjugation(v)
            root = con['root']
            con_ind = con['conjugation_ind']

            forms_ind_pass = create_all_pers_forms(con_ind, root)

            con_imp = con['conjugation_imp']
            forms_imps_pass = create_all_pers_forms(con_imp, root)

            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind_pass, 'forms_imp': forms_imps_pass})

    return forms, deponens


def create_all_perf_non_past_personal_forms(verb, deponens=False):
    """
    :param verb: verb in subjunctive mode, active and passive separated by '/', alternatives separated by ','
    :param deponens:
    :return:
    """
    verb = verb.split('/')

    if len(verb) > 1:
        act_verbs, pass_verbs = verb
    else:
        act_verbs = verb[0]
        pass_verbs = None
    sec_pos = 'ind'
    forms = []
    root = None
    if act_verbs:
        voice = 'active'
        for v in act_verbs.split(','):
            v = v.strip()
            if deponens:
                voice = 'passive'
                con = recognize_active_non_past_conjugation(v, aspect='perf', tense='fin', voice='passive')
            else:
                con = recognize_active_non_past_conjugation(v, aspect='perf', tense='fin', voice='active')
            root = con['root']
            con_ind = con['conjugation_ind']
            if con_ind in ['con1_act_modal', 'modal', 'con2_act_modal']:
                sec_pos = 'modal'
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = {}
            else:
                forms_ind = create_all_pers_forms(con_ind, root)

                con_imp = con['conjugation_imp']
                forms_imp = create_all_pers_forms(con_imp, root)

            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind, 'forms_imp': forms_imp})

    if pass_verbs:
        active_root = root
        voice = 'passive'
        for v in pass_verbs.split(','):
            v = v.strip()
            con = recognize_active_non_past_conjugation(v, aspect='perf', tense='fin', voice=voice)
            root = con['root']
            con_ind = con['conjugation_ind']
            if con_ind in ['con1_act_modal', 'modal']:
                sec_pos = 'modal'
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = {}
            else:
                forms_ind = create_all_pers_forms(con_ind, root)

                con_imp = con['conjugation_imp']
                forms_imp = create_all_pers_forms(con_imp, root, active_root=active_root)

            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind, 'forms_imp': forms_imp})

    return forms


def create_all_past_personal_forms(verb, lemma, aspect, deponens=False):
    """
    :param verb: aorist or paratatikos
    :param lemma: that is a present form, needed in order to correctly create augment
    :param aspect:
    :param deponens:
    :return:
    """
    verb = verb.split('/')
    if len(verb) > 1:
        act_verbs, pass_verbs = verb
    else:
        act_verbs = verb[0]
        pass_verbs = None

    sec_pos = 'ind'
    forms = []

    if act_verbs:
        simple_aor = True
        voice = 'active'

        for v in act_verbs.split(','):
            v = v.strip()
            if deponens and v not in ['έγινα', 'κάθισα', 'έκατσα', 'ήρθα', 'ήλθα']:
                voice = 'passive'

                simple_aor = aspect != 'imperf'
            data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)
            conjugation = data['conjugation_ind']
            if conjugation == 'parat2_act':
                simple_aor = False

            stem = data['root']
            deaugmented_stem = create_roots_from_past(v, lemma)

            forms_ind = create_all_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem, simple_aor=simple_aor)
            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind})

    if pass_verbs:

        voice = 'passive'
        diathesis = 'passive'
        for v in pass_verbs.split(','):
            v = v.strip()

            data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)
            conjugation = data['conjugation_ind']
            stem = data['root']

            not_paratatikos = aspect != 'imperf'

            forms_ind = create_all_pers_forms(conjugation, stem, simple_aor=not_paratatikos)
            forms.append({'voice': diathesis, 'sec_pos': sec_pos, 'forms_ind': forms_ind})

    return forms
