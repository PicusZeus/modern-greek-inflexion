import sys

from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, \
    count_syllables, remove_all_diacritics
from modern_greek_accentuation.augmentify import add_augment, deaugment_stem, deaugment_prefixed_stem

from ..resources import greek_corpus, irregular_imperative_forms, conjugations
from .conjugations import create_imp_pass, recognize_past_conjugation

forms_imp = {
    'sg': {
        'sec': [],
    },
    'pl': {
        'sec': [],
    }
}


def create_all_pers_forms(conjugation_name, root, active_root=None, deaugmented_root=None, simple_aor=False):
    """
    :param conjugation_name: conjugation name
    :param root: verb root
    :param active_root: if deponens, then should be given if it's a special case
    :param deaugmented_root: root without augment
    :param simple_aor: sygmatic aorist
    :return:
    """
    forms = {}

    if not conjugation_name or conjugation_name in ['modal', 'con1_pass_modal']:
        return 'modal'
    endings = conjugations[conjugation_name]

    for number in endings.keys():
        forms[number] = {}
        for person in endings[number].keys():
            forms[number][person] = []
            for ending in endings[number][person]:
                form = root + ending
                if count_syllables(ending) == 2 and ending == remove_all_diacritics(ending):
                    form = put_accent_on_the_antepenultimate(form)
                forms[number][person].append(form)

    # check if a verb in 2nd conjugation active has alternative endings belonging to other type of the 2nd con

    if conjugation_name in ['con2a_act', 'imper_act_cont_2a']:
        if root + 'είς' in greek_corpus and root + 'εί' in greek_corpus:
            endings = conjugations['con2b_act']
            if conjugation_name == 'imper_act_cont_2a':
                endings = conjugations['imper_act_cont_2b']
            for number in endings:
                for person in endings[number]:
                    for alt_ending in endings[number][person]:
                        forms[number][person].append(root + alt_ending)

    if conjugation_name in ['con2b_act', 'imper_act_cont_2b']:
        if root + 'άς' in greek_corpus and root + 'άει' in greek_corpus:
            endings = conjugations['con2a_act']
            if conjugation_name == 'imper_act_cont_2b':
                endings = conjugations['imper_act_cont_2a']
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

                    if conjugation_name == 'arch_pass_aor' and number == 'sg':
                        forms[number][person][0] = put_accent_on_the_penultimate(forms[number][person][0])

                    if form != put_accent_on_the_antepenultimate(form, true_syllabification=False):
                        if deaugmented_root:
                            form = deaugmented_root + ending
                        forms[number][person].append(
                            put_accent_on_the_antepenultimate(form, true_syllabification=False))

    if conjugation_name in ['con1_pass']:
        forms['pl']['pri'][0] = put_accent_on_the_antepenultimate(forms['pl']['pri'][0])
        forms['pl']['sec'][1] = put_accent_on_the_antepenultimate(forms['pl']['sec'][1])

    elif conjugation_name in ['parat1_pass']:
        forms['pl']['ter'][0] = put_accent_on_the_antepenultimate(forms['pl']['ter'][0])

    elif conjugation_name in ['parat2d_pass', 'parat2b_logia', 'parat2b_pass']:
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

    elif conjugation_name in ['con2d_pass']:
        for number in forms.keys():
            for person in forms[number]:
                for index, form in enumerate(forms[number][person]):
                    forms[number][person][index] = put_accent_on_the_antepenultimate(form)

    elif conjugation_name in ['con2b_act', 'con2c_act', 'imper_act_aor_c']:
        for number in forms.keys():
            for person in forms[number]:
                for index, form in enumerate(forms[number][person]):
                    if count_syllables(form) == 1:
                        forms[number][person][index] = remove_all_diacritics(form)

    elif conjugation_name in ['imper_act_cont_1', 'imper_act_cont_2c', 'imper_act_aor_a', 'imper_act_aor_b']:
        forms['sg']['sec'][0] = put_accent_on_the_antepenultimate(forms['sg']['sec'][0])

    elif conjugation_name in ['imper_pass_aor_a']:
        if active_root and active_root[-1] in ['σ', 'ψ', 'ξ']:
            forms['sg']['sec'][0] = active_root + 'ου'
        else:
            passive_aorist_recreated = create_imp_pass(root)
            forms['sg']['sec'][0] = passive_aorist_recreated

    elif conjugation_name in ['imper_act_cont_2a']:
        forms['sg']['sec'][0] = put_accent_on_the_penultimate(forms['sg']['sec'][0])
        forms['sg']['sec'][1] = put_accent_on_the_antepenultimate(forms['sg']['sec'][1])
        if len(forms['sg']['sec']) == 3:
            forms['sg']['sec'][2] = put_accent_on_the_penultimate(forms['sg']['sec'][2])
        # accent
        if forms['sg']['sec'][0] != put_accent_on_the_penultimate(forms['sg']['sec'][0], true_syllabification=False):
            forms['sg']['sec'].append(put_accent_on_the_penultimate(forms['sg']['sec'][0], true_syllabification=False))

    elif conjugation_name in ['con2e_pass']:
        forms['pl']['pri'][0] = put_accent_on_the_antepenultimate(forms['pl']['pri'][0])
        forms['pl']['pri'][1] = put_accent_on_the_antepenultimate(forms['pl']['pri'][1])
        forms['pl']['sec'][1] = put_accent_on_the_penultimate(forms['pl']['sec'][1])
    elif conjugation_name in ['imper_act_aor_ca', 'imper_act_cont_2b']:
        if root == 'ζ':
            forms['sg']['ter'] = ['ζήτω']
        forms['sg']['sec'][0] = put_accent_on_the_penultimate(forms['sg']['sec'][0])
        if len(forms['sg']['sec']) == 3:
            forms['sg']['sec'][1] = put_accent_on_the_penultimate(forms['sg']['sec'][1])
            forms['sg']['sec'][2] = put_accent_on_the_antepenultimate(forms['sg']['sec'][2])

    #### irregular imperatives
    if conjugation_name[:5] == 'imper':

        if root in irregular_imperative_forms:
            for number in irregular_imperative_forms[root]:
                for person in irregular_imperative_forms[root][number]:
                    irregular_form = irregular_imperative_forms[root][number][person]
                    try:
                        forms[number][person].append(irregular_form)
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

    if deaugmented_stem and put_accent_on_the_antepenultimate(deaugmented_stem + 'αμε') in greek_corpus:
        res = deaugmented_stem
    elif deaugmented_stem_prefixed and put_accent_on_the_antepenultimate(
            deaugmented_stem_prefixed + 'αμε') in greek_corpus:
        res = deaugmented_stem_prefixed

    return res


def create_all_past_forms(verb, lemma, aspect, deponens=False):
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
        diathesis = 'active'
        for v in act_verbs.split(','):
            v = v.strip()
            if deponens and v not in ['έγινα', 'κάθισα', 'έκατσα', 'ήρθα', 'ήλθα']:
                voice = 'passive'
                diathesis = 'deponens'
                simple_aor = aspect != 'imperf'
            data = recognize_past_conjugation(v, lemma, aspect=aspect, voice=voice)
            conjugation = data['conjugation_ind']
            if conjugation == 'parat2_act':
                simple_aor = False

            stem = data['root']
            deaugmented_stem = create_roots_from_past(v, lemma)

            forms_ind = create_all_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem,
                                              simple_aor=simple_aor)
            forms.append({'voice': diathesis, 'sec_pos': sec_pos, 'forms_ind': forms_ind})

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
