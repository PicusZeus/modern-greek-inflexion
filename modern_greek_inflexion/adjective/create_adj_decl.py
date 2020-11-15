

import copy
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_ultimate, \
    put_accent_on_the_penultimate, put_accent, count_syllables

from ..resources import greek_corpus, adj_basic_template

# adj = {'adj': 'ωμός/ωμή/ωμό', 'comparative': 'ωμότερος/ωμότατος', 'adverb': 'ωμά', 'adverb_comparative': 'ωμότερα/ωμότατα'}


def alternative_forms_kxth(fem):
    # κ, χ, θ ia, or h
    alt_forms = {'sg':{
                    'fem':{
                        'nom': '',
                        'gen': '',
                        'acc': '',
                        'voc': ''}
    }
    }
    if fem[-2] in ['κ', 'χ', 'θ']:
        alt_form = fem[:-1] + 'ια'
        if where_is_accent(fem) == 'ultimate':
            alt_form = put_accent_on_the_ultimate(alt_form)

        if alt_form in greek_corpus:
            alt_forms['sg']['fem']['nom'] = alt_form
            alt_forms['sg']['fem']['acc'] = alt_form
            alt_forms['sg']['fem']['gen'] = alt_form + 'ς'
            alt_forms['sg']['fem']['voc'] = alt_form

            return alt_forms

    return None

def alternative_forms_us(adj):
    # only for the us, ia, y type
    alt_forms = {'sg':{
                    'masc':{
                    },
                    'fem': {},
                    'neut':{
                    }
                    },
              'pl': {
                  'masc': {},
                  'fem': {},
                  'neut': {
                  }
              }}

    masc, fem, neut = adj.split('/')

    if masc:

        alt_forms['sg']['masc']['gen'] = masc[:-1]
        acc_sg = masc[:-1] + 'ν'
        if acc_sg in greek_corpus:
            alt_forms['sg']['masc']['acc'] = acc_sg
        gen_sg = masc[:-2] + 'έος'
        if gen_sg in greek_corpus:
            alt_forms['sg']['masc']['gen'] = masc[:-1] + ',' + gen_sg


    if neut:
        alt_forms['sg']['neut']['gen'] = neut
        gen_sg = masc[:-2] + 'έος'
        if gen_sg in greek_corpus:
            alt_forms['sg']['neut']['gen'] = neut + ',' + gen_sg

    if masc not in ['πολύς', 'μέγας'] and masc[:-2] + 'είς' in greek_corpus:
        alt_forms['pl']['masc']['nom'] = masc[:-2] + 'είς'
        alt_forms['pl']['masc']['acc'] = masc[:-2] + 'είς'
        alt_forms['pl']['masc']['gen'] = masc[:-2] + 'έων'
        alt_forms['pl']['masc']['voc'] = masc[:-2] + 'είς'
        alt_forms['pl']['neut']['nom'] = neut[:-1] + 'έα'
        alt_forms['pl']['neut']['acc'] = neut[:-1] + 'έα'
        alt_forms['pl']['neut']['voc'] = neut[:-1] + 'έα'
        alt_forms['pl']['neut']['gen'] = neut[:-1] + 'έων'

    if fem[:-2] + 'εία' in greek_corpus:
        fem_alt_stem = fem[:-2] + 'εία'
        fem_alt_plur = fem[:-2] + 'είες'
        alt_forms['sg']['fem']['nom'] = fem_alt_stem
        alt_forms['sg']['fem']['acc'] = fem_alt_stem + ',' + fem_alt_stem + 'ν'
        alt_forms['sg']['fem']['gen'] = fem_alt_stem + 'ς'
        alt_forms['sg']['fem']['voc'] = fem_alt_stem
        alt_forms['pl']['fem']['nom'] = fem_alt_plur
        alt_forms['pl']['fem']['acc'] = fem_alt_plur
        alt_forms['pl']['fem']['voc'] = fem_alt_plur
        alt_forms['pl']['fem']['gen'] = fem[:-2] + 'ειών'





    if masc in ['πολύς', 'μέγας']:
        alt_forms.pop('pl')
    # else there will be blank places, remember to check if there is sth
    # before inserting
    return alt_forms

def alternative_forms_us2(adj):
    # only for the us, ia, y type
    alt_forms = {'sg':{
                    'masc':{
                        'gen': '',
                    },
                    'neut':{
                        'gen': '',
                    }
                    }}

    masc, fem, neut = adj.split('/')

    if masc:

        alt_forms['sg']['masc']['gen'] = masc[:-2] + 'έος'
        alt_forms['sg']['neut']['gen'] = masc[:-2] + 'έος'

    return alt_forms


def alternative_forms_wn(adj):
    # wn, ousa on
    alt_forms = copy.deepcopy(adj_basic_template)

    masc, fem, neut = adj.split('/')

    if neut != '-':
        thema = neut + 'τ'
        alt_forms['sg']['masc']['acc'] = thema + 'α'
        alt_forms['sg']['masc']['gen'] = thema + 'ος'
        alt_forms['sg']['neut']['nom'] = neut
        alt_forms['sg']['neut']['gen'] = thema + 'ος'
        alt_forms['sg']['neut']['acc'] = neut
        alt_forms['sg']['neut']['voc'] = neut
        alt_forms['pl']['masc']['nom'] = thema + 'ες'
        alt_forms['pl']['masc']['acc'] = thema + 'ες'
        alt_forms['pl']['masc']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        alt_forms['pl']['masc']['voc'] = thema + 'ες'
        alt_forms['pl']['neut']['nom'] = thema + 'α'
        alt_forms['pl']['neut']['acc'] = thema + 'α'
        alt_forms['pl']['neut']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        alt_forms['pl']['neut']['voc'] = thema + 'α'
    if masc != '-':
        alt_forms['sg']['masc']['nom'] = masc
        alt_forms['sg']['masc']['voc'] = masc

    if fem != '-':
        alt_forms['sg']['fem']['nom'] = fem
        alt_forms['sg']['fem']['acc'] = fem
        alt_forms['sg']['fem']['gen'] = fem + 'ς'
        alt_forms['sg']['fem']['voc'] = fem
        alt_forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
        alt_forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
        alt_forms['pl']['fem']['gen'] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        alt_forms['pl']['fem']['voc'] = fem[:-1] + 'ες'

    return alt_forms


def alternative_forms_onas(adj):
    alt_forms = {'sg': {
        'masc': {
            'nom': '',
            'gen': '',
            'acc': '',
            'voc': ''
        },

    },
        'pl': {
            'masc': {
                'nom': '',
                'gen': '',
                'acc': '',
                'voc': ''},

        }}

    masc, fem, neut = adj.split('/')

    if neut:
        thema = neut
        alt_forms['sg']['masc']['acc'] = thema + 'α'
        alt_forms['sg']['masc']['gen'] = thema + 'ος'
        alt_forms['pl']['masc']['nom'] = thema + 'ες'
        alt_forms['pl']['masc']['acc'] = thema + 'ες'
        alt_forms['pl']['masc']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        alt_forms['pl']['masc']['voc'] = thema + 'ες'

    if fem:
        alt_forms['sg']['masc']['nom'] = fem
        alt_forms['sg']['masc']['voc'] = fem

    return alt_forms


def alternative_forms_ou(fem):
    """
    :param fem: its a feminine form with a ou ending
    :return:
    """
    alt_forms = {'sg': {
        'fem': {
            'nom': '',
            'gen': '',
            'acc': '',
            'voc': ''
        },

    },
        'pl': {
            'fem': {
                'nom': '',
                'gen': '',
                'acc': '',
                'voc': ''},

        }}

    alt_forms['sg']['fem']['nom'] = fem
    alt_forms['sg']['fem']['acc'] = fem
    alt_forms['sg']['fem']['gen'] = fem + 'ς'
    alt_forms['sg']['fem']['voc'] = fem


    alt_forms['pl']['fem']['nom'] = fem + 'δες'
    alt_forms['pl']['fem']['acc'] = fem + 'δες'
    alt_forms['pl']['fem']['gen'] = fem + 'δων'
    alt_forms['pl']['fem']['voc'] = fem + 'δες'

    return alt_forms


def put_accent_on_unaccented_forms(forms):
    if not forms:
        return forms

    for number in forms.keys():
        for gender in forms[number].keys():
            for case in forms[number][gender].keys():
                f = forms[number][gender][case]

                if not where_is_accent(f) and count_syllables(f) > 1:
                    forms[number][gender][case] = put_accent(f, 'penultimate')

    return forms


def create_all_adj_forms(adj):

    """
    :param adj: expects masc, fem and neut forms divided with / ('ωραίος/ωραία/ωραίο). If feminine doesnt exist, it should
    be replaced with dash '-'
    :return: two element array, first is a dictionary with all primary forms (forms[number][gender][case], the second
    one is a dictionary with alternative forms, if exists it has the same structure
    """
    forms = copy.deepcopy(adj_basic_template)

    # ωμός / ωμή / ωμό
    masc, fem, neut = adj.split('/')
    if masc[-2:] in ['ός', 'ος'] and fem[-1] in ['α', 'ά', 'η', 'ή', '-'] and neut[-1] in ['ο', 'ό']:
        fem = fem.split(',')[0] # because in the list there are given alternatives, which i dont need
        if fem == '-':
            # in my lists it sometimes happen, so this will be a solution
            fem = masc[:-2] + 'η'
            if fem [-2] in ['ι', 'ί']:
                fem = masc[:-2] + 'α'
        # os, h/a, o
        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = masc[:-1]
        forms['sg']['masc']['gen'] = masc[:-2] + 'ου'
        forms['sg']['masc']['voc'] = masc[:-2] + 'ε'

        forms['pl']['masc']['nom'] = masc[:-2] + 'οι'
        forms['pl']['masc']['acc'] = masc[:-2] + 'ους'
        forms['pl']['masc']['gen'] = masc[:-2] + 'ων'
        forms['pl']['masc']['voc'] = masc[:-2] + 'οι'

        if fem != '-':
            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = fem
            forms['sg']['fem']['gen'] = fem + 'ς'
            forms['sg']['fem']['voc'] = fem

            forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
            forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
            forms['pl']['fem']['gen'] = fem[:-1] + 'ων'
            forms['pl']['fem']['voc'] = fem[:-1] + 'ες'

        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = neut[:-1] + 'ου'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['neut']['nom'] = neut[:-1] + 'α'
        forms['pl']['neut']['acc'] = neut[:-1] + 'α'
        forms['pl']['neut']['gen'] = neut[:-1] + 'ων'
        forms['pl']['neut']['voc'] = neut[:-1] + 'α'

        accent = where_is_accent(masc)
        if accent == 'ultimate':
            for num in forms.keys():
                for gender in forms[num].keys():
                    for case, form in forms[num][gender].items():
                        forms[num][gender][case] = put_accent_on_the_ultimate(form)

        alt_forms = alternative_forms_kxth(fem)

        return forms, alt_forms



    elif (masc[-2:] in ['ύς', 'υς'] and where_is_accent(fem) == 'ultimate') or masc == 'μέγας':
        # add alternativeσ, bathys

        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = masc[:-1]

        forms['sg']['masc']['voc'] = masc[:-1]

        # if fem != '-':
        forms['sg']['masc']['gen'] = fem[:-1] + 'ου'
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = fem
        forms['sg']['fem']['gen'] = fem + 'ς'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['gen'] = fem[:-1] + 'ου'
        forms['pl']['masc']['nom'] = fem[:-1] + 'οι'
        forms['pl']['masc']['acc'] = fem[:-1] + 'ους'
        forms['pl']['masc']['gen'] = fem[:-1] + 'ων'
        forms['pl']['masc']['voc'] = fem[:-1] + 'οι'
        forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
        forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
        forms['pl']['fem']['gen'] = fem[:-1] + 'ων'
        forms['pl']['fem']['voc'] = fem[:-1] + 'ες'
        forms['pl']['neut']['nom'] = fem[:-1] + 'α'
        forms['pl']['neut']['acc'] = fem[:-1] + 'α'
        forms['pl']['neut']['gen'] = fem[:-1] + 'ων'
        forms['pl']['neut']['voc'] = fem[:-1] + 'α'


        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        if masc != 'μέγας':
            for num in forms.keys():
                for gender in forms[num].keys():
                    for case, form in forms[num][gender].items():
                        forms[num][gender][case] = put_accent_on_the_ultimate(form)

        alt_forms = alternative_forms_us(adj)

        return forms, alt_forms

    elif masc[-2:] in ['ύς', 'υς'] and where_is_accent(fem) == 'penultimate':
        # oksys, okseos

        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = masc[:-1]
        forms['sg']['masc']['gen'] = masc[:-1]
        forms['sg']['masc']['voc'] = masc[:-1]

        forms['pl']['masc']['nom'] = masc[:-2] + 'είς'
        forms['pl']['masc']['acc'] = masc[:-2] + 'είς'
        forms['pl']['masc']['gen'] = masc[:-2] + 'έων'
        forms['pl']['masc']['voc'] = masc[:-2] + 'είς'
        if fem != '-':
            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = fem
            forms['sg']['fem']['gen'] = fem + 'ς'
            forms['sg']['fem']['voc'] = fem
            forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
            forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
            forms['pl']['fem']['gen'] = fem[:-2] + 'ιών'
            forms['pl']['fem']['voc'] = fem[:-1] + 'ες'

        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = neut
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['neut']['nom'] = masc[:-2] + 'έα'
        forms['pl']['neut']['acc'] = masc[:-2] + 'έα'
        forms['pl']['neut']['gen'] = masc[:-2] + 'έων'
        forms['pl']['neut']['voc'] = masc[:-2] + 'έα'

        alt_forms = alternative_forms_us2(adj)

        return forms, alt_forms


    elif masc[-2:] in ['ης', 'άς', 'ής'] and fem[-1] in ['α', 'ύ'] and neut[-3:] == 'ικο':
        #hs, a, iko
        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = masc[:-1]
        forms['sg']['masc']['gen'] = masc[:-1]
        forms['sg']['masc']['voc'] = masc[:-1]
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = fem
        forms['sg']['fem']['gen'] = fem + 'ς'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = neut[:-1] + 'ου'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['masc']['nom'] = masc[:-1] + 'δες'
        forms['pl']['masc']['acc'] = masc[:-1] + 'δες'
        forms['pl']['masc']['gen'] = masc[:-1] + 'δων'
        forms['pl']['masc']['voc'] = masc[:-2] + 'δες'
        if fem[-2:] == 'ού':
            forms['pl']['fem']['nom'] = fem + 'δες'
            forms['pl']['fem']['acc'] = fem + 'δες'
            forms['pl']['fem']['gen'] = fem + 'δων'
            forms['pl']['fem']['voc'] = fem + 'δες'
        else:
            forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
            forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
            forms['pl']['fem']['gen'] = fem[:-2] + 'ων'
            forms['pl']['fem']['voc'] = fem[:-1] + 'ες'
        forms['pl']['neut']['nom'] = neut[:-1] + 'α'
        forms['pl']['neut']['acc'] = neut[:-1] + 'α'
        forms['pl']['neut']['gen'] = neut[:-1] + 'ων'
        forms['pl']['neut']['voc'] = neut[:-1] + 'α'

        alternative_forms = None
        # προσθεσε εναλλακτικές μορφές για το θυληκό γενος ξανθομάλλα και ξανθομαλλού
        if fem[-1] == 'α':
            alt_fem = put_accent_on_the_ultimate(fem[:-1] + 'ου')
            if alt_fem in greek_corpus:
                alternative_forms = alternative_forms_ou(alt_fem)

        return forms, alternative_forms

    elif masc[-2:] == 'ής' and fem[-1] == 'ά' and neut[-1] == 'ί':
        #colors hs, a, i
        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = masc[:-1]
        forms['sg']['masc']['gen'] = masc[:-1]
        forms['sg']['masc']['voc'] = masc[:-1]
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = fem
        forms['sg']['fem']['gen'] = fem + 'ς'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = fem[:-1] + 'ού'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut
        forms['pl']['masc']['nom'] = fem[:-1] + 'οί'
        forms['pl']['masc']['acc'] = fem[:-1] + 'ούς'
        forms['pl']['masc']['gen'] = fem[:-1] + 'ών'
        forms['pl']['masc']['voc'] = fem[:-1] + 'οί'
        forms['pl']['fem']['nom'] = fem[:-1] + 'ές'
        forms['pl']['fem']['acc'] = fem[:-1] + 'ές'
        forms['pl']['fem']['gen'] = fem[:-1] + 'ών'
        forms['pl']['fem']['voc'] = fem[:-1] + 'ές'
        forms['pl']['neut']['nom'] = fem[:-1] + 'ά'
        forms['pl']['neut']['acc'] = fem[:-1] + 'ά'
        forms['pl']['neut']['gen'] = fem[:-1] + 'ών'
        forms['pl']['neut']['voc'] = fem[:-1] + 'ά'

        return forms, None

    elif masc[-2:] == 'ώς' and fem[-1] == 'α' and neut[-1] == 'ς':
        #archaic participles, not sure which endings to choose, as it seems both are used, ancient and modern (especially in fem),
        # for now I will settle with modernized
        thema = masc[:-1] + 'τ'
        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = thema + 'α'
        forms['sg']['masc']['gen'] = thema + 'ος'
        forms['sg']['masc']['voc'] = masc
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = fem
        forms['sg']['fem']['gen'] = fem + 'ς'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = thema + 'ος'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut
        forms['pl']['masc']['nom'] = thema + 'ες'
        forms['pl']['masc']['acc'] = thema + 'ες'
        forms['pl']['masc']['gen'] = thema + 'ων'
        forms['pl']['masc']['voc'] = thema + 'ες'
        forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
        forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
        forms['pl']['fem']['gen'] = fem[:-1] + 'ων'
        forms['pl']['fem']['voc'] = fem[:-1] + 'ες'
        forms['pl']['neut']['nom'] = thema + 'α'
        forms['pl']['neut']['acc'] = thema + 'α'
        forms['pl']['neut']['gen'] = thema + 'ων'
        forms['pl']['neut']['voc'] = thema + 'α'

        return forms, None
    elif masc[-2:] in ['ης', 'ής'] and fem[-2:] in ['ής', 'ης'] and neut[-2:] in ['ες', 'ές']:
        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['gen'] = masc[:-2] + 'ους'
        forms['sg']['masc']['acc'] = masc[:-1]
        forms['sg']['masc']['voc'] = masc[:-1]
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['gen'] = fem[:-2] + 'ους'
        forms['sg']['fem']['acc'] = fem[:-1]
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = fem[:-2] + 'ους'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['masc']['nom'] = masc[:-2] + 'εις'
        forms['pl']['masc']['acc'] = masc[:-2] + 'εις'
        forms['pl']['masc']['gen'] = masc[:-2] + 'ων'
        forms['pl']['masc']['voc'] = masc[:-2] + 'εις'
        forms['pl']['fem']['nom'] = masc[:-2] + 'εις'
        forms['pl']['fem']['acc'] = masc[:-2] + 'εις'
        forms['pl']['fem']['gen'] = masc[:-2] + 'ων'
        forms['pl']['fem']['voc'] = masc[:-2] + 'εις'
        forms['pl']['neut']['nom'] = masc[:-2] + 'η'
        forms['pl']['neut']['acc'] = masc[:-2] + 'η'
        forms['pl']['neut']['gen'] = masc[:-2] + 'ων'
        forms['pl']['neut']['voc'] = masc[:-2] + 'η'

        if where_is_accent(masc) == 'ultimate':
            for num in forms.keys():
                for gender in forms[num].keys():
                    for case, form in forms[num][gender].items():
                        forms[num][gender][case] = put_accent_on_the_ultimate(form)

        return forms, None

    elif masc[-2:] in ['ων', 'ών', 'ας'] and fem[-2:] in ['σα'] and neut[-2:] in ['ον', 'όν', 'ύν', 'ών', 'ων', 'αν']:
        # wn, ousa, on and as, asa, an
        feminins = fem.split(',')
        fem = feminins[0]
        neuters = neut.split(',')
        neut = neuters[0]
        thema = neut + 'τ'

        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = thema + 'α'
        forms['sg']['masc']['gen'] = thema + 'ος'
        forms['sg']['masc']['voc'] = masc
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = fem
        forms['sg']['fem']['gen'] = fem + 'ς'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = thema + 'ος'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut
        forms['pl']['masc']['nom'] = thema + 'ες'
        forms['pl']['masc']['acc'] = thema + 'ες'
        forms['pl']['masc']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['masc']['voc'] = thema + 'ες'
        forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
        forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
        forms['pl']['fem']['gen'] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms['pl']['fem']['voc'] = fem[:-1] + 'ες'
        forms['pl']['neut']['nom'] = thema + 'α'
        forms['pl']['neut']['acc'] = thema + 'α'
        forms['pl']['neut']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['neut']['voc'] = thema + 'α'

        alternative_forms = None

        if len(neuters) > 1 and len(feminins) > 1:

            alternative_forms = alternative_forms_wn(f'{masc}/{feminins[1]}/{neuters[1]}')

        elif len(neuters) > 1:
            alternative_forms = alternative_forms_wn(f'{masc}/{feminins[0]}/{neuters[1]}')

        elif len(feminins) > 1:
            alternative_forms = alternative_forms_wn(f'{masc}/{feminins[1]}/{neuters[0]}')

        forms = put_accent_on_unaccented_forms(forms)
        alternative_forms = put_accent_on_unaccented_forms(alternative_forms)

        return forms, alternative_forms

        
    elif (masc[-4:] == 'ονας' or masc[-2:] in ['ών','ων']) and fem[-2:] == 'ων' and neut[-2:] == 'ον':

        # ονας, ων, ον
        thema = neut

        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = thema + 'α'
        forms['sg']['masc']['gen'] = thema + 'α'
        forms['sg']['masc']['voc'] = thema + 'α'
        if masc[-2:] in ['ών', 'ων']:
            forms['sg']['masc']['voc'] = masc
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = thema + 'α'
        forms['sg']['fem']['gen'] = thema + 'ος'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = thema + 'ος'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['masc']['nom'] = thema + 'ες'
        forms['pl']['masc']['acc'] = thema + 'ες'
        forms['pl']['masc']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['masc']['voc'] = thema + 'ες'
        forms['pl']['fem']['nom'] = thema + 'ες'
        forms['pl']['fem']['acc'] = thema + 'ες'
        forms['pl']['fem']['gen'] = put_accent_on_the_ultimate(thema + 'ων')
        forms['pl']['fem']['voc'] = thema + 'ες'
        forms['pl']['neut']['nom'] = thema + 'α'
        forms['pl']['neut']['acc'] = thema + 'α'
        forms['pl']['neut']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['neut']['voc'] = thema + 'α'

        alternative_forms = alternative_forms_onas(adj)

        return forms, alternative_forms

    elif masc[-3:] in ['είς'] and fem[-2:] in ['σα'] and neut[-2:] in ['έν']:
        # participles

        thema = neut + 'τ'

        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = thema + 'α'
        forms['sg']['masc']['gen'] = thema + 'ος'
        forms['sg']['masc']['voc'] = masc
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = fem
        forms['sg']['fem']['gen'] = fem + 'ς'
        forms['sg']['fem']['voc'] = fem
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = thema + 'ος'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['masc']['nom'] = thema + 'ες'
        forms['pl']['masc']['acc'] = thema + 'ες'
        forms['pl']['masc']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['masc']['voc'] = thema + 'ες'
        forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
        forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
        forms['pl']['fem']['gen'] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms['pl']['fem']['voc'] = fem[:-1] + 'ες'
        forms['pl']['neut']['nom'] = thema + 'α'
        forms['pl']['neut']['acc'] = thema + 'α'
        forms['pl']['neut']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['neut']['voc'] = thema + 'α'

        alternative_forms = None

        return forms, alternative_forms

    elif masc in ['άρρην'] or (masc[-2:] == 'ων' and neut[-2:] == 'ον'):
        # ancient 3rd declesion

        thema = neut

        forms['sg']['masc']['nom'] = masc
        forms['sg']['masc']['acc'] = thema + 'α'
        forms['sg']['masc']['gen'] = thema + 'ος'
        forms['sg']['masc']['voc'] = neut
        forms['sg']['fem']['nom'] = fem
        forms['sg']['fem']['acc'] = thema + 'α'
        forms['sg']['fem']['gen'] = thema + 'ος'
        forms['sg']['fem']['voc'] = neut
        forms['sg']['neut']['nom'] = neut
        forms['sg']['neut']['gen'] = thema + 'ος'
        forms['sg']['neut']['acc'] = neut
        forms['sg']['neut']['voc'] = neut

        forms['pl']['masc']['nom'] = thema + 'ες'
        forms['pl']['masc']['acc'] = thema + 'ες'
        forms['pl']['masc']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['masc']['voc'] = thema + 'ες'
        forms['pl']['fem']['nom'] = thema + 'ες'
        forms['pl']['fem']['acc'] = thema + 'ες'
        forms['pl']['fem']['gen'] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms['pl']['fem']['voc'] = thema + 'ες'
        forms['pl']['neut']['nom'] = thema + 'α'
        forms['pl']['neut']['acc'] = thema + 'α'
        forms['pl']['neut']['gen'] = put_accent_on_the_penultimate(thema + 'ων')
        forms['pl']['neut']['voc'] = thema + 'α'

        return forms, None

    else:
        for number in forms.keys():
            for gender in forms[number].keys():
                for case in forms[number][gender].keys():
                    forms[number][gender][case] = masc

        return forms, None


def comparative_forms(comp_or_super):
    """
    :param comp_or_super: one form ending in os
    :return: all forms in a dict
    """

    if comp_or_super[-2:] in ['ών', 'ων']:
        accent = where_is_accent(comp_or_super)
        neuter = put_accent(comp_or_super[:-2] + 'ον', accent)
        comp_forms, _ = create_all_adj_forms(f'{comp_or_super}/{comp_or_super}/{neuter}')
    else:
        comp_forms, _ = create_all_adj_forms(f'{comp_or_super}/{comp_or_super[:-2]}η/{comp_or_super[:-1]}')

    return comp_forms



