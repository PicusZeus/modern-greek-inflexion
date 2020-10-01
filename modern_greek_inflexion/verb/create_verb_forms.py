
from .conjugations import recognize_passive_present_continuous_conjugation, recognize_active_non_past_conjugation, recognize_past_conjugation

from .create_verb_con import create_all_pers_forms, create_roots_from_past


def compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp):
    """
    compuond all alternative forms into a set
    :return:
    """
    if not forms:

        forms = {'sec_pos': sec_pos, 'forms_ind': forms_ind, 'forms_imp': forms_imp}
    else:
        # print(forms_ind, forms, 'TUTAJ' )
        # print(forms, forms_ind)
        # then add alternative forms
        for number in forms['forms_ind']:
            for person in forms['forms_ind'][number]:
                old = forms['forms_ind'][number][person]
                new = forms_ind[number][person]
                new.extend(old)
                forms['forms_ind'][number][person] = new
        if forms_imp:
            for number in forms['forms_imp']:
                for person in forms['forms_imp'][number]:
                    old = forms['forms_imp'][number][person]
                    new = forms_imp[number][person]
                    new.extend(old)
                    forms['forms_imp'][number][person] = new

    # change lists to sets
    for number in forms['forms_ind']:
        for person in forms['forms_ind'][number]:
            old = forms['forms_ind'][number][person]
            new = set(old)
            forms['forms_ind'][number][person] = new
    if forms_imp:
        for number in forms['forms_imp']:
            for person in forms['forms_imp'][number]:
                old = forms['forms_imp'][number][person]
                new = set(old)
                forms['forms_imp'][number][person] = new

    return forms

def create_all_imperfect_personal_forms(verb, voice):
    """
    :param verb: it needs to be an array or set of alternative forms, active or passive,
    :param voice: voice has to be active or passive.
    :return: a dictionary {'voice': voice, 'sec_pos': secondary POS (here ind for indicative), 'forms_ind': all forms in a dictionary, 'forms_imp': all imper forms in a dictionary}
    """

    act_verbs = pass_verbs = None

    if voice == 'active':
        act_verbs = verb
    elif voice == 'passive':
        pass_verbs = verb
    else:
        print('voice can be only passive or active')
        raise ValueError

    sec_pos = 'ind'
    forms = None

    for v in verb:

        if act_verbs:
            voice = 'active'
            sec_pos = 'ind'
            v = v.strip()
            # to be safe, sometimes list, especially if created manually, can have some white spaces
            con = recognize_active_non_past_conjugation(v, voice=voice)

            root = con['root']
            con_ind = con['conjugation_ind']

            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con['conjugation_imp']
            forms_imp = create_all_pers_forms(con_imp, root)

        elif pass_verbs:
            con = recognize_passive_present_continuous_conjugation(v)
            root = con['root']
            con_ind = con['conjugation_ind']

            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con['conjugation_imp']
            forms_imp = create_all_pers_forms(con_imp, root)
        else:
            raise ValueError
        # print(v, forms, forms_ind)

        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)

    return forms


def create_all_perf_non_past_personal_forms(verb, voice, active_root_for_imp=None, deponens=False):
    """
    :param verb: an array of forms
    :param deponens:
    :return:
    """
    input(voice)
    act_verb = pass_verb = None


    sec_pos = 'ind'
    forms = {}
    root = None


    for v in verb:
        v = v.strip()
        if voice == 'active' and v:
            act_verb = v
        elif voice == 'passive' and v:
            # print(v, 'PASS')
            pass_verb = v
        if act_verb:
            # if deponens:
            #     voice = 'passive'
            #     con = recognize_active_non_past_conjugation(v, aspect='perf', tense='fin', voice='passive')

            con = recognize_active_non_past_conjugation(act_verb, aspect='perf', tense='fin', voice='active')
            root = con['root']
            con_ind = con['conjugation_ind']
            if con_ind in ['con1_act_modal', 'modal', 'con2_act_modal']:
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = None
            else:
                forms_ind = create_all_pers_forms(con_ind, root)
                con_imp = con['conjugation_imp']
                forms_imp = create_all_pers_forms(con_imp, root)

        elif pass_verb:
            con = recognize_active_non_past_conjugation(pass_verb, aspect='perf', tense='fin', voice=voice)
            root = con['root']
            con_ind = con['conjugation_ind']
            if con_ind in ['con1_act_modal', 'modal']:
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = None
            else:
                forms_ind = create_all_pers_forms(con_ind, root)
                con_imp = con['conjugation_imp']
                forms_imp = create_all_pers_forms(con_imp, root, active_root=active_root_for_imp)

        else:
            # print(voice, v)
            raise ValueError

        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)
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
