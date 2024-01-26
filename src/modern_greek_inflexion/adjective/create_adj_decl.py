from __future__ import annotations

import copy
from typing import Any

from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_ultimate, \
    put_accent_on_the_penultimate, put_accent, count_syllables, put_accent_on_the_antepenultimate
from modern_greek_accentuation.resources import vowels
from ..resources.resources import greek_corpus
from ..resources.adj import adj_basic_template
from ..resources.variables import SG, PL, FEM, MASC, NEUT, NOM, GEN, ACC, VOC, ANTEPENULTIMATE, ULTIMATE, PENULTIMATE

"""
example
adj = {'adj': 'ωμός/ωμή/ωμό', 'comparative': 'ωμότερος/ωμότατος', 'adverb': 'ωμά',
'adverb_comparative': 'ωμότερα/ωμότατα'}
"""


def put_accent_in_all_forms(forms: dict, accent: str) -> dict:
    for num in forms.keys():
        for gender in forms[num].keys():
            for case, form in forms[num][gender].items():
                forms[num][gender][case] = put_accent(form, accent_name=accent, true_syllabification=True)
    return forms


def alternative_forms_r(fem: str, accent: str) -> dict:
    alt_forms = {SG: {
        FEM: {}
    }}
    if put_accent(fem[:-1] + 'ας', accent) in greek_corpus:
        alt_form = put_accent(fem[:-1] + 'α', accent)
        alt_forms[SG][FEM][NOM] = alt_form
        alt_forms[SG][FEM][ACC] = alt_form
        alt_forms[SG][FEM][GEN] = alt_form + 'ς'
        alt_forms[SG][FEM][VOC] = alt_form

    return alt_forms


def alternative_forms_ios(adj: str):
    masc, fem, neut = adj.split('/')
    alt_forms = {SG: {
        FEM: {}, MASC: {}, NEUT: {}
    }, PL: {
        FEM: {}, MASC: {}, NEUT: {}
    }
    }
    masc_gen = put_accent_on_the_penultimate(neut + 'υ', true_syllabification=False)
    masc_gen_pl = put_accent_on_the_penultimate(neut[:-1] + 'ων', true_syllabification=False)
    masc_acc_pl = put_accent_on_the_penultimate(neut[:-1] + 'ους', true_syllabification=False)
    fem_nom = put_accent_on_the_penultimate(fem, true_syllabification=False)
    fem_gen = put_accent_on_the_penultimate(fem + 'ς', true_syllabification=False)
    if masc_gen in greek_corpus:
        alt_forms[SG][MASC][GEN] = masc_gen
        alt_forms[SG][NEUT][GEN] = masc_gen
        alt_forms[PL][MASC][GEN] = masc_gen_pl
        alt_forms[PL][NEUT][GEN] = masc_gen_pl
        alt_forms[PL][FEM][GEN] = masc_gen_pl
        alt_forms[PL][MASC][ACC] = masc_acc_pl

    if fem_nom in greek_corpus:
        alt_forms[SG][FEM][NOM] = fem_nom
        alt_forms[SG][FEM][GEN] = fem_gen
        if fem_nom + 'ν' not in greek_corpus:
            alt_forms[SG][FEM][ACC] = fem_nom
        alt_forms[SG][FEM][VOC] = fem_nom

    return alt_forms


def alternative_fem_os(fem_os: str, accent: str) -> dict:
    alt_forms = {SG: {FEM: {}}, PL: {FEM: {}}}
    alt_forms[SG][FEM][NOM] = fem_os
    alt_forms[SG][FEM][ACC] = fem_os[:-1]
    alt_forms[SG][FEM][GEN] = fem_os[:-2] + 'ου'
    alt_forms[SG][FEM][VOC] = fem_os[:-2] + 'ε'

    alt_forms[PL][FEM][NOM] = fem_os[:-2] + 'οι'
    alt_forms[PL][FEM][ACC] = fem_os[:-2] + 'ους'
    alt_forms[PL][FEM][GEN] = fem_os[:-2] + 'ων'
    alt_forms[PL][FEM][VOC] = fem_os[:-2] + 'οι'

    return put_accent_in_all_forms(alt_forms, accent)


def alternative_forms_kxth(fem: str, accent: str) -> dict | None:
    # κ, χ, θ ia, or h
    alt_forms = {SG: {
        FEM: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''}
    }
    }

    alt_form = fem[:-1] + 'ια'

    if accent == ULTIMATE:
        alt_form = put_accent_on_the_ultimate(alt_form, true_syllabification=False)

    if alt_form in greek_corpus:
        alt_forms[SG][FEM][NOM] = alt_form
        alt_forms[SG][FEM][ACC] = alt_form
        alt_forms[SG][FEM][GEN] = alt_form + 'ς'
        alt_forms[SG][FEM][VOC] = alt_form

        return alt_forms

    return None


def alternative_forms_modern_3rd(adj):
    alt_forms = {SG: {
        MASC: {
        },
        FEM: {},
        NEUT: {
        }
    },
        PL: {
            MASC: {},
            FEM: {},
            NEUT: {
            }
        }}
    masc, fem, neut = adj.split('/')

    thema = neut + 'τ'
    if thema + 'ας' in greek_corpus:
        alt_forms[SG][MASC][NOM] = thema + 'ας'
        alt_forms[SG][MASC][GEN] = thema + 'α'
        alt_forms[SG][MASC][VOC] = thema + 'α'
    if fem[:-1] + 'ης' in greek_corpus:
        alt_forms[SG][FEM][GEN] = fem[:-1] + 'ης'

    return alt_forms


def alternative_forms_us(adj: str) -> dict:
    # only for the us, ia, y type
    alt_forms = {SG: {
        MASC: {
        },
        FEM: {},
        NEUT: {
        }
    },
        PL: {
            MASC: {},
            FEM: {},
            NEUT: {
            }
        }}

    masc, fem, neut = adj.split('/')

    if masc:

        alt_forms[SG][MASC][GEN] = masc[:-1]
        acc_sg = masc[:-1] + 'ν'
        if acc_sg in greek_corpus:
            alt_forms[SG][MASC][ACC] = acc_sg
        gen_sg = masc[:-2] + 'έος'
        if gen_sg in greek_corpus:
            alt_forms[SG][MASC][GEN] = masc[:-1] + ',' + gen_sg

    if neut:
        alt_forms[SG][NEUT][GEN] = neut
        gen_sg = masc[:-2] + 'έος'
        if gen_sg in greek_corpus:
            alt_forms[SG][NEUT][GEN] = neut + ',' + gen_sg

    if masc not in ['πολύς', 'μέγας'] and masc[:-2] + 'είς' in greek_corpus:
        alt_forms[PL][MASC][NOM] = masc[:-2] + 'είς'
        alt_forms[PL][MASC][ACC] = masc[:-2] + 'είς'
        alt_forms[PL][MASC][GEN] = masc[:-2] + 'έων'
        alt_forms[PL][MASC][VOC] = masc[:-2] + 'είς'
        alt_forms[PL][NEUT][NOM] = neut[:-1] + 'έα'
        alt_forms[PL][NEUT][ACC] = neut[:-1] + 'έα'
        alt_forms[PL][NEUT][VOC] = neut[:-1] + 'έα'
        alt_forms[PL][NEUT][GEN] = neut[:-1] + 'έων'

    if fem[:-2] + 'εία' in greek_corpus:
        fem_alt_stem = fem[:-2] + 'εία'
        fem_alt_plur = fem[:-2] + 'είες'
        alt_forms[SG][FEM][NOM] = fem_alt_stem
        alt_forms[SG][FEM][ACC] = fem_alt_stem + ',' + fem_alt_stem + 'ν'
        alt_forms[SG][FEM][GEN] = fem_alt_stem + 'ς'
        alt_forms[SG][FEM][VOC] = fem_alt_stem
        alt_forms[PL][FEM][NOM] = fem_alt_plur
        alt_forms[PL][FEM][ACC] = fem_alt_plur
        alt_forms[PL][FEM][VOC] = fem_alt_plur
        alt_forms[PL][FEM][GEN] = fem[:-2] + 'ειών'

    if masc in ['πολύς', 'μέγας']:
        alt_forms.pop(PL)
    # else there will be blank places, remember to check if there is sth
    # before inserting
    return alt_forms


def alternative_forms_us2(adj: str) -> dict:
    # only for the us, ia, y type
    alt_forms = {SG: {
        MASC: {
            GEN: '',
        },
        NEUT: {
            GEN: '',
        }
    }}

    masc, fem, neut = adj.split('/')

    if masc:
        alt_forms[SG][MASC][GEN] = masc[:-2] + 'έος'
        alt_forms[SG][NEUT][GEN] = masc[:-2] + 'έος'

    return alt_forms


def alternative_forms_wn(adj: str) -> dict:
    # wn, ousa on
    alt_forms = copy.deepcopy(adj_basic_template)

    masc, fem, neut = adj.split('/')

    if neut != '-':
        thema = neut + 'τ'
        alt_forms[SG][MASC][ACC] = thema + 'α'
        alt_forms[SG][MASC][GEN] = thema + 'ος'
        alt_forms[SG][NEUT][NOM] = neut
        alt_forms[SG][NEUT][GEN] = thema + 'ος'
        alt_forms[SG][NEUT][ACC] = neut
        alt_forms[SG][NEUT][VOC] = neut
        alt_forms[PL][MASC][NOM] = thema + 'ες'
        alt_forms[PL][MASC][ACC] = thema + 'ες'
        alt_forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        alt_forms[PL][MASC][VOC] = thema + 'ες'
        alt_forms[PL][NEUT][NOM] = thema + 'α'
        alt_forms[PL][NEUT][ACC] = thema + 'α'
        alt_forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        alt_forms[PL][NEUT][VOC] = thema + 'α'
    if masc != '-':
        alt_forms[SG][MASC][NOM] = masc
        alt_forms[SG][MASC][VOC] = masc

    if fem != '-':
        alt_forms[SG][FEM][NOM] = fem
        alt_forms[SG][FEM][ACC] = fem
        alt_forms[SG][FEM][GEN] = fem + 'ς'
        alt_forms[SG][FEM][VOC] = fem
        alt_forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        alt_forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        alt_forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        alt_forms[PL][FEM][VOC] = fem[:-1] + 'ες'

    return alt_forms


def alternative_forms_tis(adj, thema):
    alt_forms = {SG: {
        MASC: {

        },

    },
        PL: {
            MASC: {
                GEN: '',
            },
            FEM: {
                GEN: '',
            },
            NEUT: {
                GEN: '',
            }

        }}

    masc, fem, neut = adj.split('/')
    if neut + 'ν' in greek_corpus:
        alt_forms[SG][MASC][ACC] = neut + 'ν'
    gen_pl = put_accent_on_the_penultimate(thema + 'ων')

    alt_forms[PL][MASC][GEN] = gen_pl
    alt_forms[PL][FEM][GEN] = gen_pl
    alt_forms[PL][NEUT][GEN] = gen_pl

    return alt_forms


def alternative_forms_onas(adj: str) -> dict:
    alt_forms = {SG: {
        MASC: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''
        },

    },
        PL: {
            MASC: {
                NOM: '',
                GEN: '',
                ACC: '',
                VOC: ''},

        }}

    masc, fem, neut = adj.split('/')

    if neut:
        thema = neut
        alt_forms[SG][MASC][ACC] = thema + 'α'
        alt_forms[SG][MASC][GEN] = thema + 'ος'
        alt_forms[PL][MASC][NOM] = thema + 'ες'
        alt_forms[PL][MASC][ACC] = thema + 'ες'
        alt_forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        alt_forms[PL][MASC][VOC] = thema + 'ες'

    if fem:
        alt_forms[SG][MASC][NOM] = fem
        alt_forms[SG][MASC][VOC] = fem

    return alt_forms


def alternative_forms_ou(fem: str) -> dict:
    """
    :param fem: its a feminine form with a ou ending
    :return:
    """
    alt_forms = {SG: {
        FEM: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''
        },

    },
        PL: {
            FEM: {
                NOM: '',
                GEN: '',
                ACC: '',
                VOC: ''},

        }}

    alt_forms[SG][FEM][NOM] = fem
    alt_forms[SG][FEM][ACC] = fem
    alt_forms[SG][FEM][GEN] = fem + 'ς'
    alt_forms[SG][FEM][VOC] = fem

    alt_forms[PL][FEM][NOM] = fem + 'δες'
    alt_forms[PL][FEM][ACC] = fem + 'δες'
    alt_forms[PL][FEM][GEN] = fem + 'δων'
    alt_forms[PL][FEM][VOC] = fem + 'δες'

    return alt_forms


def put_accent_on_unaccented_forms(forms: dict) -> dict:
    if not forms:
        return forms

    for number in forms.keys():
        for gender in forms[number].keys():
            for case in forms[number][gender].keys():
                f = forms[number][gender][case]

                if not where_is_accent(f) and count_syllables(f) > 1:
                    forms[number][gender][case] = put_accent(f, PENULTIMATE)

    return forms


def create_all_adj_forms(adj: str) -> tuple[dict, dict | None]:
    """
    :param adj: expects masc, fem and neut forms divided with / ('ωραίος/ωραία/ωραίο). If feminine doesn't exist, it
     should be replaced with dash '-'
    :return: two element tuple, first is a dictionary with all primary forms (forms[number][gender][case], the second
    one is a dictionary with alternative forms, if exists it has the same structure
    """
    forms = copy.deepcopy(adj_basic_template)
    fem_alt = None
    # ωμός / ωμή / ωμό
    masc, fem, neut = adj.split('/')
    if ',' in fem:
        [fem, fem_alt] = fem.split(',')
    accent = where_is_accent(masc)

    if masc[-2:] in ['ός', 'ος'] and fem[-1] in ['α', 'ά', 'η', 'ή', '-'] and neut[-1] in ['ο', 'ό']:

        # os, h/a, o
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][GEN] = masc[:-2] + 'ου'
        forms[SG][MASC][VOC] = masc[:-2] + 'ε'

        forms[PL][MASC][NOM] = masc[:-2] + 'οι'
        forms[PL][MASC][ACC] = masc[:-2] + 'ους'
        forms[PL][MASC][GEN] = masc[:-2] + 'ων'
        forms[PL][MASC][VOC] = masc[:-2] + 'οι'

        if fem != '-':
            forms[SG][FEM][NOM] = fem
            forms[SG][FEM][ACC] = fem
            forms[SG][FEM][GEN] = fem + 'ς'
            forms[SG][FEM][VOC] = fem

            forms[PL][FEM][NOM] = fem[:-1] + 'ες'
            forms[PL][FEM][ACC] = fem[:-1] + 'ες'
            forms[PL][FEM][GEN] = fem[:-1] + 'ων'
            forms[PL][FEM][VOC] = fem[:-1] + 'ες'

        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = neut[:-1] + 'ου'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][NEUT][NOM] = neut[:-1] + 'α'
        forms[PL][NEUT][ACC] = neut[:-1] + 'α'
        forms[PL][NEUT][GEN] = neut[:-1] + 'ων'
        forms[PL][NEUT][VOC] = neut[:-1] + 'α'

        if accent == ULTIMATE:
            for num in forms.keys():
                for gender in forms[num].keys():
                    for case, form in forms[num][gender].items():
                        forms[num][gender][case] = put_accent(form, ULTIMATE, true_syllabification=True)
        alt_forms = None

        if fem_alt and fem_alt.endswith('ς'):
            # if masc == ''
            # fem -os
            alt_forms = alternative_fem_os(fem_alt, accent)

        elif fem[-2] in ['θ', 'κ', 'χ']:
            alt_forms = alternative_forms_kxth(fem, accent)
        elif fem[-2] in ['ρ', 'ν'] or (fem[-2] in vowels and fem[-1] == 'η'):
            alt_forms = alternative_forms_r(fem, accent)
        elif (fem[-2] == 'ι' and accent in [PENULTIMATE, ANTEPENULTIMATE]) or fem.endswith('μενη') or fem.endswith('στη'):
            alt_forms = alternative_forms_ios(adj)
        return forms, alt_forms

    elif masc[-2:] in ['ος', 'ός'] and masc == fem:
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][GEN] = masc[:-2] + 'ου'
        forms[SG][MASC][VOC] = masc[:-2] + 'ε'

        forms[PL][MASC][NOM] = masc[:-2] + 'οι'
        forms[PL][MASC][ACC] = masc[:-2] + 'ους'
        forms[PL][MASC][GEN] = masc[:-2] + 'ων'
        forms[PL][MASC][VOC] = masc[:-2] + 'οι'

        forms[SG][FEM][NOM] = masc
        forms[SG][FEM][ACC] = masc[:-1]
        forms[SG][FEM][GEN] = masc[:-2] + 'ου'
        forms[SG][FEM][VOC] = masc[:-2] + 'ε'

        forms[PL][FEM][NOM] = masc[:-2] + 'οι'
        forms[PL][FEM][ACC] = masc[:-2] + 'ους'
        forms[PL][FEM][GEN] = masc[:-2] + 'ων'
        forms[PL][FEM][VOC] = masc[:-2] + 'οι'

        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = neut[:-1] + 'ου'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][NEUT][NOM] = neut[:-1] + 'α'
        forms[PL][NEUT][ACC] = neut[:-1] + 'α'
        forms[PL][NEUT][GEN] = neut[:-1] + 'ων'
        forms[PL][NEUT][VOC] = neut[:-1] + 'α'

        if accent == ULTIMATE:
            for num in forms.keys():
                for gender in forms[num].keys():
                    for case, form in forms[num][gender].items():
                        forms[num][gender][case] = put_accent_on_the_ultimate(form)

        return forms, None

    elif masc[-3:] == 'ους' and neut[-3:] == 'ουν':
        if masc[-4] == 'π':
            thema = masc[:-3] + 'οδ'
            gen_sg = thema + 'ος'
            masc_fem_acc = thema + 'α'
            masc_fem_pl = thema + 'ες'
            gen_pl = put_accent_on_the_penultimate(thema + 'ων')

            forms[SG][MASC][NOM] = masc
            forms[SG][MASC][ACC] = masc_fem_acc
            forms[SG][MASC][GEN] = gen_sg
            forms[SG][MASC][VOC] = masc
            forms[SG][FEM][NOM] = masc
            forms[SG][FEM][ACC] = masc_fem_acc
            forms[SG][FEM][GEN] = gen_sg
            forms[SG][FEM][VOC] = masc
            forms[SG][NEUT][NOM] = neut
            forms[SG][NEUT][GEN] = gen_sg
            forms[SG][NEUT][ACC] = neut
            forms[SG][NEUT][VOC] = neut
            forms[PL][MASC][NOM] = masc_fem_pl
            forms[PL][MASC][ACC] = masc_fem_pl
            forms[PL][MASC][GEN] = gen_pl
            forms[PL][MASC][VOC] = masc_fem_pl
            forms[PL][FEM][NOM] = masc_fem_pl
            forms[PL][FEM][ACC] = masc_fem_pl
            forms[PL][FEM][GEN] = gen_pl
            forms[PL][FEM][VOC] = masc_fem_pl
            forms[PL][NEUT][NOM] = masc_fem_acc
            forms[PL][NEUT][ACC] = masc_fem_acc
            forms[PL][NEUT][GEN] = gen_pl
            forms[PL][NEUT][VOC] = masc_fem_acc



        else:
            pl_fem_masc = masc[:-3] + 'οες'
            pl_gen = put_accent_on_the_penultimate(masc[:-2] + 'ων')
            forms[SG][MASC][NOM] = masc
            forms[SG][MASC][ACC] = masc[:-1]
            forms[SG][MASC][GEN] = masc[:-1]
            forms[SG][MASC][VOC] = masc
            forms[SG][FEM][NOM] = masc
            forms[SG][FEM][ACC] = masc[:-1]
            forms[SG][FEM][GEN] = masc[:-1]
            forms[SG][FEM][VOC] = masc
            forms[SG][NEUT][NOM] = neut
            forms[SG][NEUT][GEN] = neut[:-1]
            forms[SG][NEUT][ACC] = neut
            forms[SG][NEUT][VOC] = neut
            forms[PL][MASC][NOM] = pl_fem_masc
            forms[PL][MASC][ACC] = pl_fem_masc
            forms[PL][MASC][GEN] = pl_gen
            forms[PL][MASC][VOC] = pl_fem_masc
            forms[PL][FEM][NOM] = pl_fem_masc
            forms[PL][FEM][ACC] = pl_fem_masc
            forms[PL][FEM][GEN] = pl_gen
            forms[PL][FEM][VOC] = pl_fem_masc
            forms[PL][NEUT][NOM] = masc[:-3] + 'οα'
            forms[PL][NEUT][ACC] = masc[:-3] + 'οα'
            forms[PL][NEUT][GEN] = pl_gen
            forms[PL][NEUT][VOC] = masc[:-3] + 'οα'

        return forms, None

    elif (masc[-2:] in ['ύς', 'υς'] and where_is_accent(fem) == ULTIMATE) or masc == 'μέγας':
        # add alternativeσ, bathys

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]

        forms[SG][MASC][VOC] = masc[:-1]
        if masc[-3:] in ['ους', 'ούς']:
            forms[SG][MASC][VOC] = masc
        forms[SG][MASC][GEN] = fem[:-1] + 'ου'
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][GEN] = fem[:-1] + 'ου'
        forms[PL][MASC][NOM] = fem[:-1] + 'οι'
        forms[PL][MASC][ACC] = fem[:-1] + 'ους'
        forms[PL][MASC][GEN] = fem[:-1] + 'ων'
        forms[PL][MASC][VOC] = fem[:-1] + 'οι'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = fem[:-1] + 'ων'
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = fem[:-1] + 'α'
        forms[PL][NEUT][ACC] = fem[:-1] + 'α'
        forms[PL][NEUT][GEN] = fem[:-1] + 'ων'
        forms[PL][NEUT][VOC] = fem[:-1] + 'α'

        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        if masc != 'μέγας':
            for num in forms.keys():
                for gender in forms[num].keys():
                    for case, form in forms[num][gender].items():
                        forms[num][gender][case] = put_accent(form, ULTIMATE, true_syllabification=True)

        alt_forms = alternative_forms_us(adj)

        return forms, alt_forms

    elif masc[-2:] in ['ύς', 'υς'] and where_is_accent(fem) == PENULTIMATE:
        # oksys, okseos

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][GEN] = masc[:-1]
        forms[SG][MASC][VOC] = masc[:-1]

        forms[PL][MASC][NOM] = masc[:-2] + 'είς'
        forms[PL][MASC][ACC] = masc[:-2] + 'είς'
        forms[PL][MASC][GEN] = masc[:-2] + 'έων'
        forms[PL][MASC][VOC] = masc[:-2] + 'είς'
        if fem != '-':
            forms[SG][FEM][NOM] = fem
            forms[SG][FEM][ACC] = fem
            forms[SG][FEM][GEN] = fem + 'ς'
            forms[SG][FEM][VOC] = fem
            forms[PL][FEM][NOM] = fem[:-1] + 'ες'
            forms[PL][FEM][ACC] = fem[:-1] + 'ες'
            forms[PL][FEM][GEN] = fem[:-2] + 'ιών'
            forms[PL][FEM][VOC] = fem[:-1] + 'ες'

        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = neut
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][NEUT][NOM] = masc[:-2] + 'έα'
        forms[PL][NEUT][ACC] = masc[:-2] + 'έα'
        forms[PL][NEUT][GEN] = masc[:-2] + 'έων'
        forms[PL][NEUT][VOC] = masc[:-2] + 'έα'

        alt_forms = alternative_forms_us2(adj)

        return forms, alt_forms

    elif masc[-2:] in ['ης', 'άς', 'ής', 'ας'] and fem[-1] in ['α', 'ύ'] and neut[-3:] == 'ικο':
        # hs, a, iko
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][GEN] = masc[:-1]
        forms[SG][MASC][VOC] = masc[:-1]
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = neut[:-1] + 'ου'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = masc[:-1] + 'δες'
        forms[PL][MASC][ACC] = masc[:-1] + 'δες'
        forms[PL][MASC][GEN] = masc[:-1] + 'δων'
        forms[PL][MASC][VOC] = masc[:-1] + 'δες'
        if fem[-2:] == 'ού':
            forms[PL][FEM][NOM] = fem + 'δες'
            forms[PL][FEM][ACC] = fem + 'δες'
            forms[PL][FEM][GEN] = fem + 'δων'
            forms[PL][FEM][VOC] = fem + 'δες'
        else:
            forms[PL][FEM][NOM] = fem[:-1] + 'ες'
            forms[PL][FEM][ACC] = fem[:-1] + 'ες'
            # forms[PL][FEM][GEN] = ''
            forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = neut[:-1] + 'α'
        forms[PL][NEUT][ACC] = neut[:-1] + 'α'
        forms[PL][NEUT][GEN] = neut[:-1] + 'ων'
        forms[PL][NEUT][VOC] = neut[:-1] + 'α'

        alternative_forms = None
        # προσθεσε εναλλακτικές μορφές για το θυληκό γενος ξανθομάλλα και ξανθομαλλού
        if fem[-1] == 'α':
            alt_fem = put_accent_on_the_ultimate(fem[:-1] + 'ου')
            if alt_fem in greek_corpus:
                alternative_forms = alternative_forms_ou(alt_fem)

        return forms, alternative_forms

    elif masc[-2:] == 'ής' and fem[-1] == 'ά' and neut[-1] == 'ί':
        # colors hs, a, i
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][GEN] = masc[:-1]
        forms[SG][MASC][VOC] = masc[:-1]
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = fem[:-1] + 'ού'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut
        forms[PL][MASC][NOM] = fem[:-1] + 'οί'
        forms[PL][MASC][ACC] = fem[:-1] + 'ούς'
        forms[PL][MASC][GEN] = fem[:-1] + 'ών'
        forms[PL][MASC][VOC] = fem[:-1] + 'οί'
        forms[PL][FEM][NOM] = fem[:-1] + 'ές'
        forms[PL][FEM][ACC] = fem[:-1] + 'ές'
        forms[PL][FEM][GEN] = fem[:-1] + 'ών'
        forms[PL][FEM][VOC] = fem[:-1] + 'ές'
        forms[PL][NEUT][NOM] = fem[:-1] + 'ά'
        forms[PL][NEUT][ACC] = fem[:-1] + 'ά'
        forms[PL][NEUT][GEN] = fem[:-1] + 'ών'
        forms[PL][NEUT][VOC] = fem[:-1] + 'ά'

        return forms, None

    elif masc[-2:] == 'ώς' and fem[-1] == 'α' and neut[-1] == 'ς':
        # archaic participles, not sure which endings to choose, as it seems both are used, ancient and modern (especially in fem),
        # for now I will settle with modernized
        thema = masc[:-1] + 'τ'
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = thema + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut
        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = thema + 'ων'
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = fem[:-1] + 'ων'
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = thema + 'ων'
        forms[PL][NEUT][VOC] = thema + 'α'

        return forms, None

    elif masc[-2:] in ['ης', 'ής'] and fem[-2:] in ['ής', 'ης'] and neut[-2:] in ['ες', 'ές']:
        gen_pl = masc[:-2] + 'ων'
        if masc[-3] == 'δ':
            gen_pl = put_accent_on_the_ultimate(masc[:-2] + 'ων')

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][GEN] = masc[:-2] + 'ους'
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][VOC] = masc[:-1]
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][GEN] = fem[:-2] + 'ους'
        forms[SG][FEM][ACC] = fem[:-1]
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = fem[:-2] + 'ους'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = masc[:-2] + 'εις'
        forms[PL][MASC][ACC] = masc[:-2] + 'εις'
        forms[PL][MASC][GEN] = gen_pl
        forms[PL][MASC][VOC] = masc[:-2] + 'εις'
        forms[PL][FEM][NOM] = masc[:-2] + 'εις'
        forms[PL][FEM][ACC] = masc[:-2] + 'εις'
        forms[PL][FEM][GEN] = gen_pl
        forms[PL][FEM][VOC] = masc[:-2] + 'εις'
        forms[PL][NEUT][NOM] = masc[:-2] + 'η'
        forms[PL][NEUT][ACC] = masc[:-2] + 'η'
        forms[PL][NEUT][GEN] = gen_pl
        forms[PL][NEUT][VOC] = masc[:-2] + 'η'

        if where_is_accent(masc) == ULTIMATE:
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
        gen_sg = thema + 'ος'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        if not accent and put_accent(gen_sg, ULTIMATE) in greek_corpus:
            forms[SG][MASC][GEN] = put_accent(gen_sg, ULTIMATE)
            forms[SG][NEUT][GEN] = put_accent(gen_sg, ULTIMATE)
        else:
            forms[SG][MASC][GEN] = gen_sg
            forms[SG][NEUT][GEN] = gen_sg
        forms[SG][MASC][VOC] = masc

        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut
        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][NEUT][VOC] = thema + 'α'

        alternative_forms = None

        if masc[-3:] in ['σας', 'ξας', 'ψας']:
            alternative_forms = alternative_forms_modern_3rd(adj)

        if len(neuters) > 1 and len(feminins) > 1:

            alternative_forms = alternative_forms_wn(f'{masc}/{feminins[1]}/{neuters[1]}')

        elif len(neuters) > 1:
            alternative_forms = alternative_forms_wn(f'{masc}/{feminins[0]}/{neuters[1]}')

        elif len(feminins) > 1:
            alternative_forms = alternative_forms_wn(f'{masc}/{feminins[1]}/{neuters[0]}')

        forms = put_accent_on_unaccented_forms(forms)
        alternative_forms = put_accent_on_unaccented_forms(alternative_forms)
        if masc[-4:] in ['ντας']:
            forms[SG][MASC][GEN] = masc[:-1]
            forms[SG][MASC][VOC] = masc[:-1]
        return forms, alternative_forms

    elif (masc[-4:] == 'ονας' or masc[-2:] in ['ών', 'ων']) and fem[-2:] == 'ων' and neut[-2:] == 'ον':

        # ονας, ων, ον
        thema = neut

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'α'
        forms[SG][MASC][VOC] = thema + 'α'
        if masc[-2:] in ['ών', 'ων']:
            forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = thema + 'α'
        forms[SG][FEM][GEN] = thema + 'ος'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = thema + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = thema + 'ες'
        forms[PL][FEM][ACC] = thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(thema + 'ων')
        forms[PL][FEM][VOC] = thema + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][NEUT][VOC] = thema + 'α'

        alternative_forms = alternative_forms_onas(adj)

        return forms, alternative_forms

    elif masc[-2:] == 'ωρ':

        thema = masc[:-2] + 'ορ'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = thema
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = thema + 'α'
        forms[SG][FEM][GEN] = thema + 'ος'
        forms[SG][FEM][VOC] = thema
        # forms[SG][NEUT][NOM] = neut
        # forms[SG][NEUT][GEN] = thema + 'ος'
        # forms[SG][NEUT][ACC] = neut
        # forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = thema + 'ες'
        forms[PL][FEM][ACC] = thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][FEM][VOC] = thema + 'ες'

        return forms, None

    elif masc[-3:] in ['είς'] and fem[-2:] in ['σα'] and neut[-2:] in ['έν']:
        # participles

        thema = neut + 'τ'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = thema + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][NEUT][VOC] = thema + 'α'

        alternative_forms = None

        return forms, alternative_forms

    elif masc in ['άρρην'] or (masc[-2:] in ['ων'] and neut[-2:] in ['ον']):
        # ancient 3rd declesion

        thema = neut

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = neut
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = thema + 'α'
        forms[SG][FEM][GEN] = thema + 'ος'
        forms[SG][FEM][VOC] = neut
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = thema + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = thema + 'ες'
        forms[PL][FEM][ACC] = thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms[PL][FEM][VOC] = thema + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][NEUT][VOC] = thema + 'α'

        return forms, None

    elif masc[-2:] == 'ις' and masc == fem and neut == '-':
        # ancient 3rd declesion
        thema = masc[:-1] + 'δ'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = masc
        forms[SG][FEM][ACC] = thema + 'α'
        forms[SG][FEM][GEN] = thema + 'ος'
        forms[SG][FEM][VOC] = masc

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = thema + 'ες'
        forms[PL][FEM][ACC] = thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(thema + 'ων')
        forms[PL][FEM][VOC] = thema + 'ες'

        forms = put_accent_on_antepenultimate_in_all_forms(masc, forms)
        return forms, None

    elif masc[-1:] in ['ξ', 'ψ'] and masc == fem and neut == '-':
        # ancient 3rd declesion
        thema = masc[:-1] + 'κ'
        if masc[-4:] == 'θριξ':
            thema = masc[:-4] + 'τριχ'
        elif masc[-3:] == 'φυξ':
            thema = masc[:-3] + 'φυγ'
        elif masc[-1] == 'ψ':
            thema = masc[:-1] + 'π'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = masc
        forms[SG][FEM][ACC] = thema + 'α'
        forms[SG][FEM][GEN] = thema + 'ος'
        forms[SG][FEM][VOC] = masc

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = thema + 'ες'
        forms[PL][FEM][ACC] = thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(thema + 'ων')
        forms[PL][FEM][VOC] = thema + 'ες'
        if accent == ANTEPENULTIMATE:
            forms = put_accent_in_all_forms(forms, ANTEPENULTIMATE)
        return forms, None

    elif masc[-2:] == 'ας' and fem[-2:] == 'να' and neut[-2:] == 'αν':
        """
        not a very often occurrence: ancient type of melas, melaina, melan
        """
        thema = neut
        fem_thema = fem[:-1]
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = thema + 'α'
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = neut
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = thema + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = fem_thema + 'ες'
        forms[PL][FEM][ACC] = fem_thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem_thema + 'ων')
        forms[PL][FEM][VOC] = fem_thema + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][NEUT][VOC] = thema + 'α'

        return forms, None

    elif masc[-2:] == 'ις' and fem == masc and neut[-1] == 'ι':

        thema = neut + 'τ'
        acc_masc_fem_sing = thema + 'ά'
        if not thema + 'α' in greek_corpus:
            thema = neut + 'δ'
            acc_masc_fem_sing = neut
        fem_thema = thema
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = acc_masc_fem_sing
        forms[SG][MASC][GEN] = thema + 'ος'
        forms[SG][MASC][VOC] = neut
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = acc_masc_fem_sing
        forms[SG][FEM][GEN] = thema + 'ος'
        forms[SG][FEM][VOC] = neut
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = thema + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ες'
        forms[PL][MASC][ACC] = thema + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][MASC][VOC] = thema + 'ες'
        forms[PL][FEM][NOM] = fem_thema + 'ες'
        forms[PL][FEM][ACC] = fem_thema + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem_thema + 'ων')
        forms[PL][FEM][VOC] = fem_thema + 'ες'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(thema + 'ων')
        forms[PL][NEUT][VOC] = thema + 'α'
        if accent == ANTEPENULTIMATE:
            forms = put_accent_in_all_forms(forms, accent)

        alternative_forms = alternative_forms_tis(adj, thema)

        return forms, alternative_forms

    elif masc[-2:] == 'ως' and fem == masc and neut[-2:] == 'ων':

        thema = neut[:-2]

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = masc[:-1]
        forms[SG][MASC][GEN] = neut
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem[:-1]
        forms[SG][FEM][GEN] = neut
        forms[SG][FEM][VOC] = masc
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = neut[:-1]
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = thema + 'ῳ'
        forms[PL][MASC][ACC] = thema + 'ῳς'
        forms[PL][MASC][GEN] = thema + 'ων'
        forms[PL][MASC][VOC] = thema + 'ῳ'
        forms[PL][FEM][NOM] = thema + 'ῳ'
        forms[PL][FEM][ACC] = thema + 'ῳς'
        forms[PL][FEM][GEN] = thema + 'ῳν'
        forms[PL][FEM][VOC] = thema + 'ῳ'
        forms[PL][NEUT][NOM] = thema + 'α'
        forms[PL][NEUT][ACC] = thema + 'α'
        forms[PL][NEUT][GEN] = thema + 'ων'
        forms[PL][NEUT][VOC] = thema + 'α'

        forms = put_accent_on_antepenultimate_in_all_forms(masc, forms)

        return forms, None

    else:
        for number in forms.keys():
            for gender in forms[number].keys():
                for case in forms[number][gender].keys():
                    forms[number][gender][case] = masc

        return forms, None


def comparative_forms(comp_or_super: str) -> dict:
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
