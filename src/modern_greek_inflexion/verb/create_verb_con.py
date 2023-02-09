import sys

from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, \
    count_syllables, remove_all_diacritics
from modern_greek_accentuation.augmentify import add_augment, deaugment_stem, deaugment_prefixed_stem

from ..resources import greek_corpus, irregular_imperative_forms, conjugations
from .conjugations import create_imp_pass, recognize_past_conjugation
from ..resources import SG, SEC, PL, PRI, TER, CON2A_ACT, CON2B_ACT, CON2C_ACT, PARAT2_ACT, CON1_PASS, MODAL, ACTIVE, \
    IMPERF, PASSIVE, CON1_PASS_MODAL, IND, CON2D_PASS, CON2E_PASS, PARAT1_PASS, PARAT2B_PASS, PARAT2D_PASS, \
    ARCH_PASS_AOR, IMPER_ACT_CONT_2A, IMPER_PASS_AOR_A, IMPER_ACT_AOR_CA, IMPER_ACT_CONT_1, IMPER_ACT_CONT_2B, \
    IMPER_ACT_CONT_2C, IMPER_ACT_AOR_A, IMPER_ACT_AOR_B, IMPER_ACT_AOR_C, PARAT2B_LOGIA, ROOT, DEPONENS

forms_imp = {
    SG: {
        SEC: [],
    },
    PL: {
        SEC: [],
    }
}


def create_all_pers_forms(conjugation_name, root, active_root=None, deaugmented_root=None, simple_aor=False):
    """

    :param conjugation_name: conjugation name
    :param root: verb root
    :param active_root: if pass, for imp, should be given if it's a special case, should be an array
    :param deaugmented_root: root without augment
    :param simple_aor: sygmatic aorist
    :return:
    """
    forms = {}

    if not conjugation_name or conjugation_name in [MODAL, CON1_PASS_MODAL]:
        return MODAL
    endings = conjugations[conjugation_name]

    for number in endings.keys():
        forms[number] = {}
        for person in endings[number].keys():
            forms[number][person] = []
            for ending in endings[number][person]:
                form = root + ending
                if count_syllables(ending) == 2 and ending == remove_all_diacritics(ending):
                    form = put_accent_on_the_antepenultimate(form)
                if ending == 'ει' and person == SEC:
                    form = put_accent_on_the_penultimate(form, true_syllabification=False)
                forms[number][person].append(form)
    # check if a verb in 2nd conjugation active has alternative endings belonging to other type of the 2nd con

    if conjugation_name in [CON2A_ACT, IMPER_ACT_CONT_2A]:
        if root + 'είς' in greek_corpus and root + 'εί' in greek_corpus:
            endings = conjugations[CON2B_ACT]

            if conjugation_name == IMPER_ACT_CONT_2A:
                endings = conjugations[IMPER_ACT_CONT_2B]
            for number in endings:
                for person in endings[number]:
                    for alt_ending in endings[number][person]:
                        forms[number][person].append(root + alt_ending)

    if conjugation_name in [CON2B_ACT, IMPER_ACT_CONT_2B]:
        if root + 'άς' in greek_corpus and root + 'άει' in greek_corpus:
            endings = conjugations[CON2A_ACT]
            if conjugation_name == IMPER_ACT_CONT_2B:
                endings = conjugations[IMPER_ACT_CONT_2A]
            for number in endings:
                for person in endings[number]:
                    for alt_ending in endings[number][person]:
                        forms[number][person].append(root + alt_ending)

    if simple_aor:
        for number in endings.keys():
            forms[number] = {}
            for person in endings[number].keys():
                forms[number][person] = []
                for ending in endings[number][person]:

                    if deaugmented_root and count_syllables(ending) > 1:
                        form = put_accent_on_the_antepenultimate(deaugmented_root + ending)

                        forms[number][person].append(form)
                    else:
                        form = put_accent_on_the_antepenultimate(root + ending)

                        forms[number][person].append(form)

                    if conjugation_name == ARCH_PASS_AOR and number == SG:
                        forms[number][person][0] = put_accent_on_the_penultimate(forms[number][person][0])

                    if form != put_accent_on_the_antepenultimate(form, true_syllabification=False):
                        if deaugmented_root:
                            form = deaugmented_root + ending
                        forms[number][person].append(
                            put_accent_on_the_antepenultimate(form, true_syllabification=False))

    if conjugation_name in [CON1_PASS]:
        forms[PL][PRI][0] = put_accent_on_the_antepenultimate(forms[PL][PRI][0])
        forms[PL][SEC][1] = put_accent_on_the_antepenultimate(forms[PL][SEC][1])

    elif conjugation_name in [PARAT1_PASS]:
        forms[PL][TER][0] = put_accent_on_the_antepenultimate(forms[PL][TER][0])

    elif conjugation_name in [PARAT2D_PASS, PARAT2B_LOGIA, PARAT2B_PASS]:
        # add augment to archaic forms
        forms_ind_with_augmented_forms = forms.copy()
        for number in forms.keys():
            for person in forms[number]:
                for form in (forms[number][person]):
                    augmented_forms = add_augment(form)
                    for augmented_form in augmented_forms:

                        if remove_all_diacritics(augmented_form) == augmented_form:
                            augmented_form = put_accent_on_the_antepenultimate(augmented_form)
                        if augmented_form in greek_corpus:

                            if augmented_form not in forms[number][person]:
                                forms_ind_with_augmented_forms[number][person].append(augmented_form)

        forms = forms_ind_with_augmented_forms

    elif conjugation_name in [CON2D_PASS]:
        for number in forms.keys():
            for person in forms[number]:
                for index, form in enumerate(forms[number][person]):
                    forms[number][person][index] = put_accent_on_the_antepenultimate(form)

    elif conjugation_name in [CON2B_ACT, CON2C_ACT, IMPER_ACT_AOR_C]:
        for number in forms.keys():
            for person in forms[number]:
                for index, form in enumerate(forms[number][person]):
                    if count_syllables(form, true_syllabification=False) == 1:
                        forms[number][person][index] = remove_all_diacritics(form)

    elif conjugation_name in [IMPER_ACT_CONT_1, IMPER_ACT_CONT_2C, IMPER_ACT_AOR_A, IMPER_ACT_AOR_B]:
        forms[SG][SEC][0] = put_accent_on_the_antepenultimate(forms[SG][SEC][0], true_syllabification=False)

    elif conjugation_name in [IMPER_PASS_AOR_A]:
        if active_root and active_root[0][-1] in ['σ', 'ψ', 'ξ']:
            forms[SG][SEC] = [x + "ου" for x in active_root]
        else:
            passive_aorist_recreated = create_imp_pass(root)
            forms[SG][SEC][0] = passive_aorist_recreated

    elif conjugation_name in [IMPER_ACT_CONT_2A]:
        forms[SG][SEC][0] = put_accent_on_the_penultimate(forms[SG][SEC][0])
        forms[SG][SEC][1] = put_accent_on_the_antepenultimate(forms[SG][SEC][1])
        if len(forms[SG][SEC]) == 3:
            forms[SG][SEC][2] = put_accent_on_the_penultimate(forms[SG][SEC][2])
        # accent
        if forms[SG][SEC][0] != put_accent_on_the_penultimate(forms[SG][SEC][0], true_syllabification=False):
            forms[SG][SEC].append(put_accent_on_the_penultimate(forms[SG][SEC][0], true_syllabification=False))

    elif conjugation_name in [CON2E_PASS]:
        forms[PL][PRI][0] = put_accent_on_the_antepenultimate(forms[PL][PRI][0])
        forms[PL][PRI][1] = put_accent_on_the_antepenultimate(forms[PL][PRI][1])
        forms[PL][SEC][1] = put_accent_on_the_penultimate(forms[PL][SEC][1])
    elif conjugation_name in [IMPER_ACT_AOR_CA, IMPER_ACT_CONT_2B]:
        if root == 'ζ':
            forms[SG][TER] = ['ζήτω']
        forms[SG][SEC][0] = put_accent_on_the_penultimate(forms[SG][SEC][0], true_syllabification=False)
        if len(forms[SG][SEC]) == 3:
            forms[SG][SEC][1] = put_accent_on_the_penultimate(forms[SG][SEC][1])
            forms[SG][SEC][2] = put_accent_on_the_antepenultimate(forms[SG][SEC][2])

    #### irregular imperatives
    if conjugation_name[:5] == 'imper':

        if root in irregular_imperative_forms:
            for number in irregular_imperative_forms[root]:
                for person in irregular_imperative_forms[root][number]:
                    irregular_form = irregular_imperative_forms[root][number][person]
                    try:
                        forms[number][person].append(irregular_form)
                        if root == 'πά':
                            # a sketchy way to deal with pao, but no other way I see
                            forms[number][person] = [irregular_form]
                        # in this case check validity of all imperative forms
                        forms[number][person] = [form for form in forms[number][person] if form in greek_corpus]
                    except:
                        print(sys.exc_info()[0])

    return forms


def create_roots_from_past(verb, lemma):
    # argument only in 1st person

    res = None
    if verb[-1] in ['α']:
        stem = verb[:-1]
    else:
        return None
    deaugmented_stem = deaugment_stem(stem, lemma)
    deaugmented_stem_prefixed = deaugment_prefixed_stem(stem)
    if deaugmented_stem:
        res = deaugmented_stem
    elif deaugmented_stem_prefixed:
        res = deaugmented_stem_prefixed

    return res


def create_all_past_forms(verb, lemma, aspect, deponens=False):
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
