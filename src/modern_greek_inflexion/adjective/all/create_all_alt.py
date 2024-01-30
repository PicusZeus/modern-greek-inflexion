from copy import deepcopy

from modern_greek_accentuation.accentuation import put_accent, put_accent_on_the_penultimate, put_accent_on_the_ultimate

from modern_greek_inflexion.adjective.helpers import put_accent_in_all_forms
from modern_greek_inflexion.resources import SG, FEM, NOM, ACC, GEN, VOC, greek_corpus, NEUT, MASC, PL, ULTIMATE

alt_template = {SG: {MASC: {}, FEM: {}, NEUT: {}},
                PL: {MASC: {}, FEM: {}, NEUT: {}}}


def alternative_forms_r(fem: str, accent: str) -> dict:
    alt_forms = deepcopy(alt_template)

    if put_accent(fem[:-1] + 'ας', accent) in greek_corpus:
        alt_form = put_accent(fem[:-1] + 'α', accent)
        alt_forms[SG][FEM][NOM] = alt_form
        alt_forms[SG][FEM][ACC] = alt_form
        alt_forms[SG][FEM][GEN] = alt_form + 'ς'
        alt_forms[SG][FEM][VOC] = alt_form

    return alt_forms


def alternative_forms_ios(adj: str) -> dict:
    masc, fem, neut = adj.split('/')
    alt_forms = deepcopy(alt_template)

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


def alternative_forms_us(adj: str) -> dict:
    # only for the us, ia, y type
    alt_forms = deepcopy(alt_template)

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

    if masc.endswith('πολύς') or masc.endswith('μέγας'):
        alt_forms.pop(PL)
    # else there will be blank places, remember to check if there is sth
    # before inserting
    return alt_forms


def alternative_fem_os(fem_os: str, accent: str) -> dict:
    alt_forms = deepcopy(alt_template)

    alt_forms[SG][FEM][NOM] = fem_os
    alt_forms[SG][FEM][ACC] = fem_os[:-1]
    alt_forms[SG][FEM][GEN] = fem_os[:-2] + 'ου'
    alt_forms[SG][FEM][VOC] = fem_os[:-2] + 'ε'

    alt_forms[PL][FEM][NOM] = fem_os[:-2] + 'οι'
    alt_forms[PL][FEM][ACC] = fem_os[:-2] + 'ους'
    alt_forms[PL][FEM][GEN] = fem_os[:-2] + 'ων'
    alt_forms[PL][FEM][VOC] = fem_os[:-2] + 'οι'

    return put_accent_in_all_forms(alt_forms, accent)


def alternative_forms_kxth(fem: str, accent: str) -> dict :
    # κ, χ, θ ia, or h
    alt_forms = deepcopy(alt_template)

    alt_form = fem[:-1] + 'ια'

    if accent == ULTIMATE:
        alt_form = put_accent_on_the_ultimate(alt_form, true_syllabification=False)

    if alt_form in greek_corpus:
        alt_forms[SG][FEM][NOM] = alt_form
        alt_forms[SG][FEM][ACC] = alt_form
        alt_forms[SG][FEM][GEN] = alt_form + 'ς'
        alt_forms[SG][FEM][VOC] = alt_form

    return alt_forms


def alternative_forms_modern_3rd(adj):
    alt_forms = deepcopy(alt_template)
    masc, fem, neut = adj.split('/')

    thema = neut + 'τ'
    if thema + 'ας' in greek_corpus:
        alt_forms[SG][MASC][NOM] = thema + 'ας'
        alt_forms[SG][MASC][GEN] = thema + 'α'
        alt_forms[SG][MASC][VOC] = thema + 'α'
    if fem[:-1] + 'ης' in greek_corpus:
        alt_forms[SG][FEM][GEN] = fem[:-1] + 'ης'
    if fem + 'ν' in greek_corpus:
        alt_forms[SG][FEM][ACC] = fem + 'ν'

    return alt_forms


def alternative_forms_us2(adj: str) -> dict:
    # only for the us, ia, y type
    alt_forms = deepcopy(alt_template)

    masc, fem, neut = adj.split('/')

    if masc:
        alt_forms[SG][MASC][GEN] = masc[:-2] + 'έος'
        alt_forms[SG][NEUT][GEN] = masc[:-2] + 'έος'

    return alt_forms


def alternative_forms_wn(adj: str) -> dict:
    # wn, ousa on
    alt_forms = deepcopy(alt_template)

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
    alt_forms = deepcopy(alt_template)

    masc, fem, neut = adj.split('/')
    if neut + 'ν' in greek_corpus:
        alt_forms[SG][MASC][ACC] = neut + 'ν'
    gen_pl = put_accent_on_the_penultimate(thema + 'ων')

    alt_forms[PL][MASC][GEN] = gen_pl
    alt_forms[PL][FEM][GEN] = gen_pl
    alt_forms[PL][NEUT][GEN] = gen_pl

    return alt_forms


def alternative_forms_onas(adj: str) -> dict:
    alt_forms = deepcopy(alt_template)

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
    alt_forms = deepcopy(alt_template)

    alt_forms[SG][FEM][NOM] = fem
    alt_forms[SG][FEM][ACC] = fem
    alt_forms[SG][FEM][GEN] = fem + 'ς'
    alt_forms[SG][FEM][VOC] = fem

    alt_forms[PL][FEM][NOM] = fem + 'δες'
    alt_forms[PL][FEM][ACC] = fem + 'δες'
    alt_forms[PL][FEM][GEN] = fem + 'δων'
    alt_forms[PL][FEM][VOC] = fem + 'δες'

    return alt_forms

