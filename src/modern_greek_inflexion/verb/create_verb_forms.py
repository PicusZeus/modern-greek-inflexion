from .conjugations import recognize_passive_present_continuous_conjugation, recognize_active_non_past_conjugation, \
    recognize_past_conjugation

from .create_verb_con import create_all_pers_forms, create_roots_from_past


def compound_alternative_forms(forms, sec_pos, forms_ind_or_con, forms_imp):
    """
    compound all alternative forms into a set
    :return:
    """
    if not forms:
        if forms_imp:
            forms = {sec_pos: forms_ind_or_con, 'imp': forms_imp}
        else:
            forms = {sec_pos: forms_ind_or_con}
    else:
        for pos in forms:
            for number in forms[pos]:
                for person in forms[pos][number]:
                    old = forms[pos][number][person]
                    try:
                        new = forms_ind_or_con[number][person]
                    except KeyError:
                        new = []
                    new.extend(old)
                    forms[pos][number][person] = new

    if forms_ind_or_con == 'modal':
        return forms
    if forms_imp == 'modal':
        forms_imp = None

    for pos in forms:
        for number in forms[pos]:
            for person in forms[pos][number]:
                old = forms[pos][number][person]
                new = set(old)
                forms[pos][number][person] = new

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
            if con_ind == 'con1_act_modal':
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = None
            if forms_imp == 'modal':
                forms_imp = None

        elif pass_verbs:

            con = recognize_passive_present_continuous_conjugation(v)

            root = con['root']
            con_ind = con['conjugation_ind']
            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con['conjugation_imp']
            forms_imp = create_all_pers_forms(con_imp, root)
            if forms_ind == 'modal':
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = None
        else:
            raise ValueError

        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)
    return forms


def create_all_perf_non_past_personal_forms(verb, voice, active_root_for_imp=None):
    """
    :param voice:
    :param active_root_for_imp:
    :param verb: an array of forms
    :param deponens:
    :return:
    """

    act_verb = pass_verb = None

    sec_pos = 'ind'
    forms = {}

    for v in verb:
        v = v.strip()
        if voice == 'active' and v:
            act_verb = v
        elif voice == 'passive' and v:
            pass_verb = v
        if act_verb:
            con = recognize_active_non_past_conjugation(act_verb, aspect='perf', tense='fin', voice='active')
            root = con['root']
            con_ind = con['conjugation_ind']
            con_imp = con['conjugation_imp']
            if con_ind in ['con1_act_modal', 'modal', 'con2_act_modal']:

                forms_imp = None
            else:
                con_imp = con['conjugation_imp']
                forms_imp = create_all_pers_forms(con_imp, root)
            forms_ind = create_all_pers_forms(con_ind, root)

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
            raise ValueError
        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)
    return forms


def create_all_past_personal_forms(verb, lemma, aspect, voice):
    """
    :param voice:
    :param verb: aorist or paratatikos in a set (can be multiple alternative forms)
    :param lemma: that is a present form, needed in order to correctly create augment
    :param aspect:
    :param deponens:
    :return:
    """

    sec_pos = 'ind'
    forms = {}

    simple_aor = True

    for v in verb:
        v = v.strip()

        data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)

        conjugation = data['conjugation_ind']
        if conjugation == 'parat2_act' or (voice == 'passive' and aspect == 'imperf'):
            simple_aor = False
        stem = data['root']
        deaugmented_stem = create_roots_from_past(v, lemma)

        forms_ind = create_all_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem, simple_aor=simple_aor)
        if forms_ind == 'modal':
            forms_ind = {'sg': {'ter': [v]}}
        forms = compound_alternative_forms(forms, sec_pos, forms_ind, None)

    return forms
