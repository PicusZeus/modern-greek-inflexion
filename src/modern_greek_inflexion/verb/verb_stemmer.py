from modern_greek_accentuation.syllabify import modern_greek_syllabify, count_syllables
from modern_greek_accentuation.accentuation import is_accented, put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, put_accent_on_the_ultimate, remove_all_diacritics, where_is_accent
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.resources import vowels

from .conjugations import recognize_passive_present_continuous_conjugation, recognize_active_non_past_conjugation, create_regular_perf_root

from ..resources import greek_corpus, irregular_passive_perfect_participles, irregular_active_aorists,\
    irregular_passive_aorists, deponens_with_active_perf_forms


def create_basic_present_forms(base_form, deponens=False, not_deponens=True, intransitive_active=False, modal_act=False, modal_med=False):

    if deponens:
        passive_conjugation = recognize_passive_present_continuous_conjugation(base_form)

        pres_dep_forms = [base_form]
        pres_conjugation = passive_conjugation['conjugation_ind']
        root = passive_conjugation['root']
        pres_dep_form_alt = None
        pres_dep_form_alt_alt = None
        if pres_conjugation == 'con2a_pass':
            pres_dep_form_alt = root + 'ούμαι'
            pres_dep_form_alt_alt = root + 'ώμαι'
        elif pres_conjugation == 'con2b_pass':
            pres_dep_form_alt = root + 'ιέμαι'
        elif pres_conjugation == 'con2ab_pass':
            pres_dep_form_alt = root + 'ούμαι'
            pres_dep_form_alt_alt = root + 'ιέμαι'

        if pres_dep_form_alt and (pres_dep_form_alt in greek_corpus):
            pres_dep_forms.append(pres_dep_form_alt)

        if pres_dep_form_alt_alt and (pres_dep_form_alt_alt in greek_corpus):
            pres_dep_forms.append(pres_dep_form_alt_alt)

        present_basic_forms = ','.join(pres_dep_forms)

    elif not_deponens:

        passive_conjugation = recognize_active_non_past_conjugation(base_form)

        pres_conjugation = passive_conjugation['conjugation_ind']
        root = passive_conjugation['root']

        pres_pass_forms = []
        pres_pass_form = None
        pres_pass_form_alt_1 = None
        pres_pass_form_alt_2 = None
        # check conjugation

        if pres_conjugation == 'con2a_act':

            pres_pass_form = root + 'ιέμαι'
            pres_pass_form_alt_1 = root + 'ούμαι'
            pres_pass_form_alt_2 = root + 'ώμαι'

        elif pres_conjugation == 'con2b_act':
            pres_pass_form = root + 'ούμαι'
            pres_pass_form_alt_1 = root + 'ιέμαι'
            pres_pass_form_alt_2 = root + 'ώμαι'

        elif pres_conjugation == 'con2d_act':
            pres_pass_form = root + 'ούμαι'

        elif pres_conjugation == 'con2c_act':
            pres_pass_form = root + 'γομαι'

        elif pres_conjugation == 'con1_act':
            pres_pass_form = root + 'ομαι'

        if pres_pass_form and (pres_pass_form in greek_corpus or root[-3:] == 'ποι'):
            pres_pass_forms.append(pres_pass_form)
        if pres_pass_form_alt_1 and (pres_pass_form_alt_1 in greek_corpus):
            pres_pass_forms.append(pres_pass_form_alt_1)
        if pres_pass_form_alt_2 and (pres_pass_form_alt_2 in greek_corpus):
            pres_pass_forms.append(pres_pass_form_alt_2)

        pres_pass_forms = ','.join(pres_pass_forms)

        if pres_pass_forms:
            present_basic_forms = base_form + '/' + pres_pass_forms
        else:
            present_basic_forms = base_form
            intransitive_active = True

    elif modal_act:
        passive_conjugation = recognize_active_non_past_conjugation(base_form)
        pres_conjugation = passive_conjugation['conjugation_ind']
        root = passive_conjugation['root']
        present_basic_forms = base_form

    elif modal_med:
        passive_conjugation = recognize_passive_present_continuous_conjugation(base_form)
        pres_conjugation = passive_conjugation['conjugation_ind']
        root = passive_conjugation['root']
        # modals and others
        present_basic_forms = base_form

    else:
        return False
    return present_basic_forms, pres_conjugation, root, intransitive_active


def create_basic_conjunctive_forms(pres_form, pres_conjugation, root, deponens=False, not_deponens=True, intransitive_active=False, modal_act=False, modal_med=False):
    act_root, passive_root = None, None
    active_perf_form = passive_perf_form = ''

    conjunctive_basic_forms = None
    perf_root = None
    if not_deponens:

        act_root = create_regular_perf_root(pres_form)

        if not intransitive_active:
            passive_root = create_regular_perf_root(pres_form, voice="passive")
        if act_root:

            if ',' in act_root:
                act_perf_forms = []
                for stem in act_root.split(','):
                    active_perf_form = stem + 'ω'
                    syllables = modern_greek_syllabify(active_perf_form)

                    if len(syllables) > 1 and not is_accented(syllables[-2]):
                        active_perf_form = stem + 'ώ'
                    act_perf_forms.append(active_perf_form)
                active_perf_form = ','.join(act_perf_forms)

            else:
                active_perf_form = act_root + 'ω'
                syllables = modern_greek_syllabify(active_perf_form)
                if len(syllables) > 1 and not is_accented(syllables[-2]):
                    active_perf_form = act_root + 'ώ'

                # check for exv
                if pres_form[-3:] == 'έχω' and act_root + 'ει' not in greek_corpus:
                    active_perf_form = pres_form

        if not intransitive_active:

            if passive_root:

                if ',' in passive_root:
                    passive_perf_forms = []
                    for stem in passive_root.split(','):
                        passive_perf_form = stem + 'ώ'
                        passive_perf_forms.append(passive_perf_form)
                    passive_perf_form = ','.join(passive_perf_forms)
                else:
                    passive_perf_form = passive_root + 'ώ'

        conjunctive_basic_forms = active_perf_form + '/' + passive_perf_form

    elif deponens:
        passive_root = create_regular_perf_root(pres_form, voice="passive")

        if passive_root:
            if ',' in passive_root:

                passive_perf_forms = []
                for stem in passive_root.split(','):
                    passive_perf_form = stem + 'ώ'

                    if is_accented(stem):
                        passive_perf_form = stem + 'ω'

                    passive_perf_forms.append(passive_perf_form)

                passive_perf_form = ','.join(passive_perf_forms)
            else:
                passive_perf_form = passive_root + 'ώ'
                # check accent
                if is_accented(passive_root):
                    passive_perf_form = passive_root + 'ω'

            conjunctive_basic_forms = '/' + passive_perf_form
            if pres_form[-7:] in deponens_with_active_perf_forms:
                act_root = passive_root
                passive_root = None
                conjunctive_basic_forms = passive_perf_form + '/'

    elif modal_act:
        if pres_conjugation == 'con1_act_modal':
            act_root = create_regular_perf_root(root + 'ω')
        elif pres_conjugation == 'con2_act_modal':
            act_root = create_regular_perf_root(root + 'ώ')

        if act_root:
            active_perf_form = act_root + 'ει'

            syllables = modern_greek_syllabify(active_perf_form)

            if len(syllables) > 1 and not is_accented(syllables[-2]):
                active_perf_form = act_root + 'εί'

        conjunctive_basic_forms = active_perf_form + '/'

    elif modal_med:
        perf_root = None
        if pres_form[-4:] == 'εται':
            perf_root = create_regular_perf_root(root + 'ομαι', 'passive')
            if perf_root and perf_root + 'εί' not in greek_corpus:
                perf_root = create_regular_perf_root(root + 'μαι', 'passive')
        elif pres_form[-5:] == 'είται':
            perf_root = create_regular_perf_root(root + 'ούμαι', 'passive')
        elif pres_form[-4:] == 'άται':
            perf_root = create_regular_perf_root(root + 'άμαι', 'passive')
            if perf_root and perf_root + 'εί' not in greek_corpus:
                perf_root = create_regular_perf_root(root + 'ώμαι', 'passive')
        elif pres_form[-4:] == 'αται':
            perf_root = create_regular_perf_root(root + 'αμαι', 'passive')
        elif pres_form[-3:] == 'ται':
            perf_root = create_regular_perf_root(root + 'μαι', 'passive')
        passive_root = perf_root

        if perf_root:
            conjunctive_basic_forms = '/' + passive_root + 'εί'

    return conjunctive_basic_forms, perf_root, act_root, passive_root


def create_basic_aorist_forms(pres_form, act_root, passive_root, deponens=False, not_deponens=True, intransitive_active=False, modal_act=False, modal_med=False):
    aorist_basic_forms = None
    active_aor_forms, passive_aor_forms = [], []

    if not_deponens:

        for ir_verb in irregular_active_aorists:
            length_ir_verb = len(ir_verb)
            if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                active_aor_forms.extend(add_augment(pres_form[:-length_ir_verb] + irregular_active_aorists[ir_verb]))
                if irregular_active_aorists[ir_verb][-4:] == 'βηκα':
                    # add archaic athematic aorist for compounds with bainw
                    active_aor_forms.extend(add_augment(pres_form[:-length_ir_verb] + irregular_active_aorists[ir_verb][:-2]))
        for ir_verb in irregular_passive_aorists:
            length_ir_verb = len(ir_verb)
            if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                passive_aor_forms.extend(add_augment(pres_form[:-length_ir_verb] + irregular_passive_aorists[ir_verb]))

        if act_root:

            if ',' in act_root:
                for stem in act_root.split(','):
                    active_aor_forms.extend(add_augment(stem + 'α'))
            else:
                active_aor_forms.extend(add_augment(act_root + 'α'))

            if pres_form[-3:] == 'έχω':
                active_aor_forms.extend([pres_form[:-3] + 'είχα'])
                archaic_aor_form = add_augment(pres_form[:-3] + 'σχον')
                active_aor_forms.extend(archaic_aor_form)

            # filter_out
            active_aor_forms = [f for f in active_aor_forms if f in greek_corpus]

            # there are at least two instances where this algorithm can be confused by irregular imperative forms
            irregular_imperative_similar_to_aorist = ('ανέβα', 'κατέβα', 'τρέχα', 'φεύγα')

            active_aor_forms = list(set(active_aor_forms).difference(irregular_imperative_similar_to_aorist))

            # special case for poiw
            if 'ποιήσ' in act_root:
                active_aor_forms.append(put_accent_on_the_antepenultimate(act_root + 'α', true_syllabification=False))

        if passive_root or passive_aor_forms:
            if passive_root and ',' in passive_root:

                for stem in passive_root.split(','):
                    pass_aor_form = stem + 'ηκα'

                    passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form))
                    # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in corpus
                    archaic_passive_aor = stem + 'η'
                    archaic_passive_aor = add_augment(archaic_passive_aor)
                    passive_aor_forms.extend(archaic_passive_aor)

            elif passive_root:
                pass_aor_form = passive_root + 'ηκα'
                pass_aor_form = put_accent_on_the_antepenultimate(pass_aor_form)
                passive_aor_forms.append(pass_aor_form)
                # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in corpus
                archaic_passive_aor = passive_root + 'η'
                archaic_passive_aor = add_augment(archaic_passive_aor)
                passive_aor_forms.extend(archaic_passive_aor)

                if 'ποιηθ' in passive_root:
                    passive_aor_forms.append(
                        put_accent_on_the_antepenultimate(passive_root + 'ηκα', true_syllabification=False))
            # filter out

            passive_aor_forms = [f for f in passive_aor_forms if f in greek_corpus]

        # if active_aor_forms:
        active_aor_forms = list(set(active_aor_forms))
        active_aor_forms = ','.join(active_aor_forms)
        # if passive_aor_form:
        passive_aor_forms = list(set(passive_aor_forms))
        passive_aor_forms = ','.join(passive_aor_forms)

        aorist_basic_forms = '/'.join([active_aor_forms, passive_aor_forms])

    elif deponens:
        if pres_form[-7:] in deponens_with_active_perf_forms:
            passive_root = act_root
        if passive_root:

            if ',' in passive_root:
                passive_aor_forms = []
                for stem in passive_root.split(','):
                    pass_aor_form = stem + 'ηκα'
                    passive_aor_forms.extend(put_accent_on_the_antepenultimate(pass_aor_form))

                    # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in
                    # corpus
                    archaic_passive_aor = stem + 'η'
                    archaic_passive_aor = add_augment(archaic_passive_aor)
                    passive_aor_forms.extend(archaic_passive_aor)

            else:
                passive_aor_forms = passive_root + 'ηκα'

                passive_aor_forms = [put_accent_on_the_antepenultimate(passive_aor_forms)]
                # archaic passive
                archaic_passive_aor = passive_root + 'ην'
                archaic_passive_aor = add_augment(archaic_passive_aor)
                passive_aor_forms.extend(archaic_passive_aor)
            # filter out

            passive_aor_forms = [f for f in passive_aor_forms if f in greek_corpus]
            passive_aor_forms = ','.join(passive_aor_forms)

            # ginomai, erxomai, kathomai

            if pres_form[-7:] in deponens_with_active_perf_forms:
                if ',' in passive_root:
                    passive_aor_forms = []
                    for stem in passive_root.split(','):
                        pass_aor_form = stem + 'α'
                        passive_aor_forms.extend(add_augment(pass_aor_form))
                else:
                    passive_aor_forms = passive_root + 'α'
                    passive_aor_forms = add_augment(passive_aor_forms)
                passive_aor_forms = [form for form in passive_aor_forms if form in greek_corpus]
                passive_aor_forms = ','.join(passive_aor_forms)
            if 'ποιηθ' in passive_root:
                passive_aor_forms = (passive_root + 'ηκα')
            aorist_basic_forms = '/' + passive_aor_forms
            if pres_form[-7:] in deponens_with_active_perf_forms:
                aorist_basic_forms = passive_aor_forms + '/'
    elif modal_act or modal_med:
        mod_root = None
        if act_root:
            mod_root = act_root
        elif passive_root:
            mod_root = passive_root
        if mod_root:
            aor_forms = add_augment(mod_root + 'ε')
            if passive_root:
                aor_forms.extend(add_augment(mod_root + 'ηκε'))
            # mainly for symbainei
            anc_forms = add_augment(mod_root + 'η')
            anc_forms = [a for a in anc_forms if where_is_accent(a) == 'penultimate']
            aor_forms.extend(anc_forms)

            aor_forms = [f for f in aor_forms if f in greek_corpus]

            aorist_basic_forms = ','.join(aor_forms)
            if modal_act:
                aorist_basic_forms = aorist_basic_forms + '/'
            elif modal_med:
                aorist_basic_forms = '/' + aorist_basic_forms

    return aorist_basic_forms


def create_basic_paratatikos_forms(pres_form, root, pres_conjugation, deponens=False, not_deponens=True, modal_act=False, modal_med=False):
    paratatikos_basic_forms = None
    if not_deponens:
        act_par, pass_par = [], []
        if pres_conjugation == 'con1_act':
            not_augmented_par = root + 'α'
            act_par = add_augment(not_augmented_par)

            act_par = [f for f in act_par if not (count_syllables(
                f) == 2 and f[0] not in vowels)]
            pass_par = [put_accent_on_the_penultimate(root + 'όμουν')]

        elif pres_conjugation == 'con2a_act':
            act_par = [root + 'ούσα', put_accent_on_the_antepenultimate(root + 'αγα')]
            pass_par = [root + 'ιόμουν', root + 'άμην']

        elif pres_conjugation in ['con2b_act', 'con2d_act']:
            act_par = [root + 'ούσα']
            pass_par = [root + 'ούμουν']
            if pres_conjugation == 'con2b_act' and root[-1] == 'ι':
                pass_par.append(root + 'όμουν')

        elif pres_conjugation == 'con2c_act':
            not_augmented_par = root + 'γα'
            act_par = add_augment(not_augmented_par)
            pass_par = [put_accent_on_the_penultimate(root + 'γόμουν')]

        elif pres_conjugation == 'eimai':
            act_par = ['ήμουν']

        act_par_all = [f for f in act_par if f in greek_corpus]
        if not act_par_all:

            act_par_all_3rd = [f for f in act_par if f[:-1] + 'ε' in greek_corpus]
            if act_par_all_3rd:
                act_par_all = [f[:-1] + 'α' for f in act_par_all_3rd]

        pass_par = [f for f in pass_par if f in greek_corpus]
        act_par = ','.join(act_par_all)
        pass_par = ','.join(pass_par)

        paratatikos = '/'.join([act_par, pass_par])
        if root[-3:] == 'ποι':
            paratatikos = root + 'ούσα/' + root + 'ούμουν' + ',' + root + 'όμουν'

        paratatikos_basic_forms = paratatikos

    elif deponens:
        pass_par = []
        root = remove_all_diacritics(root)
        if pres_conjugation == 'con1_pass':
            pass_par = [root + 'όμουν']
        elif pres_conjugation == 'con2a_pass':
            pass_par = [root + 'ιόμουν', root + 'ούμουν', root + 'όμουν']
        elif pres_conjugation == 'con2b_pass':
            pass_par = [root + 'ούμουν', root + 'ιόμουν']
        elif pres_conjugation in ['con2c_pass', 'con2ab_pass']:
            pass_par = [root + 'όμουν']
        elif pres_conjugation == 'con2d_pass':
            pass_par = [put_accent_on_the_penultimate(root + 'μην'), root[:-1] + 'όμουν', root + 'όμουν']
            pass_par.extend(add_augment(pass_par[0]))
        elif pres_conjugation == 'con2e_pass':
            pass_par = [root + 'άμην', root + 'όμουν']
        pass_par = [f for f in pass_par if f in greek_corpus]
        pass_par = list(set(pass_par))
        pass_par = ','.join(pass_par)
        if root[-3:] == 'ποι':
            pass_par = root + 'ούμουν,' + root + 'όμουν'
        paratatikos_basic_forms = '/' + pass_par

    elif modal_act:
        parat_act_forms = []
        if pres_form[-3:] == 'άει':
            parat_act_forms = add_augment(pres_form[:-3] + 'ούσε')
            parat_act_forms.extend(add_augment(pres_form[:-3] + 'αγε'))
        elif pres_form[-3:] == 'ά':
            parat_act_forms = add_augment(pres_form[:-1] + 'ούσε')
            parat_act_forms.extend(add_augment(pres_form[:-1] + 'γε'))
        elif pres_form[-2:] == 'ει':
            parat_act_forms = add_augment(pres_form[:-2] + 'ε')
        elif pres_form[-2:] == 'εί':
            parat_act_forms = add_augment(pres_form[:-2] + 'ούσε')

        parat_act_forms = [f for f in parat_act_forms if f in greek_corpus]
        parat_act_forms = ','.join(parat_act_forms)

        paratatikos_basic_forms = parat_act_forms + '/'

    elif modal_med:
        parat_med_forms = ''
        if pres_form[-5:] == 'ιέται':
            parat_med_forms = [root + 'ιόταν']

        elif pres_form[-5:] == 'είται':
            parat_med_forms = add_augment(root + 'είτο')
            parat_med_forms.extend([root + 'ούνταν'])

        elif pres_form[-4:] == 'άται':
            parat_med_forms = [root + 'άτο', root + 'όταν', root + 'ιόταν']

        elif pres_form[-4:] == 'εται':
            parat_med_forms = [put_accent_on_the_penultimate(root + 'όταν'), root + 'ετο']
        elif pres_form[-5:] == 'ειται':
            parat_med_forms = [root + 'ειτο']
            parat_med_forms.extend(add_augment(parat_med_forms[0]))
            parat_med_forms = [put_accent_on_the_antepenultimate(v) for v in parat_med_forms]

        parat_med_forms = [f for f in parat_med_forms if f in greek_corpus]
        parat_med_forms = ','.join(parat_med_forms)
        paratatikos_basic_forms = '/' + parat_med_forms

    return paratatikos_basic_forms

def create_present_active_participle(_, root, pres_conjugation):

    pres_part_act = ''
    if pres_conjugation == 'con1_act':
        pres_part_act = root + 'οντας'

    elif pres_conjugation in ['con2a_act', 'con2b_act', 'con2ab_act']:
        pres_part_act = root + 'ώντας'

    elif pres_conjugation == 'con2c_act':
        pres_part_act = root + 'γοντας'

    elif pres_conjugation == 'eimai':
        pres_part_act = 'όντας'

    if pres_part_act and pres_part_act in greek_corpus or root[-3:] == 'ποι':
        return pres_part_act
    else:
        return None


def create_present_active_participle_arch(_, root, pres_conjugation):

    arch_pres_part_act = ''
    if pres_conjugation == 'con1_act':
        if root + 'ων' in greek_corpus and root + 'ουσα' in greek_corpus:
            arch_pres_part_act = root + 'ων/' + root + 'ουσα/' + root + 'ον'

    elif pres_conjugation in ['con2a_act', 'con2ab_act']:
        if root + 'ών' in greek_corpus and root + 'ώσα' in greek_corpus:
            arch_pres_part_act = root + 'ών/' + root + 'ώσα/' + root + 'ών'

    elif pres_conjugation in ['con2b_act', 'con2d_act']:
        if root + 'ών' in greek_corpus and root + 'ούντα' in greek_corpus:
            arch_pres_part_act = root + 'ών/' + root + 'ούσα/' + root + 'ούν'

    elif pres_conjugation == 'con2c_act':
        if root + 'γων' in greek_corpus and root + 'γοντα' in greek_corpus:
            arch_pres_part_act = root + 'γων/' + root + 'γουσα/' + root + 'γον'

    elif pres_conjugation == 'eimai':

        if root + 'ων' in greek_corpus and \
                root + 'όντα' in greek_corpus:
            masc = put_accent_on_the_ultimate(root + 'ων', accent_one_syllable=False)
            fem = put_accent_on_the_penultimate(root + 'ούσα')
            neut = put_accent_on_the_ultimate(root + 'ον', accent_one_syllable=False)

            arch_pres_part_act = masc + '/' + fem + '/' + neut

    return arch_pres_part_act


def create_present_passive_participle(_, root, pres_conjugation):
    pres_part_pass = []
    present_passive_participle = ''
    part_root = remove_all_diacritics(root)

    if pres_conjugation in ['con1_act', 'con1_pass']:
        pres_part_pass = [part_root + 'όμενος']

    elif pres_conjugation in ['con2a_act', 'con2ab_pass', 'con2a_pass']:
        pres_part_pass = [part_root + 'ώμενος', part_root + 'ούμενος']

    elif pres_conjugation == 'con2c_act':
        pres_part_pass = [part_root + 'γόμενος']

    elif pres_conjugation in ['con2b_act', 'con2b_pass', 'con2c_pass', 'con2d_act']:

        pres_part_pass = [part_root + 'ούμενος']
    elif pres_conjugation == 'con2e_pass':
        pres_part_pass = [part_root + 'άμενος']
    elif pres_conjugation == 'con2d_pass':
        pres_part_pass = [put_accent_on_the_antepenultimate(root + 'μενος')]

    # special case for xairomai
    if part_root == 'χαιρ':
        pres_part_pass = ['χαρούμενος']

    present_passive_participle = [part for part in pres_part_pass if part in greek_corpus]

    return ','.join(present_passive_participle)


def create_passive_perfect_participle(pres_form, root, act_root, passive_root):

    all_passive_perfect_participles = ''
    passive_perfect_participles = []

    # check for irregularities
    for pr_f in irregular_passive_perfect_participles.keys():

        if pr_f == pres_form[-(len(pr_f)):] and irregular_passive_perfect_participles[pr_f]:

            part = pres_form[:-len(pr_f)] + irregular_passive_perfect_participles[pr_f]
            part_aug = add_augment(part)
            if part in greek_corpus:
                passive_perfect_participles = [part]
            for p in part_aug:
                if p in greek_corpus:
                    passive_perfect_participles.append(p)

    if passive_root and not passive_perfect_participles:

        if passive_root[-2:] == 'νθ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'σμενος')
        elif passive_root[-2:] == 'στ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
        elif passive_root[-1] == 'θ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
        elif passive_root[-2:] == 'φτ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'μμενος')
        elif passive_root[-1] == 'φ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μμενος')

        elif passive_root[-3:] == 'ευτ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'μενος')
            if act_root and act_root[-1] == 'σ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
            if passive_perfect_participle not in greek_corpus:
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
        elif passive_root[-2:] == 'χτ':
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'γμενος')
        else:
            passive_perfect_participle = put_accent_on_the_penultimate(passive_root + 'μένος')

        passive_perfect_participles = add_augment(passive_perfect_participle)

        passive_perfect_participles = [f for f in passive_perfect_participles if f in greek_corpus]
        if root[-3:] == 'ποι':
            passive_perfect_participles = [root + 'ημένος']

    elif not passive_root and act_root and not passive_perfect_participles:

        if act_root[-2:] in ['ύσ', 'άσ', 'ίσ']:
            passive_perfect_participle = put_accent_on_the_penultimate(act_root + 'μενος')
        elif act_root[-1] in ['σ', 'ν']:
            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'μενος')
            if passive_perfect_participle not in greek_corpus:
                passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'σμενος')
        elif act_root[-1] == 'ξ':
            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'γμενος')
        elif pres_form[-3:] == 'αίν':
            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-3] + 'ημενος')
            if passive_perfect_participle not in greek_corpus:
                passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-3] + 'αμενος')
        else:
            passive_perfect_participle = put_accent_on_the_penultimate(act_root + 'μενος')
        if passive_perfect_participle:
            passive_perfect_participles = add_augment(passive_perfect_participle)

            passive_perfect_participles = [f for f in passive_perfect_participles if f in greek_corpus]

    if passive_perfect_participles:
        # these are all possible participles in masc sg!!!
        passive_perfect_participles = list(set(passive_perfect_participles))
        all_passive_perfect_participles = ','.join(passive_perfect_participles)

    return all_passive_perfect_participles


def create_active_aorist_participle(root, act_roots):
    """
    :param root:
    :param act_roots: can be multiple alternative forms separated by ','
    :return:
    """
    result = []
    for act_root in act_roots.split(','):
        active_aorist_participles = None
        masc = act_root + 'ας'
        fem = act_root + 'ασα'
        neut = act_root + 'αν'

        masc_wn = put_accent_on_the_ultimate(act_root + 'ων')
        fem_ousa = put_accent_on_the_penultimate(act_root + 'ουσα')
        neut_on = put_accent_on_the_ultimate(act_root + 'ον')
        if masc in greek_corpus and fem in greek_corpus:
            active_aorist_participles = masc + '/' + fem + '/' + neut
            # on as
        elif masc_wn in greek_corpus and fem_ousa in greek_corpus:
            active_aorist_participles = masc_wn + '/' + fem_ousa + '/' + neut_on

        if active_aorist_participles:
            result.append(active_aorist_participles)

    return ','.join(result)


def create_passive_aorist_participle(passive_root):
    if passive_root + 'είσα' in greek_corpus:
        return passive_root + 'είς/' + passive_root + 'είσα/' + passive_root + 'έν'
    else:
        return None


