from __future__ import annotations

from copy import deepcopy

from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_ultimate, \
    put_accent_on_the_penultimate, put_accent
from modern_greek_accentuation.resources import vowels

from modern_greek_inflexion.adjective.all.create_all_alt import alternative_forms_r, alternative_forms_ios, \
    alternative_forms_us, alternative_fem_os, alternative_forms_kxth, alternative_forms_modern_3rd, \
    alternative_forms_onas, alternative_forms_tis, alternative_forms_wn, alternative_forms_us2, alternative_forms_ou
from modern_greek_inflexion.adjective._helpers import put_accent_on_all_forms, put_accent_on_unaccented_forms
from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.adj import adj_basic_template
from modern_greek_inflexion.resources.typing import genders_declensions_type, adj_declension_degree_type
from modern_greek_inflexion.resources.variables import SG, PL, FEM, MASC, NEUT, NOM, GEN, ACC, VOC, ANTEPENULTIMATE, \
    ULTIMATE, PENULTIMATE

"""
example
adj = {'adj': 'ωμός/ωμή/ωμό', 'comparative': 'ωμότερος/ωμότατος', 'adverb': 'ωμά',
'adverb_comparative': 'ωμότερα/ωμότατα'}
"""


def create_all_adj_forms(adj: str) -> tuple[adj_declension_degree_type, adj_declension_degree_type | None]:
    """
    :param adj: expects masc, fem and neut forms divided with slash / (eg 'ωραίος/ωραία/ωραίο). If feminine doesn't exist, it should be replaced with dash '-'.
    :return: two element tuple, first is a dictionary with all primary forms (forms[number][gender][case], the second
    one is a dictionary with alternative forms, if exists it has the same structure as the first dictionary
    """
    forms = deepcopy(adj_basic_template)
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
            forms = put_accent_on_all_forms(forms, ULTIMATE)

        alt_forms = None

        if fem_alt and fem_alt.endswith('ς'):

            alt_forms = alternative_fem_os(fem_alt, accent)

        elif fem[-2] in ['θ', 'κ', 'χ']:
            alt_forms = alternative_forms_kxth(fem, accent)
        elif fem[-2] in ['ρ', 'ν'] or (fem[-2] in vowels and fem[-1] == 'η'):
            alt_forms = alternative_forms_r(fem, accent)
        elif ((fem[-2] == 'ι' and accent in [PENULTIMATE, ANTEPENULTIMATE])
              or fem.endswith('μενη') or fem.endswith('στη')):
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
            forms = put_accent_on_all_forms(forms, ULTIMATE)

        return forms, None

    elif masc[-3:] == 'ους' and neut[-3:] == 'ουν':
        if masc[-4] == 'π':
            stem = masc[:-3] + 'οδ'
            gen_sg = stem + 'ος'
            masc_fem_acc = stem + 'α'
            masc_fem_pl = stem + 'ες'
            gen_pl = put_accent_on_the_penultimate(stem + 'ων')

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
            forms = put_accent_on_all_forms(forms, ULTIMATE)

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
            forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = neut[:-1] + 'α'
        forms[PL][NEUT][ACC] = neut[:-1] + 'α'
        forms[PL][NEUT][GEN] = neut[:-1] + 'ων'
        forms[PL][NEUT][VOC] = neut[:-1] + 'α'

        alternative_forms = None
        # πρόσθεσε εναλλακτικές μορφές για το θηλυκό γένος ξανθομάλλα και ξανθομαλλού
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
        """
        archaic participles, not sure which endings to choose,
        as it seems both are used, ancient and modern (especially in fem),
        for now I will settle with modernized
        """
        stem = masc[:-1] + 'τ'
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = stem + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut
        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = stem + 'ων'
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = fem[:-1] + 'ων'
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = stem + 'ων'
        forms[PL][NEUT][VOC] = stem + 'α'

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
            forms = put_accent_on_all_forms(forms, accent)

        return forms, None

    elif (masc[-2:] in ['ων', 'ών', 'ας', 'άς'] and
          fem[-2:] in ['σα'] and neut[-2:] in ['ον', 'όν', 'ύν', 'ών', 'ων', 'αν', 'άν']):
        # wn, ousa, on and as, asa, an

        feminines = fem.split(',')
        fem = feminines[0]
        neuters = neut.split(',')
        neut = neuters[0]
        stem = neut + 'τ'
        gen_sg = stem + 'ος'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
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
        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][NEUT][VOC] = stem + 'α'

        alternative_forms = None

        if masc[-3:] in ['σας', 'ξας', 'ψας'] or masc[-2:] in ['άς', 'ων', 'ών']:
            alternative_forms = alternative_forms_modern_3rd(adj)

        elif len(neuters) > 1 and len(feminines) > 1:

            alternative_forms = alternative_forms_wn(f'{masc}/{feminines[1]}/{neuters[1]}')

        elif len(neuters) > 1:
            alternative_forms = alternative_forms_wn(f'{masc}/{feminines[0]}/{neuters[1]}')

        elif len(feminines) > 1:
            alternative_forms = alternative_forms_wn(f'{masc}/{feminines[1]}/{neuters[0]}')

        forms = put_accent_on_unaccented_forms(forms)
        if alternative_forms:
            alternative_forms = put_accent_on_unaccented_forms(alternative_forms)
        if masc[-4:] in ['ντας']:
            forms[SG][MASC][GEN] = masc[:-1]
            forms[SG][MASC][VOC] = masc[:-1]
        return forms, alternative_forms

    elif (masc[-4:] == 'ονας' or masc[-2:] in ['ών', 'ων']) and fem[-2:] == 'ων' and neut[-2:] == 'ον':

        # ονας, ων, ον
        stem = neut

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'α'
        forms[SG][MASC][VOC] = stem + 'α'
        if masc[-2:] in ['ών', 'ων']:
            forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = stem + 'α'
        forms[SG][FEM][GEN] = stem + 'ος'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = stem + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = stem + 'ες'
        forms[PL][FEM][ACC] = stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(stem + 'ων')
        forms[PL][FEM][VOC] = stem + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][NEUT][VOC] = stem + 'α'

        alternative_forms = alternative_forms_onas(adj)

        return forms, alternative_forms

    elif masc[-2:] == 'ωρ':

        stem = masc[:-2] + 'ορ'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = stem
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = stem + 'α'
        forms[SG][FEM][GEN] = stem + 'ος'
        forms[SG][FEM][VOC] = stem

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = stem + 'ες'
        forms[PL][FEM][ACC] = stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][FEM][VOC] = stem + 'ες'

        return forms, None

    elif masc[-3:] in ['είς', 'εις'] and fem[-2:] in ['σα'] and neut[-2:] in ['έν', 'εν']:
        # participles

        stem = neut + 'τ'

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = stem + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = fem[:-1] + 'ες'
        forms[PL][FEM][ACC] = fem[:-1] + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms[PL][FEM][VOC] = fem[:-1] + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][NEUT][VOC] = stem + 'α'

        alternative_forms = None

        return forms, alternative_forms

    elif masc in ['άρρην'] or (masc[-2:] in ['ων'] and neut[-2:] in ['ον']):
        # ancient 3rd declesion

        stem = neut

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = neut
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = stem + 'α'
        forms[SG][FEM][GEN] = stem + 'ος'
        forms[SG][FEM][VOC] = neut
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = stem + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = stem + 'ες'
        forms[PL][FEM][ACC] = stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem[:-1] + 'ων')
        forms[PL][FEM][VOC] = stem + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][NEUT][VOC] = stem + 'α'

        return forms, None

    elif masc[-2:] == 'ις' and masc == fem and neut == '-':
        # ancient 3rd declension
        stem = put_accent_on_the_penultimate(masc[:-1] + 'δ')

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = masc
        forms[SG][FEM][ACC] = stem + 'α'
        forms[SG][FEM][GEN] = stem + 'ος'
        forms[SG][FEM][VOC] = masc

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = stem + 'ες'
        forms[PL][FEM][ACC] = stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(stem + 'ων')
        forms[PL][FEM][VOC] = stem + 'ες'

        alt_forms = put_accent_on_all_forms(forms, ANTEPENULTIMATE)
        return forms, alt_forms

    elif masc[-1:] in ['ξ', 'ψ'] and masc == fem and neut == '-':
        # ancient 3rd declension
        alt_forms = None
        stem = masc[:-1] + 'κ'
        if masc[-4:] == 'θριξ':
            stem = masc[:-4] + 'τριχ'
        elif masc[-3:] == 'φυξ':
            stem = masc[:-3] + 'φυγ'
        elif masc[-1] == 'ψ':
            stem = masc[:-1] + 'π'
        if accent == ANTEPENULTIMATE:
            stem = put_accent_on_the_penultimate(stem)

        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = masc
        forms[SG][FEM][NOM] = masc
        forms[SG][FEM][ACC] = stem + 'α'
        forms[SG][FEM][GEN] = stem + 'ος'
        forms[SG][FEM][VOC] = masc

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = stem + 'ες'
        forms[PL][FEM][ACC] = stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(stem + 'ων')
        forms[PL][FEM][VOC] = stem + 'ες'
        if accent == ANTEPENULTIMATE:
            alt_forms = put_accent_on_all_forms(forms, accent)
        return forms, alt_forms

    elif masc[-2:] == 'ας' and fem[-2:] == 'να' and neut[-2:] == 'αν':
        """
        not a very often occurrence: ancient type of melas, melaina, melan
        """
        stem = neut
        fem_stem = fem[:-1]
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = stem + 'α'
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = neut
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = fem
        forms[SG][FEM][GEN] = fem + 'ς'
        forms[SG][FEM][VOC] = fem
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = stem + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = fem_stem + 'ες'
        forms[PL][FEM][ACC] = fem_stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem_stem + 'ων')
        forms[PL][FEM][VOC] = fem_stem + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][NEUT][VOC] = stem + 'α'

        return forms, None

    elif masc[-2:] == 'ις' and fem == masc and neut[-1] == 'ι':

        stem = neut + 'τ'
        acc_masc_fem_sing = stem + 'ά'
        if not stem + 'α' in greek_corpus:
            stem = neut + 'δ'
            acc_masc_fem_sing = neut
        fem_stem = stem
        forms[SG][MASC][NOM] = masc
        forms[SG][MASC][ACC] = acc_masc_fem_sing
        forms[SG][MASC][GEN] = stem + 'ος'
        forms[SG][MASC][VOC] = neut
        forms[SG][FEM][NOM] = fem
        forms[SG][FEM][ACC] = acc_masc_fem_sing
        forms[SG][FEM][GEN] = stem + 'ος'
        forms[SG][FEM][VOC] = neut
        forms[SG][NEUT][NOM] = neut
        forms[SG][NEUT][GEN] = stem + 'ος'
        forms[SG][NEUT][ACC] = neut
        forms[SG][NEUT][VOC] = neut

        forms[PL][MASC][NOM] = stem + 'ες'
        forms[PL][MASC][ACC] = stem + 'ες'
        forms[PL][MASC][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][MASC][VOC] = stem + 'ες'
        forms[PL][FEM][NOM] = fem_stem + 'ες'
        forms[PL][FEM][ACC] = fem_stem + 'ες'
        forms[PL][FEM][GEN] = put_accent_on_the_ultimate(fem_stem + 'ων')
        forms[PL][FEM][VOC] = fem_stem + 'ες'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = put_accent_on_the_penultimate(stem + 'ων')
        forms[PL][NEUT][VOC] = stem + 'α'
        if accent == ANTEPENULTIMATE:
            forms = put_accent_on_all_forms(forms, accent)

        alternative_forms = alternative_forms_tis(adj, stem)

        return forms, alternative_forms

    elif masc[-2:] == 'ως' and fem == masc and neut[-2:] == 'ων':

        stem = neut[:-2]

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

        forms[PL][MASC][NOM] = stem + 'ῳ'
        forms[PL][MASC][ACC] = stem + 'ῳς'
        forms[PL][MASC][GEN] = stem + 'ων'
        forms[PL][MASC][VOC] = stem + 'ῳ'
        forms[PL][FEM][NOM] = stem + 'ῳ'
        forms[PL][FEM][ACC] = stem + 'ῳς'
        forms[PL][FEM][GEN] = stem + 'ῳν'
        forms[PL][FEM][VOC] = stem + 'ῳ'
        forms[PL][NEUT][NOM] = stem + 'α'
        forms[PL][NEUT][ACC] = stem + 'α'
        forms[PL][NEUT][GEN] = stem + 'ων'
        forms[PL][NEUT][VOC] = stem + 'α'

        forms = put_accent_on_all_forms(forms, PENULTIMATE)

        return forms, None

    else:
        for number in forms.keys():
            for gender in forms[number].keys():
                for case in forms[number][gender].keys():
                    forms[number][gender][case] = masc

        return forms, None


def create_all_comparative_forms(comp_or_super: str) -> genders_declensions_type:
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
