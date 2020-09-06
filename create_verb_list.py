import pickle

from modern_greek_accentuation.resources import vowels

from .stemmer import create_regular_perf_root, recognize_active_non_past_conjugation, \
    recognize_passive_present_continuous_conjugation
from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, put_accent_on_the_antepenultimate,\
    count_syllables, remove_all_diacritics, is_accented, put_accent_on_the_ultimate
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.syllabify import modern_greek_syllabify
from modern_greek_stemmer.greek_tables import past_perfect_participles
"""
create lists of words that can be easily parsed by existing code.
Firstly, create list of verbs together with all the basic forms in the form:

[{'': '', 'czas teraźniejszy': 'αγαπάω / αγαπιέμαι', 'znaczenie': 'kocham', 'czas przyszły (θα), tryb zależny prosty
(να)': 'αγαπήσω / αγαπηθώ', 'aoryst': 'αγάπησα / αγαπήθηκα', 'paratatikos': 'αγαπούσα / αγαπιόμουν'},]

creating them automatically from the list 'lekseis_kata_pos.pickle', where you have probably all greek verbs.
Also to check if the created forms actually exist check them with this simple el_GR.dic.
"""
file=open('modern_greek_stemmer/el_GR.pickle', 'rb')
greek_corpus = pickle.load(file)

verb_temp = {'': '', 'czas teraźniejszy': '', 'znaczenie': '', 'czas przyszły (θα), tryb zależny prosty (να)': '', 'aoryst': '', 'paratatikos': ''}

def create_all_basic_forms(praes_form):

    if praes_form[-1] not in ['ω', 'ώ', 'ι', 'α']:
        return None

    # create dictionary with regular verb forms
    verb_temp = {'': '', 'czas teraźniejszy': '', 'znaczenie': '', 'czas przyszły (θα), tryb zależny prosty (να)': '',
      'aoryst': '', 'paratatikos': ''}
    not_deponens = True
    deponens = False
    intransitive_active = False
    past_part_pass = ''
    pres_conjugation = 'con1_act'

    if 'μαι' == praes_form[-3:] and not 'είμαι' == praes_form:
    # if this is not deponens
        deponens = True
        not_deponens = False
        pres_conjugation = 'con1_pass'

    modal_act = False
    modal_med = False
    if praes_form[-2:] in ['ει', 'εί']:
        modal_act = True
        not_deponens = False
    if praes_form[-3:] == 'ται':
        modal_med = True
        not_deponens = False

    root = ''
    praes_form_alt = None

    # prepositions that are sometimes added to a verb but do not have any impact on the way they are declined
    with_prothesis = False
    protheseis = ['ξανα', 'πρωτο', 'κακο', 'υπερ']
    # if they are at the beginning of the verb and such a verb exist
    for prothesis in protheseis:
        if praes_form[:len(prothesis)] == prothesis and praes_form[len(prothesis):] in greek_corpus:
            praes_form = praes_form[len(prothesis):]
            with_prothesis = prothesis

    # praesens

    if deponens:
        res = recognize_passive_present_continuous_conjugation(praes_form)

        praes_dep_forms = [praes_form]
        pres_conjugation = res['conjugation_ind']
        root = res['root']
        praes_dep_form_alt = None
        praes_dep_form_alt_alt = None
        if pres_conjugation == 'con2a_pass':
            praes_dep_form_alt = root + 'ούμαι'
            praes_dep_form_alt_alt = root + 'ώμαι'
        elif pres_conjugation == 'con2b_pass':
            praes_dep_form_alt = root + 'ιέμαι'

        elif pres_conjugation in ['con2e_pass', 'con2c_pass', 'con2d_pass']:
            print(pres_conjugation, root)
            pass

        elif pres_conjugation == 'con2ab_pass':
            praes_dep_form_alt = root + 'ούμαι'
            praes_dep_form_alt_alt = root + 'ιέμαι'

        if praes_dep_form_alt and (praes_dep_form_alt in greek_corpus):
            praes_dep_forms.append(praes_dep_form_alt)

        if praes_dep_form_alt_alt and (praes_dep_form_alt_alt in greek_corpus):
            praes_dep_forms.append(praes_dep_form_alt_alt)

        verb_temp['czas teraźniejszy'] = ','.join(praes_dep_forms)

    elif not_deponens:

        res = recognize_active_non_past_conjugation(praes_form)

        pres_conjugation = res['conjugation_ind']
        root = res['root']

        praes_pass_forms = []
        praes_pass_form = None
        praes_pass_form_alt_1 = None
        praes_pass_form_alt_2 = None
        # check conjugation

        if pres_conjugation == 'con2a_act':

            praes_pass_form = root + 'ιέμαι'
            praes_pass_form_alt_1 = root + 'ούμαι'
            praes_pass_form_alt_2 = root + 'ώμαι'

        elif pres_conjugation == 'con2b_act':
            praes_pass_form = root + 'ούμαι'
            praes_pass_form_alt_1 = root + 'ιέμαι'
            praes_pass_form_alt_2 = root + 'ώμαι'

        elif pres_conjugation == 'con2d_act':
            praes_pass_form = root + 'ούμαι'


        elif pres_conjugation == 'con2c_act':
            praes_pass_form = root + 'γομαι'


        elif pres_conjugation == 'con1_act':
            praes_pass_form = root + 'ομαι'

        if praes_pass_form and (praes_pass_form in greek_corpus or root[-3:] == 'ποι'):
            praes_pass_forms.append(praes_pass_form)
        if praes_pass_form_alt_1 and (praes_pass_form_alt_1 in greek_corpus):
            praes_pass_forms.append(praes_pass_form_alt_1)
        if praes_pass_form_alt_2 and (praes_pass_form_alt_2 in greek_corpus):
            praes_pass_forms.append(praes_pass_form_alt_2)

        praes_pass_forms = ','.join(praes_pass_forms)

        if praes_pass_forms:
            verb_temp['czas teraźniejszy'] = praes_form + '/' + praes_pass_forms
        else:
            verb_temp['czas teraźniejszy'] = praes_form
            intransitive_active = True

    elif modal_act:
        res = recognize_active_non_past_conjugation(praes_form)
        pres_conjugation = res['conjugation_ind']
        root = res['root']

        verb_temp['czas teraźniejszy'] = praes_form

    elif modal_med:
        res = recognize_passive_present_continuous_conjugation(praes_form)
        pres_conjugation = res['conjugation_ind']
        root = res['root']
        # modals and others


        verb_temp['czas teraźniejszy'] = praes_form

    # μέλλοντας και υποτακτική

    act_root, passive_root = None, None
    active_perf_form, passive_perf_form = '', ''

    if not_deponens:

        perf_forms = []
        act_root = create_regular_perf_root(praes_form)

        if not intransitive_active:
            passive_root = create_regular_perf_root(praes_form, voice="passive")
        # check for accent in root

        if act_root:
            if ',' in act_root:

                act_perf_forms = []
                for stem in act_root.split(','):
                    active_perf_form = stem + 'ω'

                    syllables = modern_greek_syllabify(active_perf_form)
                    if len(syllables) > 1 and not is_accented(syllables[-2]):
                        active_perf_form = act_root + 'ώ'
                    act_perf_forms.append(active_perf_form)

                active_perf_form = ','.join(act_perf_forms)



            else:
                active_perf_form = act_root + 'ω'

                syllables = modern_greek_syllabify(active_perf_form)
                if len(syllables) > 1 and not is_accented(syllables[-2]):
                    active_perf_form = act_root + 'ώ'

                # check for exv
                if praes_form[-3:] == 'έχω' and act_root + 'ει' not in greek_corpus:
                    active_perf_form = praes_form

            perf_forms.append(active_perf_form)

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

                perf_forms.append(passive_perf_form)

        perf_forms = '/'.join(perf_forms)



        verb_temp['czas przyszły (θα), tryb zależny prosty (να)'] = perf_forms

    elif deponens:

        passive_root = create_regular_perf_root(praes_form, voice="passive")


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

            verb_temp['czas przyszły (θα), tryb zależny prosty (να)'] = passive_perf_form

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


        verb_temp['czas przyszły (θα), tryb zależny prosty (να)'] = active_perf_form

    elif modal_med:
        perf_root = None
        if praes_form[-4:] == 'εται':
            perf_root = create_regular_perf_root(root + 'ομαι', 'passive')
            if perf_root and perf_root + 'εί' not in greek_corpus:
                perf_root = create_regular_perf_root(root + 'μαι', 'passive')
        elif praes_form[-5:] == 'είται':
            perf_root = create_regular_perf_root(root + 'ούμαι', 'passive')
        elif praes_form[-4:] == 'άται':
            perf_root = create_regular_perf_root(root + 'άμαι', 'passive')
            if perf_root and perf_root + 'εί' not in greek_corpus:
                perf_root = create_regular_perf_root(root + 'ώμαι', 'passive')
        elif praes_form[-4:] == 'αται':
            perf_root = create_regular_perf_root(root + 'αμαι', 'passive')
        elif praes_form[-3:] == 'ται':
            perf_root = create_regular_perf_root(root + 'μαι', 'passive')
        passive_root = perf_root

        if perf_root:
            verb_temp['czas przyszły (θα), tryb zależny prosty (να)'] = passive_root + 'εί'

    # aoryst

    active_aor_forms, passive_aor_form = [], []

    if not_deponens:
        aor_forms = []

        #act_root = create_regular_perf_root(praes_form)
        #passive_root = create_regular_perf_root(praes_form, voice="passive")

        if intransitive_active:

            if len(praes_form) >= 5 and praes_form[-5:] == 'βαίνω':
                active_aor_forms = act_root + 'ηκα'
                active_aor_forms = add_augment(active_aor_forms)
                archaic_aor_form = add_augment(act_root + 'η')
                active_aor_forms.extend(archaic_aor_form)
            elif len(praes_form) >= 6 and praes_form[-6:] in ['μπαίνω', 'βγαίνω', 'βρίσκω']:
                act_root = act_root + 'ηκ'

                # briskw is only found in one form, so no reason to add to code
            elif len(praes_form) >= 7 and praes_form[-7:] == 'πηγαίνω':
                act_root = 'πήγ'

        if act_root:

            # take care of those roots that are irregular in aoryst (εχω, είχα κτλ)

            if len(praes_form) >=5 and praes_form[-5:] == 'βλέπω':
                active_aor_forms.extend(add_augment(praes_form[:-5] + 'είδα'))
                passive_aor_form.extend(add_augment(praes_form[:-5] + 'ειδώθηκα'))

            elif len(praes_form) >=4 and praes_form[-4:] == 'λέγω':
                active_aor_forms.extend(add_augment(praes_form[:-4] + 'είπα'))
                passive_aor_form.extend(add_augment(praes_form[:-4] + 'ειπώθηκα'))
            elif len(praes_form) >=3 and praes_form[-3:] == 'λέω':
                active_aor_forms.extend(add_augment(praes_form[:-3] + 'είπα'))
                passive_aor_form.extend(add_augment(praes_form[:-3] + 'ειπώθηκα'))

            elif praes_form[-4:] == ('πίνω'):
                active_aor_forms.extend(add_augment(praes_form[:-4] + 'ήπια'))
            elif praes_form[-6:] == 'βρίσκω':
                active_aor_forms.extend(add_augment(praes_form[:-6] + 'βρήκα'))
                passive_aor_form.extend(add_augment(praes_form[:-6] + 'βρέθηκα'))
            elif len(praes_form) >= 6 and praes_form[-6:] == 'παίρνω':
                active_aor_forms.extend(add_augment(praes_form[:-6]+'πήρα'))
                passive_aor_form.extend(add_augment(praes_form[:-6]+'πάρθηκα'))
            elif praes_form[-4:] == 'τρώω' or praes_form[-5:] == 'τρώγω':
                active_aor_forms.extend(add_augment(praes_form[:-5] + 'φαγα'))
                passive_aor_form.extend(add_augment(praes_form[:-5] + 'φαγώθηκα'))
            elif praes_form[-4:] == 'τρώω' or praes_form[-5:] == 'τρώγω':
                active_aor_forms.extend(add_augment(praes_form[:-5] + 'φαγα'))
                passive_aor_form.extend(add_augment(praes_form[:-5] + 'φαγώθηκα'))

            if ',' in act_root:
                for stem in act_root.split(','):
                    active_aor_forms.extend(add_augment(stem + 'α'))

            else:
                active_aor_forms.extend(add_augment(act_root + 'α'))

            if praes_form[-3:] == ('έχω'):
                active_aor_forms.extend([praes_form[:-3] + 'είχα'])

                archaic_aor_form = add_augment(praes_form[:-3] + 'σχον')

                active_aor_forms.extend(archaic_aor_form)

            # filter_out

            active_aor_forms = [f for f in active_aor_forms if f in greek_corpus]


            # filter out 2 syllables without augment
            #active_aor_forms = [f for f in active_aor_forms if not (count_syllables(
            #    f) == 2 and f[0] not in vowels and f not in ['πήρα', 'πήγα', 'βρήκα', 'βγήκα', 'μπήκα'])]
            active_aor_forms = list(set(active_aor_forms))


            # special case for poiw
            if 'ποιήσ' in act_root:
                active_aor_forms.append(put_accent_on_the_antepenultimate(act_root + 'α', true_syllabification=False))

        if passive_root or passive_aor_form:
            if passive_root and ',' in passive_root:

                for stem in passive_root.split(','):
                    pass_aor_form = stem + 'ηκα'

                    passive_aor_form.append(put_accent_on_the_antepenultimate(pass_aor_form))

                    # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in
                    # corpus
                    archaic_passive_aor = stem + 'η'

                    archaic_passive_aor = add_augment(archaic_passive_aor)
                    passive_aor_form.extend(archaic_passive_aor)

            elif passive_root:
                pass_aor_form = passive_root + 'ηκα'

                pass_aor_form = put_accent_on_the_antepenultimate(pass_aor_form)
                passive_aor_form.append(pass_aor_form)
                # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in
                # corpus
                archaic_passive_aor = passive_root + 'η'

                archaic_passive_aor = add_augment(archaic_passive_aor)

                passive_aor_form.extend(archaic_passive_aor)

                if 'ποιηθ' in passive_root:
                    passive_aor_form.append(put_accent_on_the_antepenultimate(passive_root + 'ηκα', true_syllabification=False))
            # filter out

            passive_aor_form = [f for f in passive_aor_form if f in greek_corpus]







        #if active_aor_forms:
        active_aor_forms = ','.join(active_aor_forms)
        #if passive_aor_form:
        passive_aor_form = ','.join(passive_aor_form)

        aor_forms = '/'.join([active_aor_forms, passive_aor_form])

        verb_temp['aoryst'] = aor_forms

    elif deponens:

        if passive_root:


            if ',' in passive_root:
                passive_aor_form = []
                for stem in passive_root.split(','):
                    pass_aor_form = stem + 'ηκα'

                    passive_aor_form.extend(put_accent_on_the_antepenultimate(pass_aor_form))

                    # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in
                    # corpus
                    archaic_passive_aor = stem + 'η'

                    archaic_passive_aor = add_augment(archaic_passive_aor)

                    passive_aor_form.extend(archaic_passive_aor)

            else:
                passive_aor_form = passive_root + 'ηκα'

                passive_aor_form = [put_accent_on_the_antepenultimate(passive_aor_form)]
                # archaic passive
                archaic_passive_aor = passive_root + 'ην'
                archaic_passive_aor = add_augment(archaic_passive_aor)

                passive_aor_form.extend(archaic_passive_aor)
            # filter out

            passive_aor_form = [f for f in passive_aor_form if f in greek_corpus]
            passive_aor_form = ','.join(passive_aor_form)


            # ginomai, erxomai, kathomai

            if praes_form[-7:] in ['γίνομαι', 'έρχομαι', 'κάθομαι']:

                if ',' in passive_root:
                    passive_aor_form = []
                    for stem in passive_root.split(','):

                        pass_aor_form = stem + 'α'

                        passive_aor_form.extend(add_augment(pass_aor_form))



                else:

                    passive_aor_form = passive_root + 'α'
                    passive_aor_form = add_augment(passive_aor_form)

                passive_aor_form = [form for form in passive_aor_form if form in greek_corpus]

                passive_aor_form = ','.join(passive_aor_form)

            if 'ποιηθ' in passive_root:
                passive_aor_form = (passive_root + 'ηκα')

            verb_temp['aoryst'] = passive_aor_form

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
            aor_forms.extend(anc_forms)

            aor_forms = [f for f in aor_forms if f in greek_corpus]

            aor_forms = ','.join(aor_forms)
            verb_temp['aoryst'] = aor_forms


    # paratatikos
    #praes_form = remove_accent(praes_form)

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

        elif pres_conjugation == 'con2c_act':
            not_augmented_par = root + 'γα'
            act_par = add_augment(not_augmented_par)

            pass_par = [put_accent_on_the_penultimate(root + 'γόμουν')]

        elif pres_conjugation == 'eimai':
            act_par = ['ήμουν']

        act_par = [f for f in act_par if f in greek_corpus]
        pass_par = [f for f in pass_par if f in greek_corpus]
        act_par = ','.join(act_par)
        pass_par = '.'.join(pass_par)

        parat = '/'.join([act_par, pass_par])
        if root[-3:] == 'ποι':
            parat = root + 'ούσα/' + root + 'ούμουν'

        verb_temp['paratatikos'] = parat

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
            pass_par = root + 'ούμουν'
        verb_temp['paratatikos'] = pass_par

    elif modal_act:
        parat_act_forms = []

        if praes_form[-3:] == 'άει':
            parat_act_forms = add_augment(praes_form[:-3] + 'ούσε')
            parat_act_forms.extend(add_augment(praes_form[:-3] + 'αγε'))
        elif praes_form[-3:] == 'ά':
            parat_act_forms = add_augment(praes_form[:-1] + 'ούσε')
            parat_act_forms.extend(add_augment(praes_form[:-1] + 'γε'))
        elif praes_form[-2:] == 'ει':
            parat_act_forms = add_augment(praes_form[:-2] + 'ε')

        elif praes_form[-2:] == 'εί':
            parat_act_forms = add_augment(praes_form[:-2] + 'ούσε')

        parat_act_forms = [f for f in parat_act_forms if f in greek_corpus]
        parat_act_forms = ','.join(parat_act_forms)

        verb_temp['paratatikos'] = parat_act_forms

    elif modal_med:

        parat_med_forms = ''
        if praes_form[-5:] == 'ιέται':
            parat_med_forms = [root + 'ιόταν']

        elif praes_form[-5:] == 'είται':
            parat_med_forms = add_augment(root + 'είτο')
            parat_med_forms.extend([root + 'ούνταν'])

        elif praes_form[-4:] == 'άται':
            parat_med_forms = [root + 'άτο', root + 'όταν', root + 'ιόταν']

        elif praes_form[-4:] == 'εται':
            parat_med_forms = [root + 'όταν', root + 'ετο']
        elif praes_form[-5:] == 'ειται':
            parat_med_forms = [root + 'ειτο']
            parat_med_forms.extend(add_augment(parat_med_forms[0]))

        parat_med_forms = [f for f in parat_med_forms if f in greek_corpus]
        parat_med_forms = '.'.join(parat_med_forms)
        verb_temp['paratatikos'] = parat_med_forms


    # praes_part_act

    praes_part_act = ''
    if pres_conjugation == 'con1_act':
        praes_part_act = root + 'οντας'

    elif pres_conjugation in ['con2a_act', 'con2b_act', 'con2ab_act']:
        praes_part_act = root + 'ώντας'

    elif pres_conjugation == 'con2c_act':
        praes_part_act = root + 'γοντας'

    elif pres_conjugation == 'eimai':
        praes_part_act = 'όντας'

    if praes_part_act and praes_part_act in greek_corpus or root[-3:] == 'ποι':
        verb_temp['act_pres_participle'] = praes_part_act

    # archaic praes part act

    arch_praes_part_act = ''
    if pres_conjugation == 'con1_act':
        if root + 'ων' in greek_corpus and root + 'ουσα' in greek_corpus:
            arch_praes_part_act = root + 'ων/' + root + 'ουσα/' + root + 'ον'

    elif pres_conjugation in ['con2a_act', 'con2ab_act']:
        if root + 'ών' in greek_corpus and root + 'ώσα' in greek_corpus:
            arch_praes_part_act = root + 'ών/' + root + 'ώσα/' + root + 'ών'

    elif pres_conjugation in ['con2b_act', 'con2d_act']:
        if root + 'ών' in greek_corpus and root + 'ούντα' in greek_corpus:
            arch_praes_part_act = root + 'ών/' + root + 'ούσα/' + root + 'ούν'

    elif pres_conjugation == 'con2c_act':
        if root + 'γων' in greek_corpus and root + 'γοντα' in greek_corpus:
            arch_praes_part_act = root + 'γων/' + root + 'γουσα/' + root + 'γον'

    elif pres_conjugation == 'eimai':

        if root + 'ων' in greek_corpus and root + 'όντα' in greek_corpus:
            arch_praes_part_act = put_accent_on_the_ultimate(root + 'ων/', accent_one_syllable=False) + put_accent_on_the_penultimate(root + \
                                  'ούσα/') + put_accent_on_the_ultimate(root + 'ον', accent_one_syllable=False)


    if arch_praes_part_act:

        verb_temp['arch_act_pres_participle'] = arch_praes_part_act

    # pres part pass
    praes_part_pass = ''
    part_root = remove_all_diacritics(root)

    if pres_conjugation in ['con1_act', 'con1_pass']:
        praes_part_pass = part_root + 'όμενος'

    elif pres_conjugation in ['con2a_act', 'con2ab_pass', 'con2a_pass']:
        praes_part_pass = part_root + 'ώμενος'

    elif pres_conjugation == 'con2c_act':
        praes_part_pass = part_root + 'γόμενος'

    elif pres_conjugation in ['con2b_act', 'con2b_pass', 'con2c_pass', 'con2d_act']:

        praes_part_pass = part_root + 'ούμενος'
    elif pres_conjugation == 'con2e_pass':
        praes_part_pass = part_root + 'άμενος'
    elif pres_conjugation == 'con2d_pass':
        praes_part_pass = put_accent_on_the_antepenultimate(root + 'μενος')

    # special case for xairomai
    if part_root == 'χαιρ':
        praes_part_pass = 'χαρούμενος'

    if praes_part_pass and praes_part_pass in greek_corpus or root[-3:] == 'ποι':

        verb_temp['pass_pres_participle'] = praes_part_pass + '/' + praes_part_pass[:-2] + 'η' + '/' + praes_part_pass[:-1]


    # past_pass_part
    past_participles = []

    # check for irregularities
    irregular_ppart = past_perfect_participles

    for pr_f in irregular_ppart.keys():

        if pr_f == praes_form[-(len(pr_f)):] and irregular_ppart[pr_f]:


            part = praes_form[:-len(pr_f)] + irregular_ppart[pr_f]
            part_aug = add_augment(part)
            print(part, part_aug, 'part')
            if part in greek_corpus:
                past_participles = [part]

            for p in part_aug:
                if p in greek_corpus:
                    past_participles.append(p)


                break


    if passive_root and not past_participles:

        if passive_root[-2:] == 'νθ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-2] + 'σμενος')
        elif passive_root[-2:] == 'στ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')



        elif passive_root[-1] == 'θ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
        elif passive_root[-2:] == 'φτ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-2] + 'μμενος')
        elif passive_root[-1] == 'φ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-1] + 'μμενος')

        elif passive_root[-3:] == 'ευτ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-2] + 'μενος')
            if act_root and act_root[-1] == 'σ':
                past_part_pass = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
            if past_part_pass not in greek_corpus:
                past_part_pass = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
        elif passive_root[-2:] == 'χτ':
            past_part_pass = put_accent_on_the_penultimate(passive_root[:-2] + 'γμενος')
        else:
            past_part_pass = put_accent_on_the_penultimate(passive_root + 'μένος')

        past_participles = add_augment(past_part_pass)

        past_participles = [f for f in past_participles if f in greek_corpus]
        if root[-3:] == 'ποι':
            past_participles = [root+'ημένος']



    if not passive_root and act_root and not past_participles:

        if act_root[-2:] in ['ύσ', 'άσ', 'ίσ']:
            past_part_pass = put_accent_on_the_penultimate(act_root + 'μενος')

        elif act_root[-1] in ['σ', 'ν']:
            past_part_pass = put_accent_on_the_penultimate(act_root[:-1] + 'μενος')
            if past_part_pass not in greek_corpus:
                past_part_pass = put_accent_on_the_penultimate(act_root[:-1] + 'σμενος')
        elif act_root[-1] == 'ξ':
            past_part_pass = put_accent_on_the_penultimate(act_root[:-1] + 'γμενος')
        elif praes_form[-3:] == 'αίν':
            past_part_pass = put_accent_on_the_penultimate(act_root[:-3] + 'ημενος')
            if past_part_pass not in greek_corpus:
                past_part_pass = put_accent_on_the_penultimate(act_root[:-3] + 'αμενος')

        if past_part_pass:
            past_participles = add_augment(past_part_pass)

            past_participles = [f for f in past_participles if f in greek_corpus]

    if past_participles:
        # these are all possible participles in masc sg!!!
        verb_temp['passive_perfect_participle'] = '/'.join(past_participles)






    # active aorist
    if act_root:

        if 'passive_perfect_participle' in verb_temp and verb_temp['passive_perfect_participle'][-2:] in ['άς', 'άν']:
            # correcting improper categorization of part on an
            print(act_root, 'ppp on an, as')
            verb_temp['active_aorist_participle'] = act_root + 'άς/' + act_root + 'άσα/' + act_root + 'άν'
        # on as
        if act_root + 'ας' in greek_corpus and act_root + 'ασα' in greek_corpus or root[-3:] == 'ποι':
            verb_temp['active_aorist_participle'] = act_root + 'ας/' + act_root + 'ασα/' + act_root + 'αν'
        elif act_root + 'ών' in greek_corpus and act_root + 'ούσα' in greek_corpus:
            verb_temp['active_aorist_participle'] = act_root + 'ών/' + act_root + 'ούσα/' + act_root + 'όν'

    # passive aorist
    if passive_root:
        if passive_root + 'είσα' in greek_corpus:
            verb_temp['passive_aorist_participle'] = passive_root + 'είς/' + passive_root + 'είσα/' + passive_root + 'έν'



    if with_prothesis:
        for key, value in verb_temp.items():

            forms = value.split('/')
            with_p_f = []
            for form in forms:
                if ',' in form:
                    form = form.split(',')
                    with_p = []
                    for f in form:
                        with_p.append(with_prothesis+f)
                    form = ','.join(with_p)
                    with_p_f.append(form)
                else:
                    form = with_prothesis + form
                    with_p_f.append(form)
            forms = '/'.join(with_p_f)
            verb_temp[key] = forms




    return verb_temp
# create list of all verbs with their basic forms. Check them with existing forms and if they already exist,
# leave them out



def create_list_of_greek_basic_verb_forms():
    file = open('modern_greek_stemmer/lekseis_kata_pos.pickle', 'br')
    all_lekseis = pickle.load(file)
    all_verbs = all_lekseis['verb']
    all = []
    for verb in all_verbs:
        lemma = verb[0]

        verb_temp = create_all_basic_forms(lemma)
        if verb_temp:
            all.append(verb_temp)

    file = open('modern_greek_stemmer/all_greek_verbs.pickle', 'wb')
    pickle.dump(all, file)
    file.close()



