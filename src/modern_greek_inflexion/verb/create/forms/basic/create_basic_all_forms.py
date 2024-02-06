
from modern_greek_inflexion.verb.create.forms.basic.create_basic_aorist_forms import create_basic_aorist_forms
from modern_greek_inflexion.verb.create.forms.basic.create_basic_conjunctive_forms import create_basic_conjunctive_forms
from modern_greek_inflexion.verb.create.forms.basic.create_basic_paratatikos_forms import create_basic_paratatikos_forms
from modern_greek_inflexion.verb.create.forms.basic.create_basic_present_forms import create_basic_present_forms
from modern_greek_inflexion.verb.create.forms.basic.participles.create_aorist_participles import \
    create_active_aorist_participle, create_passive_aorist_participle
from modern_greek_inflexion.verb.create.forms.basic.participles.create_passive_perfect_participle import \
    create_passive_perfect_participle
from modern_greek_inflexion.verb.create.forms.basic.participles.create_present_active_participle import \
    create_present_active_participle
from modern_greek_inflexion.verb.create.forms.basic.participles.create_present_active_participle_arch import \
    create_present_active_participle_arch
from modern_greek_inflexion.verb.create.forms.basic.participles.create_present_passive_participle import \
    create_present_passive_participle
from modern_greek_inflexion.verb.helpers import update_forms_with_prefix
from modern_greek_accentuation.accentuation import remove_diaer, put_accent_on_the_penultimate, \
    put_accent_on_the_antepenultimate, where_is_accent, put_accent_on_the_ultimate
from modern_greek_accentuation.syllabify import count_syllables
from modern_greek_accentuation.augmentify import deaugment_past_form
from modern_greek_inflexion.resources.verb import prefixes_detachable, prefixes_detachable_weak, \
    prefixes_before_augment, para_detachable_never, para_detachable_only
from modern_greek_inflexion.resources.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_passive_roots
from modern_greek_inflexion.resources.variables import ACTIVE, PASSIVE, MODAL, AORIST, PRESENT, PARATATIKOS, \
    CONJUNCTIVE, ACT_PRES_PARTICIPLE, ARCH_ACT_PRES_PARTICIPLE, PASSIVE_PERFECT_PARTICIPLE, ACTIVE_AORIST_PARTICIPLE, \
    PASSIVE_AORIST_PARTICIPLE
from modern_greek_inflexion.exceptions import NotLegalVerbException, NotInGreekException

import re

greek_pattern = re.compile('[ά-ώ|α-ω]+', re.IGNORECASE)


def create_all_basic_forms(pres_form: str, para: bool = False) -> dict:
    """
    :param para: there is a problem with prefix para, which can mean different things and so a verb prefixed with it can mean
    either "too much", and "from above". In the first instance it is fully detachable and a verb is conjugated
    as if it was a root verb, in the second instance the perfective tense can be different and also augment is handled
    differently. So I will add a flag 'para', so that if false it can be conjugated as a simple verb, if true, as
    a detachable verb
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

    # prefixes
    """ 
    common logia verbs that create all the archaic forms also when prefixed 
    """
    archaic_detachable = ['καίω', 'επενδύω', 'εκδύω', 'λύω', 'δεικνύω', 'ζευγνύω', 'νέμω', 'πέμπω', 'λάμπω', 'τρέπω',
                          'ελκύω', 'σβεννύω', 'πτύω', 'συμπηγνύω', 'ρρέω', 'ρέω', 'στέλλω', 'βάλλω', 'πλέκομαι',
                          'μέλπω', 'βαίνω', 'τέμνω', 'σπέρνω', 'σπείρω', 'αίρω', 'δίδομαι', 'δίδω', 'στέλλομαι',
                          'στέκομαι',
                          'τρέπομαι', 'αίρομαι', 'καθιστώ', 'καθίσταμαι', 'υφίσταμαι', 'κρέμαμαι', 'ίπταμαι', 'προσαρτώ',
                          'βιώ', 'επιμελούμαι', 'απολογούμαι', 'πυροδοτούμαι', 'επείγει', 'υφαίνω']

    """ 
    special case for common verbs with modern "para" prefix, which can be confused with ancient "para" and cause
    augmentation mistakes. These should be inflected also with 'alternative' flag to give different results
    """
    dimotik_detachable = [
        'παραβλέπω', 'παραείμαι', 'παραβγαίνω', 'παρατρώω', 'παρατρώγω', 'παραμένω', 'παραλέω'
    ]

    """
    there is a problem with prefix para, which can mean different things and so a verb prefixed with it can mean
    either "too much", and "from above". In the first instance it is fully detachable and a verb is conjugated
    as if it was a root verb, in the second instance the perfective tense can be different and also augment is handled 
    differently. So I will add a flag 'para', so that if false it can be conjugated as a simple verb, if true, as
    a detachable verb
    """


    prefix = []


    """
        verbs that conditionally can be detached from their prefixes, mostly of logia descend
    """

    for pref in prefixes_before_augment:
        if pres_form.startswith(pref):
            without_prefix = remove_diaer(pres_form.replace(pref, ''))
            if without_prefix in archaic_detachable:
                prefix = [pref, prefixes_before_augment[pref]]

                pres_form = without_prefix

    if pres_form in para_detachable_only or (para and pres_form.startswith('παρα') and pres_form not in para_detachable_never):
        prefix = ['παρα', 'παρα']
        pres_form = pres_form[4:]

    elif not prefix:
        """
        these prefixes, lika ξανα can be safely detached
        """

        for pref in prefixes_detachable:
            if pres_form.startswith(pref):
                without_prefix = remove_diaer(pres_form.replace(pref, ''))
                num_syll = count_syllables(without_prefix, true_syllabification=False)
                if without_prefix.endswith('αι'):
                    num_syll -= 1
                if num_syll > 1 and without_prefix in greek_corpus:
                    prefix = [pref, prefixes_detachable[pref]]
                    pres_form = without_prefix

        """
            by weak I mean situation where very frequent verbs, mostly two syllables, 
            have their own inflection and cannot be detached or there is possibility of 
            internal augment
    
        """
        for pref in prefixes_detachable_weak:
            if pres_form.startswith(pref):
                without_prefix = remove_diaer(pres_form.replace(pref, ''))
                num_syll = count_syllables(without_prefix, true_syllabification=False)
                if without_prefix.endswith('αι'):
                    num_syll -= 1
                if (num_syll > 2 and without_prefix in greek_corpus) or pres_form in dimotik_detachable:
                    prefix = [pref, prefixes_detachable_weak[pref]]
                    pres_form = without_prefix

    verb_temp = {}

    # defaults
    # deponentia
    not_deponens = True
    deponens = False
    intransitive_active = False
    modal_act = False
    modal_med = False

    if 'μαι' == pres_form[-3:] and pres_form not in ['είμαι', 'παραείμαι']:

        deponens = True
        not_deponens = False

    elif pres_form[-2:] in ['ει', 'εί']:
        modal_act = True
        not_deponens = False
    elif pres_form[-3:] == 'ται':
        modal_med = True
        not_deponens = False

    modal = modal_act or modal_med

    # presens
    has_passive = False
    present_basic, pres_conjugation, root, intransitive_active = create_basic_present_forms(pres_form,
                                                                                            deponens=deponens,
                                                                                            not_deponens=not_deponens,
                                                                                            intransitive_active=intransitive_active,
                                                                                            modal_act=modal_act,
                                                                                            modal_med=modal_med)

    if pres_form[:-1] in irregular_passive_roots:
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
        has_passive = set(pres_pass)

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
                                                   not_deponens=not_deponens, modal_act=modal_act, modal_med=modal_med)

    aorist_active = []
    if aorist_basic_forms:
        verb_temp[AORIST] = {}
        aorist_active, aorist_passive = aorist_basic_forms.split('/')
        # some compoundse move accent or dont use augment
        aorist_active = aorist_active.split(',')

        aorist_passive = aorist_passive.split(',')
        if aorist_active and aorist_active[0]:
            verb_temp[AORIST][ACTIVE] = set(aorist_active)
        if aorist_passive and aorist_passive[0]:
            verb_temp[AORIST][PASSIVE] = set(aorist_passive)

    # paratatikos

    paratatikos_basic_forms = create_basic_paratatikos_forms(pres_form, root, pres_conjugation, deponens=deponens,
                                                             not_deponens=not_deponens, modal_act=modal_act,
                                                             modal_med=modal_med, has_passive=has_passive)
    paratatikos_active = []
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
        verb_temp[ACT_PRES_PARTICIPLE] = set(present_participle_active.split(','))

    # archaic praes part act

    present_participle_active_archaic = create_present_active_participle_arch(pres_form, root, pres_conjugation)

    if present_participle_active_archaic and not modal:
        verb_temp[ARCH_ACT_PRES_PARTICIPLE] = set(present_participle_active_archaic.split(','))

    # pres part pass

    present_participle_passive = create_present_passive_participle(pres_form, root, pres_conjugation)

    if present_participle_passive and not modal:
        verb_temp['pass_pres_participle'] = set(present_participle_passive.split(','))

    # passive_perfect_participles

    if (PASSIVE_PERFECT_PARTICIPLE in verb_temp and
            verb_temp[PASSIVE_PERFECT_PARTICIPLE][-2:] in ['άς', 'άν'] and not modal):
        # correcting improper categorization of part on an

        verb_temp[ACTIVE_AORIST_PARTICIPLE] = {act_root + 'άς/' + act_root + 'άσα/' + act_root + 'άν'}
        verb_temp[PASSIVE_PERFECT_PARTICIPLE] = {''}

    passive_perfect_participles = create_passive_perfect_participle(pres_form, root, act_root, passive_root)

    if passive_perfect_participles and not modal:
        verb_temp[PASSIVE_PERFECT_PARTICIPLE] = set(passive_perfect_participles.split(','))

    # active aorist participle

    if act_root and not modal:

        active_aorist_participle = create_active_aorist_participle(root, act_root)
        if active_aorist_participle:
            verb_temp[ACTIVE_AORIST_PARTICIPLE] = set(active_aorist_participle.split(','))

    # passive aorist participle
    if passive_root and not modal:

        participles = set()
        for p_root in passive_root.split(','):
            participle = create_passive_aorist_participle(p_root)
            if participle:
                participles.add(participle)

        # passive_aorist_participle = create_passive_aorist_participle(passive_root)
        if participles:
            verb_temp[PASSIVE_AORIST_PARTICIPLE] = participles

    verb_temp[MODAL] = modal_act or modal_med

    if prefix:

        verbs_temp_updated = update_forms_with_prefix(verb_temp, prefix)
        verb_temp = verbs_temp_updated
        """
        now we must deal with augment
        """
        try:
            # aorist
            aorist_active_cmp = verb_temp[AORIST][ACTIVE]
            alt_aorists = list(aorist_active_cmp)
            alt_aorists.extend([put_accent_on_the_antepenultimate(prefix[0] + deaugment_past_form(f, pres_form)) for f in aorist_active])
            alt_aorists.extend([put_accent_on_the_antepenultimate(f) for f in alt_aorists])

            alt_aorist_active = [f for f in alt_aorists if f in greek_corpus]
            if alt_aorist_active:
                verb_temp[AORIST][ACTIVE] = set(alt_aorist_active)
        except KeyError:
            pass
        try:
            # paratatikos
            paratatikos_active_cmp = verb_temp[PARATATIKOS][ACTIVE]
            alt_paratatikos = list(paratatikos_active_cmp)
            alt_paratatikos.extend([put_accent_on_the_antepenultimate(prefix[0] + deaugment_past_form(f, pres_form)) for f in paratatikos_active])

            alt_paratatikos_active = [f for f in alt_paratatikos if f in greek_corpus]
            if alt_paratatikos_active:
                verb_temp[PARATATIKOS][ACTIVE] = set(alt_paratatikos_active)

            subjunctive_active = verb_temp[CONJUNCTIVE][ACTIVE]
            moved_accent = [put_accent_on_the_penultimate(f) for f in subjunctive_active]

            alt_subjunctive_active = [f for f in moved_accent if f in greek_corpus]
            if alt_subjunctive_active:
                verb_temp[CONJUNCTIVE][ACTIVE] = set(alt_subjunctive_active)
        except KeyError:
            pass
        try:
            # participles
            participles = list(verb_temp[ARCH_ACT_PRES_PARTICIPLE])[0].split('/')
            if not where_is_accent(participles[0]):
                accented_participles = []
                for p in participles:
                    if not where_is_accent(p):
                        accented_participles.append(put_accent_on_the_ultimate(p))
                    else:
                        accented_participles.append(p)
                verb_temp[ARCH_ACT_PRES_PARTICIPLE] = {'/'.join(accented_participles)}
        except KeyError:
            pass

    if pres_form == 'όψομαι':
        del verb_temp[PARATATIKOS]

    return verb_temp
# create list of all verbs with their basic forms. Check them with existing forms and if they already exist,
# leave them out
