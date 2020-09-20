import pickle

from .verb_stemmer import create_basic_present_forms, create_basic_conjunctive_forms, create_basic_aorist_forms, create_basic_paratatikos_forms, create_present_active_participle, create_present_active_participle_arch, create_present_passive_participle, create_passive_perfect_participle, create_active_aorist_participle, create_passive_aorist_participle

with open('el_GR.pickle', 'rb') as file:
    greek_corpus = pickle.load(file)


def create_all_basic_forms(pres_form):

    """
   :param pres_form: 1st person sg present
   :return: a dictionary {'present': '', 'conjunctive': '', 'aorist': '', 'paratatikos': ''} and others, for times it gives active and medio-passive (if exists) divided by '/'. Modals are given in 3rd person, alternative formse are separated by coma, passive participles on menos are given only in masc separated by coma
   if there are alternatives
    """

    if pres_form[-1] not in ['ω', 'ώ', 'ι', 'α'] or pres_form not in greek_corpus:
        # filter out possible not correct forms
        print(pres_form, 'error', pres_form[-1] not in ['ω', 'ώ', 'ι', 'α'])
        print('It is not a correct verb form. You have to input 1st person sg present in active voice if possible, or modal form in 3rd person sg, and your input is: ' + pres_form)
        return None

    verb_temp = {}

    not_deponens = True
    deponens = False
    intransitive_active = False

    if 'μαι' == pres_form[-3:] and not 'είμαι' == pres_form:
        #  deponens
        deponens = True
        not_deponens = False

    modal_act = False
    modal_med = False
    if pres_form[-2:] in ['ει', 'εί']:
        modal_act = True
        not_deponens = False
    if pres_form[-3:] == 'ται':
        modal_med = True
        not_deponens = False

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

    # aorist

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
        active_aorist_participle = create_active_aorist_participle(root, act_root)
        if active_aorist_participle:
            verb_temp['active_aorist_participle'] = active_aorist_participle

    # passive aorist participle
    if passive_root:
        passive_aorist_participle = create_passive_aorist_participle(passive_root)
        if passive_aorist_participle:
            verb_temp['passive_aorist_participle'] = passive_aorist_participle

    if with_prothesis:
        # because my db lacks compound verbs with common prefixes like ksana etc. it is a way to get all the forms, though
        # I am not sure if I really need them in my db... for the sake of completeness I will add them
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





