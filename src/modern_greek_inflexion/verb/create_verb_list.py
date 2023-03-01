from .verb_stemmer import create_basic_present_forms, create_basic_conjunctive_forms, create_basic_aorist_forms, \
    create_basic_paratatikos_forms, create_present_active_participle, create_present_active_participle_arch, \
    create_present_passive_participle, create_passive_perfect_participle, create_active_aorist_participle, \
    create_passive_aorist_participle
from ..resources import greek_corpus, irregular_passive_roots
from ..resources import ACTIVE, PASSIVE, DEPONENS, MODAL, AORIST, PRESENT, PARATATIKOS, CONJUNCTIVE
from ..exceptions import NotLegalVerbException, NotInGreekException

import re

greek_pattern = re.compile('[ά-ώ|α-ω]+', re.IGNORECASE)


def create_all_basic_forms(pres_form):
    """
   :param pres_form: 1st person sg present
   :return: a dictionary {PRESENT: '', CONJUNCTIVE: '', AORIST: '', PARATATIKOS: ''} and others, for times it
   gives active and medio-passive (if exists) divided by '/'.
   Modals are given in 3rd person, alternative formse are separated by coma,
   passive participles on menos are given only in masc separated by coma
   if there are alternatives
    """

    if not greek_pattern.match(pres_form):
        raise NotInGreekException

    if pres_form not in greek_corpus and pres_form[-2:] == 'άω':
        pres_form = pres_form[:-2] + 'ώ'

    if not pres_form or (pres_form[-1] not in ['ω', 'ώ']
                         and pres_form[-2:] not in ['ει', 'εί']
                         and pres_form[-3:] not in ['ται', 'μαι']) \
            or pres_form[-4:] == 'νται' \
            or pres_form not in greek_corpus:
        raise NotLegalVerbException

    verb_temp = {}

    not_deponens = True
    deponens = False
    intransitive_active = False
    if pres_form in ['είμαι', 'παραείμαι']:
        deponens = False
        not_deponens = True
    elif 'μαι' == pres_form[-3:]:
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

    modal = modal_act or modal_med

    # presens

    present_basic, pres_conjugation, root, intransitive_active = create_basic_present_forms(pres_form,
                                                                                            deponens=deponens,
                                                                                            not_deponens=not_deponens,
                                                                                            intransitive_active=intransitive_active,
                                                                                            modal_act=modal_act,
                                                                                            modal_med=modal_med)



    if pres_form[:-1] in sum(irregular_passive_roots, []):
        intransitive_active = False

    pres_act = pres_pass = None
    try:
        pres_act, pres_pass = present_basic.split('/')
        pres_act = pres_act.split(',')
        pres_pass = pres_pass.split(',')
    except ValueError:
        if present_basic[-1] in ['ω', 'ώ'] or present_basic[-2:] in ['ει', 'εί'] or present_basic in ['είμαι',
                                                                                                      'παραείμαι']:
            pres_act = present_basic.split(',')
        elif present_basic[-3:] in ['μαι', 'ται']:
            pres_pass = present_basic.split(',')

    verb_temp[PRESENT] = {}
    if pres_act:
        verb_temp[PRESENT][ACTIVE] = set(pres_act)
    if pres_pass:
        verb_temp[PRESENT][PASSIVE] = set(pres_pass)

    # μέλλοντας και υποτακτική

    conjunctive_basic_forms, perf_root, act_root, passive_root = \
        create_basic_conjunctive_forms(pres_form,
                                       pres_conjugation,
                                       root,
                                       deponens=deponens,
                                       not_deponens=not_deponens,
                                       intransitive_active=intransitive_active,
                                       modal_act=modal_act,
                                       modal_med=modal_med)

    if conjunctive_basic_forms:

        verb_temp[CONJUNCTIVE] = {}
        conjunctive_act, conjunctive_pass = conjunctive_basic_forms.split('/')

        conjunctive_act = conjunctive_act.split(',')
        conjunctive_pass = conjunctive_pass.split(',')

        if conjunctive_act and conjunctive_act[0]:
            verb_temp[CONJUNCTIVE][ACTIVE] = set(conjunctive_act)
        if conjunctive_pass and conjunctive_pass[0]:
            verb_temp[CONJUNCTIVE][PASSIVE] = set(conjunctive_pass)

    # aorist

    aorist_basic_forms = create_basic_aorist_forms(pres_form, act_root, passive_root, deponens=deponens,
                                                   not_deponens=not_deponens, intransitive_active=intransitive_active,
                                                   modal_act=modal_act, modal_med=modal_med)

    if aorist_basic_forms:
        verb_temp[AORIST] = {}
        aorist_active, aorist_passive = aorist_basic_forms.split('/')
        aorist_active = aorist_active.split(',')
        aorist_passive = aorist_passive.split(',')
        if aorist_active and aorist_active[0]:
            verb_temp[AORIST][ACTIVE] = set(aorist_active)
        if aorist_passive and aorist_passive[0]:
            verb_temp[AORIST][PASSIVE] = set(aorist_passive)

    # paratatikos

    paratatikos_basic_forms = create_basic_paratatikos_forms(pres_form, root, pres_conjugation, deponens=deponens,
                                                             not_deponens=not_deponens, modal_act=modal_act,
                                                             modal_med=modal_med)

    if paratatikos_basic_forms:
        paratatikos_active, paratatikos_passive = paratatikos_basic_forms.split('/')
        paratatikos_active = paratatikos_active.split(',')
        paratatikos_passive = paratatikos_passive.split(',')

        verb_temp[PARATATIKOS] = {}
        if paratatikos_active and paratatikos_active[0]:
            verb_temp[PARATATIKOS][ACTIVE] = set(paratatikos_active)
        if paratatikos_passive and paratatikos_passive[0]:
            verb_temp[PARATATIKOS][PASSIVE] = set(paratatikos_passive)

    # pres_part_act

    present_participle_active = create_present_active_participle(pres_form, root, pres_conjugation)

    if present_participle_active and not modal:
        verb_temp['act_pres_participle'] = set(present_participle_active.split(','))

    # archaic praes part act

    present_participle_active_archaic = create_present_active_participle_arch(pres_form, root, pres_conjugation)

    if present_participle_active_archaic and not modal:
        verb_temp['arch_act_pres_participle'] = set(present_participle_active_archaic.split(','))

    # pres part pass

    present_participle_passive = create_present_passive_participle(pres_form, root, pres_conjugation)

    if present_participle_passive and not modal:
        verb_temp['pass_pres_participle'] = set(present_participle_passive.split(','))

    # passive_perfect_participles

    if 'passive_perfect_participle' in verb_temp and verb_temp['passive_perfect_participle'][-2:] in ['άς',
                                                                                                      'άν'] and not modal:
        # correcting improper categorization of part on an

        verb_temp['active_aorist_participle'] = {act_root + 'άς/' + act_root + 'άσα/' + act_root + 'άν'}
        verb_temp['passive_perfect_participle'] = {''}

    passive_perfect_participles = create_passive_perfect_participle(pres_form, root, act_root, passive_root)

    if passive_perfect_participles and not modal:
        verb_temp['passive_perfect_participle'] = set(passive_perfect_participles.split(','))

    # active aorist participle

    if act_root and not modal:

        active_aorist_participle = create_active_aorist_participle(root, act_root)
        if active_aorist_participle:
            verb_temp['active_aorist_participle'] = set(active_aorist_participle.split(','))

    # passive aorist participle
    if passive_root and not modal:
        passive_aorist_participle = create_passive_aorist_participle(passive_root)
        if passive_aorist_participle:
            verb_temp['passive_aorist_participle'] = set(passive_aorist_participle.split(','))

    verb_temp[MODAL] = modal_act or modal_med

    return verb_temp
# create list of all verbs with their basic forms. Check them with existing forms and if they already exist,
# leave them out
