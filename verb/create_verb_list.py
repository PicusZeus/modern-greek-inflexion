import pickle

from modern_greek_accentuation.resources import vowels

from .conjugations import create_regular_perf_root, recognize_active_non_past_conjugation, \
    recognize_passive_present_continuous_conjugation
from .verb_stemmer import create_basic_present_forms, create_basic_conjunctive_forms, create_basic_aorist_forms, create_basic_paratatikos_forms, create_present_active_participle, create_present_active_participle_arch, create_present_passive_participle, create_passive_perfect_participle
from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, put_accent_on_the_antepenultimate,\
    count_syllables, remove_all_diacritics, is_accented, put_accent_on_the_ultimate
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.syllabify import modern_greek_syllabify
from .greek_tables import irregular_passive_perfect_participles
"""
create lists of words that can be easily parsed by existing code.
Firstly, create list of verbs together with all the basic forms in the form:




creating them automatically from the list 'lekseis_kata_pos.pickle', where you have probably all greek verbs.
Also to check if the created forms actually exist check them with this simple el_GR.dic.
"""
file = open('el_GR.pickle', 'rb')
greek_corpus = pickle.load(file)
file.close()


def create_all_basic_forms(pres_form):

    """
   :param pres_form: 1st person sg present
   :return: a dictionary {'present': '', 'conjunctive': '', 'aorist': '', 'paratatikos': ''} and others, for times it gives active and medio-passive (if exists) divided by '/'. Modals are given in 3rd person, alternative formse are separated by coma
    """

    if pres_form[-1] not in ['ω', 'ώ', 'ι', 'α'] or pres_form not in greek_corpus:
        # filter out possible not correct forms
        print('It is not a correct verb form. You have to input 1st person sg present in active voice if possible, or modal form in 3rd person sg, and your input is: ' + pres_form)
        return None

    verb_temp = {}

    not_deponens = True
    deponens = False
    intransitive_active = False
    passive_perfect_participle  = ''
    pres_conjugation = 'con1_act'

    if 'μαι' == pres_form[-3:] and not 'είμαι' == pres_form:
        #  deponens
        deponens = True
        not_deponens = False
        pres_conjugation = 'con1_pass'

    modal_act = False
    modal_med = False
    if pres_form[-2:] in ['ει', 'εί']:
        modal_act = True
        not_deponens = False
    if pres_form[-3:] == 'ται':
        modal_med = True
        not_deponens = False

    root = ''

    # prepositions that are sometimes added to a verb but do not have any impact on the way they are declined
    with_prothesis = False
    protheseis = ['ξανα', 'πρωτο', 'κακο', 'υπερ']
    # if they are at the beginning of the verb and such a verb exist
    for prothesis in protheseis:
        if pres_form[:len(prothesis)] == prothesis and pres_form[len(prothesis):] in greek_corpus:
            pres_form = pres_form[len(prothesis):]
            with_prothesis = prothesis

    # presens

    present_basic, pres_conjugation, root, intransitive_active = create_basic_present_forms(pres_form, deponens=deponens, not_deponens=not_deponens, intransitive_active=intransitive_active, modal_act=modal_act, modal_med=modal_med)

    verb_temp['present'] = present_basic

    # μέλλοντας και υποτακτική

    conjunctive_basic_forms, perf_root, act_root, passive_root = create_basic_conjunctive_forms(pres_form, pres_conjugation, root, deponens=deponens, not_deponens=not_deponens, intransitive_active=intransitive_active, modal_act=modal_act, modal_med=modal_med)

    if conjunctive_basic_forms:
        verb_temp['conjunctive'] = conjunctive_basic_forms



    # aoristos

    aorist_basic_forms = create_basic_aorist_forms(pres_form, act_root, passive_root, deponens=deponens, not_deponens=not_deponens, intransitive_active=intransitive_active, modal_act=modal_act, modal_med=modal_med)

    if aorist_basic_forms:
        verb_temp['aorist'] = aorist_basic_forms

    # paratatikos

    paratatikos_basic_forms = create_basic_paratatikos_forms(pres_form, root, pres_conjugation, deponens=deponens, not_deponens=not_deponens, modal_act=modal_act, modal_med=modal_med)

    if paratatikos_basic_forms:
        verb_temp['paratatikos'] = paratatikos_basic_forms

    # pres_part_act

    present_participle_active = create_present_active_participle(pres_form, root, pres_conjugation)

    if present_participle_active:
        verb_temp['act_pres_participle'] = present_participle_active


    # archaic praes part act

    present_participle_active_archaic = create_present_active_participle_arch(pres_form, root, pres_conjugation)

    if present_participle_active_archaic:
        verb_temp['arch_act_pres_participle'] = present_participle_active_archaic

    # pres part pass

    present_participle_passive = create_present_passive_participle(pres_form, root, pres_conjugation)

    if present_participle_passive:
        verb_temp['pass_pres_participle'] = present_participle_passive


    # passive_perfect_participles

    if 'passive_perfect_participle' in verb_temp and verb_temp['passive_perfect_participle'][-2:] in ['άς', 'άν']:
        # correcting improper categorization of part on an

        verb_temp['active_aorist_participle'] = act_root + 'άς/' + act_root + 'άσα/' + act_root + 'άν'
        verb_temp['passive_perfect_participle'] = ''

    passive_perfect_participles = create_passive_perfect_participle(pres_form, root, act_root, passive_root)

    if passive_perfect_participles:
        verb_temp['passive_perfect_participle'] = passive_perfect_participles

    # active aorist participle

    if act_root:
        if 'passive_perfect_participle' in verb_temp and verb_temp['passive_perfect_participle'][-2:] in ['άς', 'άν']:
            # correcting improper categorization of part on an

            verb_temp['active_aorist_participle'] = act_root + 'άς/' + act_root + 'άσα/' + act_root + 'άν'
            verb_temp['passive_perfect_participle'] = ''
        # on as
        if act_root + 'ας' in greek_corpus and act_root + 'ασα' in greek_corpus or root[-3:] == 'ποι':
            verb_temp['active_aorist_participle'] = act_root + 'ας/' + act_root + 'ασα/' + act_root + 'αν'
        elif act_root + 'ών' in greek_corpus and act_root + 'ούσα' in greek_corpus:
            verb_temp['active_aorist_participle'] = act_root + 'ών/' + act_root + 'ούσα/' + act_root + 'όν'

    # passive aorist participle
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



