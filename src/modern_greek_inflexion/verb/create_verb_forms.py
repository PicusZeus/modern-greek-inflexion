from .conjugations import recognize_passive_present_continuous_conjugation, recognize_active_non_past_conjugation, \
    recognize_past_conjugation
from ..resources import ACTIVE, PASSIVE, PRI, SEC, PL, SG, TER, EIMAI, EIMAI_PARATATIKOS, IND, IMP, CON1_ACT, \
    CON2_ACT_MODAL, MODAL, CON1_ACT_MODAL, CON2_ACT_MODAL, PARAT2_ACT, ROOT, IMPERF, PERF, CONJUGATION_IND, \
    CONJUGATION_IMP, FIN
from .create_verb_con import create_all_pers_forms, create_roots_from_past
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate, \
    put_accent_on_the_antepenultimate
from ..resources import greek_corpus


def compound_alternative_forms(forms, sec_pos, forms_ind_or_con, forms_imp):
    """
    compound all alternative forms into a set
    :return:
    """

    if not forms:
        if forms_imp:
            forms = {sec_pos: forms_ind_or_con, IMP: forms_imp}
        else:
            forms = {sec_pos: forms_ind_or_con}
    else:
        if forms_imp:
            new_forms = {sec_pos: forms_ind_or_con, IMP: forms_imp}
        else:
            new_forms = {sec_pos: forms_ind_or_con}
        for pos in forms:
            for number in forms[pos]:
                for person in forms[pos][number]:
                    old = forms[pos][number][person]
                    try:
                        new = new_forms[pos][number][person]
                    except KeyError:
                        new = []

                    new.extend(old)
                    forms[pos][number][person] = new

    if forms_ind_or_con == MODAL:
        return forms

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

    if voice == ACTIVE:
        act_verbs = verb
    elif voice == PASSIVE:
        pass_verbs = verb
    else:
        print('voice can be only passive or active')
        raise ValueError

    sec_pos = IND
    forms = None

    for v in verb:

        if act_verbs:
            voice = ACTIVE
            sec_pos = IND
            v = v.strip()
            # to be safe, sometimes list, especially if created manually, can have some white spaces
            con = recognize_active_non_past_conjugation(v, voice=voice)

            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]
            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con[CONJUGATION_IMP]
            forms_imp = create_all_pers_forms(con_imp, root)

            if con_ind == CON1_ACT_MODAL:
                forms_ind = {SG: {TER: [v]}}
                forms_imp = None
            if forms_imp == MODAL:
                forms_imp = None

        elif pass_verbs:

            con = recognize_passive_present_continuous_conjugation(v)

            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]
            forms_ind = create_all_pers_forms(con_ind, root)

            con_imp = con[CONJUGATION_IMP]
            forms_imp = create_all_pers_forms(con_imp, root)
            if forms_ind == MODAL:
                forms_ind = {SG: {TER: [v]}}
                forms_imp = None
        else:
            raise ValueError

        forms = compound_alternative_forms(forms, sec_pos, forms_ind, forms_imp)
    return forms


def create_all_perf_non_past_personal_forms(verb, voice, active_root_for_imp=None):
    """
    :param voice:
    :param active_root_for_imp: an array of possible roots
    :param verb: an array of forms
    :param deponens:
    :return:
    """

    act_verb = pass_verb = None

    sec_pos = IND
    forms = {}

    for v in verb:
        v = v.strip()
        if voice == ACTIVE and v:
            act_verb = v
        elif voice == PASSIVE and v:
            pass_verb = v
        if act_verb:
            con = recognize_active_non_past_conjugation(act_verb, aspect=PERF, tense=FIN, voice=ACTIVE)
            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]

            if con_ind in [CON1_ACT_MODAL, MODAL, CON2_ACT_MODAL]:

                forms_imp = None
            else:
                con_imp = con[CONJUGATION_IMP]
                forms_imp = create_all_pers_forms(con_imp, root)
            forms_ind = create_all_pers_forms(con_ind, root)

        elif pass_verb:
            con = recognize_active_non_past_conjugation(pass_verb, aspect=PERF, tense=FIN, voice=voice)
            root = con[ROOT]
            con_ind = con[CONJUGATION_IND]
            if con_ind in [CON1_ACT_MODAL, MODAL]:
                forms_ind = {SG: {TER: [v]}}
                forms_imp = None
            else:
                forms_ind = create_all_pers_forms(con_ind, root)
                con_imp = con[CONJUGATION_IMP]
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

    sec_pos = IND
    forms = {}

    simple_aor = True

    for v in verb:

        v = v.strip()

        data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)

        conjugation = data[CONJUGATION_IND]
        if conjugation in [PARAT2_ACT, EIMAI_PARATATIKOS] \
                or (voice == PASSIVE and aspect == IMPERF) \
                or where_is_accent(data[ROOT]) == 'ultimate':
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
