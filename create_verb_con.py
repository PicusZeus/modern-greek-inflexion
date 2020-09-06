import pickle
from modern_greek_stemmer.stemmer import recognize_active_non_past_conjugation, \
    recognize_passive_present_continuous_conjugation, create_imp_pass, recognize_past_conjugation
from modern_greek_stemmer.resources import conjugations

from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, \
    where_is_accent, count_syllables, remove_all_diacritics
from modern_greek_accentuation.augmentify import add_augment, deaugment_stem, deaugment_prefixed_stem
from modern_greek_stemmer.greek_tables import past_perfect_participles


try:
    file = open('modern_greek_stemmer/el_GR.pickle', 'br')
except FileNotFoundError:
    file = open('el_GR.pickle', 'br')
greek_corpus = pickle.load(file)




ex = {'': '', 'czas teraźniejszy': 'τσινάω', 'znaczenie': '', 'czas przyszły (θα), tryb zależny prosty (να)': 'τσινήσω', 'aoryst': 'τσίνησα/', 'paratatikos': 'τσινούσα/', 'act_pres_participle': 'τσινώντας'}
ex_2 = {'': '', 'czas teraźniejszy': 'γράφω/γράφομαι', 'znaczenie': '', 'czas przyszły (θα), tryb zależny prosty (να)': 'γράψω/γραφώ,γραφτώ', 'aoryst': 'έγραψα/γράφηκα,εγράφη,γράφτηκα,εγράφτη', 'paratatikos': 'έγραφα/γραφόμουν', 'act_pres_participle': 'γράφοντας', 'arch_act_pres_participle': 'γράφων,γράφουσα,γράφον', 'pass_pres_participle': 'γραφόμενος', 'active_aorist_participle': 'γράψας,γράψασα,γράψαν'}

#print([verbs[i] for i in range(333,355)])



forms_imp = {
    'sg': {
        'sec': [],
    },
    'pl': {
        'sec': [],
    }
}


def create_pers_forms(conjugation_name, root, active_root = None, deaugmented_root = None, simple_aor = False):
    forms_ind = {}

    if conjugation_name == 'modal':
        return None

    endings = conjugations[conjugation_name]

    for number in endings.keys():
        forms_ind[number] = {}
        for person in endings[number].keys():
            forms_ind[number][person] = []
            for ending in endings[number][person]:
                form = root + ending
                if count_syllables(ending) == 2 and ending == remove_all_diacritics(ending):
                    form = put_accent_on_the_antepenultimate(form)
                forms_ind[number][person].append(form)

    if simple_aor:
        for number in endings.keys():
            forms_ind[number] = {}
            for person in endings[number].keys():
                forms_ind[number][person] = []
                for ending in endings[number][person]:

                    if deaugmented_root and count_syllables(ending) > 1:
                        form = put_accent_on_the_antepenultimate(deaugmented_root + ending)
                        forms_ind[number][person].append(form)
                    else:
                        form = put_accent_on_the_antepenultimate(root + ending)

                        forms_ind[number][person].append(form)

                    if form != put_accent_on_the_antepenultimate(form, true_syllabification=False):
                        if deaugmented_root:
                            form = deaugmented_root + ending
                        forms_ind[number][person].append(put_accent_on_the_antepenultimate(form, true_syllabification=False))

    if conjugation_name in ['con1_pass']:
        forms_ind['pl']['pri'][0] = put_accent_on_the_antepenultimate(forms_ind['pl']['pri'][0])
        forms_ind['pl']['sec'][1] = put_accent_on_the_antepenultimate(forms_ind['pl']['sec'][1])

    elif conjugation_name in ['parat1_pass']:
        forms_ind['pl']['ter'][0] = put_accent_on_the_antepenultimate(forms_ind['pl']['ter'][0])

    elif conjugation_name in ['parat2d_pass', 'parat2b_logia', 'parat2b_pass']:
        # add augment to archaic forms
        forms_ind_with_augmented_forms = forms_ind.copy()
        for number in forms_ind.keys():
            for person in forms_ind[number]:
                for form in (forms_ind[number][person]):
                    augmented_forms = add_augment(form)
                    for augmented_form in augmented_forms:

                        if remove_all_diacritics(augmented_form) == augmented_form:
                            augmented_form = put_accent_on_the_antepenultimate(augmented_form)
                        if augmented_form in greek_corpus:

                            if augmented_form not in forms_ind[number][person]:
                                forms_ind_with_augmented_forms[number][person].append(augmented_form)

        forms_ind = forms_ind_with_augmented_forms

    elif conjugation_name in ['con2d_pass']:
        for number in forms_ind.keys():
            for person in forms_ind[number]:
                for index, form in enumerate(forms_ind[number][person]):
                    forms_ind[number][person][index] = put_accent_on_the_antepenultimate(form)

    elif conjugation_name in ['con2b_act', 'con2c_act', 'imper_act_aor_c']:
        for number in forms_ind.keys():
            for person in forms_ind[number]:
                for index, form in enumerate(forms_ind[number][person]):
                    if count_syllables(form) == 1:
                        forms_ind[number][person][index] = remove_all_diacritics(form)

    elif conjugation_name in ['imper_act_cont_1', 'imper_act_aor_a', 'imper_act_aor_b']:
        forms_ind['sg']['sec'][0] = put_accent_on_the_antepenultimate(forms_ind['sg']['sec'][0])

    elif conjugation_name in ['imper_pass_aor_a']:
        if active_root and active_root[-1] in ['σ', 'ψ', 'ξ']:
            forms_ind['sg']['sec'][0] = active_root + 'ου'
        else:
            forms_ind['sg']['sec'][0] = create_imp_pass(root)

    elif conjugation_name in ['imper_act_cont_2a']:
        forms_ind['sg']['sec'][0] = put_accent_on_the_penultimate(forms_ind['sg']['sec'][0])
        forms_ind['sg']['sec'][1] = put_accent_on_the_antepenultimate(forms_ind['sg']['sec'][1])
        if forms_ind['sg']['sec'][0] != put_accent_on_the_penultimate(forms_ind['sg']['sec'][0], true_syllabification=False):
            forms_ind['sg']['sec'].append(put_accent_on_the_penultimate(forms_ind['sg']['sec'][0], true_syllabification=False))
    elif conjugation_name in ['con2e_pass']:
        forms_ind['pl']['pri'][0] = put_accent_on_the_antepenultimate(forms_ind['pl']['pri'][0])
        forms_ind['pl']['pri'][1] = put_accent_on_the_antepenultimate(forms_ind['pl']['pri'][1])
        forms_ind['pl']['sec'][1] = put_accent_on_the_penultimate(forms_ind['pl']['sec'][1])
    elif conjugation_name == 'imper_act_cont_2c':
        if root == 'ακού':
            forms_ind['sg']['sec'] = ['άκου']
    elif conjugation_name in ['imper_act_aor_ca', 'imper_act_cont_2b']:
        forms_ind['sg']['sec'][0] = put_accent_on_the_penultimate(forms_ind['sg']['sec'][0])
    return forms_ind


def create_participle_forms(conjugation_name, root):
    endings = conjugations[conjugation_name]
    if 'nd' in endings.keys():
        form = root + endings['nd']['nd'][0]
        if where_is_accent(form) in ['incorrect_accent', None]:
            form = put_accent_on_the_antepenultimate(form)

    else:
        nom_sg = root + endings['sg']['nd'][0]
        nom_sg = put_accent_on_the_antepenultimate(nom_sg)
        root_part = nom_sg[:-2]
        fem_sg = root_part + 'η'
        neuter = root_part + 'ο'
        form = nom_sg + '/' + fem_sg + '/' + neuter

    return form


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
    elif deaugmented_stem_prefixed and put_accent_on_the_antepenultimate(deaugmented_stem_prefixed + 'αμε') in greek_corpus:
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
                simple_aor=False

            stem = data['root']
            deaugmented_stem = create_roots_from_past(v, lemma)


            forms_ind = create_pers_forms(conjugation, stem, deaugmented_root=deaugmented_stem, simple_aor=simple_aor)
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

            forms_ind = create_pers_forms(conjugation, stem, simple_aor=not_paratatikos)
            forms.append({'voice': diathesis, 'sec_pos': sec_pos, 'forms_ind': forms_ind})

    return forms


def create_perf_pass_part(lemma, v=None,  pass_form=None):

    if lemma in past_perfect_participles:
        ppp = past_perfect_participles[lemma]
        return ppp

    active_verb_root = None
    if v:
        active_verb_root = v[:-1]

    # if there I dont have this form in the list then try creating one
    if pass_form:
        pass_form_root = pass_form[:-3]
        if pass_form_root[-2:] == 'στ':
            ppp = pass_form_root[:-1] + 'μενος'
        elif pass_form_root[-3:] == 'εύτ':
            ppp = pass_form_root[:-2] + 'μενος'
        elif pass_form_root[-2:] == 'χτ':
            ppp = pass_form_root[:-3] + 'γμενος'
        elif pass_form_root[-1] == 'θ':
            ppp = pass_form_root[:-1] + 'μένος'
        else:
            print('ppp_error', pass_form)
            raise ValueError

    elif active_verb_root:
        #if there is no passive form, sometimes there is a ppp, probably most cases alrewdy in the list of irregular ppp, but still
        ppp = active_verb_root + 'μένος'
        ppp = put_accent_on_the_penultimate(ppp)
        if ppp in greek_corpus:
            return ppp
        else:
            print(ppp)
            return None

    else:
        print(v, pass_form, 'error')
        raise ValueError


def create_all_perf_forms(verb, deponens=False):
    # fut, conjunctive
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
                voice = 'deponens'

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
                forms_ind = create_pers_forms(con_ind, root)

                con_imp = con['conjugation_imp']
                forms_imp = create_pers_forms(con_imp, root)

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
                forms_ind = create_pers_forms(con_ind, root)

                con_imp = con['conjugation_imp']
                forms_imp = create_pers_forms(con_imp, root, active_root=active_root)
            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind, 'forms_imp': forms_imp})
    elif not act_verbs:
        print('No perfects')

    return forms


def create_all_present_ind_forms(verb):
    #verb can be one or with a passive version after /. there can be also some additional non standard forms, they are
    # added after a comma,
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

            if v[-3:] == 'μαι' and v != 'είμαι':
                voice = 'deponens'

                con = recognize_passive_present_continuous_conjugation(v)
            else:
                con = recognize_active_non_past_conjugation(v, voice=voice)

            root = con['root']
            con_ind = con['conjugation_ind']
            if con_ind in ['con1_act_modal', 'modal']:

                sec_pos = 'modal'
                forms_ind = {'sg': {'ter': [v]}}
                forms_imp = {}
                forms_part = {}
            else:
                forms_ind = create_pers_forms(con_ind, root)

                con_imp = con['conjugation_imp']
                forms_imp = create_pers_forms(con_imp, root)

                con_part = con['conjugation_part']

                forms_part = create_participle_forms(con_part, root)

            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind, 'forms_imp': forms_imp,
                          'forms_part': forms_part})

    if pass_verbs:
        voice = 'passive'
        for v in pass_verbs.split(','):
            con = recognize_passive_present_continuous_conjugation(v)
            root = con['root']
            con_ind = con['conjugation_ind']

            forms_ind_pass = create_pers_forms(con_ind, root)

            con_imp = con['conjugation_imp']
            forms_imps_pass = create_pers_forms(con_imp, root)

            con_part = con['conjugation_part']
            forms_part_pass = create_participle_forms(con_part, root)

            forms.append({'voice': voice, 'sec_pos': sec_pos, 'forms_ind': forms_ind_pass, 'forms_imp': forms_imps_pass,
                          'forms_part': forms_part_pass})

    return forms


if __name__ == '__main__':
    res = create_all_past_forms('σήκωσα/σηκώθηκα', 'σηκώνω', 'perf',deponens=False)
    #res = create_all_present_ind_forms('αγονίζομαι')
    print(res)