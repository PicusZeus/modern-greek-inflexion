from typing import Any, Union

# from icecream import ic
from modern_greek_accentuation.accentuation import where_is_accent, put_accent, count_syllables, remove_all_diacritics
from modern_greek_accentuation.resources import vowels
from ..resources.resources import greek_corpus

from ..resources.variables import *

from ..resources.noun import irregular_gen_sg, irregular_voc_sg, noun_grammar_lists


def put_accent_on_unaccented_forms(forms: dict) -> dict:
    # one syllable words
    for number in forms.keys():
        for case in forms[number].keys():
            f = forms[number][case]
            if not where_is_accent(f) and count_syllables(f) > 1:
                forms[number][case] = put_accent(f, PENULTIMATE)
    return forms


def create_all_noun_forms(nom_sg: str, gen_sg: str, nom_pl: str, genders: str,
                          proper_name: bool = False) -> dict:
    """
    :param nom_sg: nominative singular
    :param gen_sg: genitive singular
    :param nom_pl: nominative plural
    :param genders: FEM or MASC or NEUT, if more than one, than separated with ','
    :param proper_name: flag useful for creation of vocatives in proper names

    """
    accent = where_is_accent(nom_sg, true_syllabification=False)
    number_of_syllables = count_syllables(nom_sg)
    fem_masc = ',' in genders
    multiple_plurals = ',' in nom_pl
    noun_all = {}
    neut_plural = False

    if multiple_plurals:
        # irregular plural neut gender
        plurals = nom_pl.split(',')
        if (plurals[0][-2:] in ['οι', 'οί'] or not plurals[0]) and plurals[1][-1] in ['α', 'ά', 'ή', 'η']:
            genders = genders + ',neut'
            neut_plural = True
            nom_pl = plurals[0]
            irregular_nom_pl = plurals[1]

    for gender in genders.split(','):

        if neut_plural and gender == NEUT:
            # they lack gen pl
            noun_all[NEUT] = {}
            noun_all[NEUT][PL] = {}
            noun_all[NEUT][PL][NOM] = irregular_nom_pl
            noun_all[NEUT][PL][ACC] = irregular_nom_pl
            noun_all[NEUT][PL][VOC] = irregular_nom_pl

            gen_pl = irregular_nom_pl[:-1] + 'ων'
            if irregular_nom_pl[-1] in ['ή', 'η', 'ά']:
                gen_pl = put_accent(gen_pl, ULTIMATE)

            if gen_pl in greek_corpus:
                noun_all[NEUT][PL][GEN] = gen_pl

            if irregular_nom_pl == 'χρόνια':
                gen_pl = 'χρόνω,χρόνων,χρονώ,χρονών'
                noun_all[NEUT][PL][GEN] = gen_pl

        elif gender == 'surname' and nom_sg[-1] != 'ς':

            noun_all[gender] = {}
            noun_all[gender][SG] = {}
            noun_all[gender][PL] = {}
            noun_all[gender][SG][NOM] = nom_sg
            noun_all[gender][SG][ACC] = nom_sg
            noun_all[gender][SG][GEN] = nom_sg
            noun_all[gender][SG][VOC] = nom_sg
            noun_all[gender][PL][NOM] = nom_sg
            noun_all[gender][PL][ACC] = nom_sg
            noun_all[gender][PL][VOC] = nom_sg
            noun_all[gender][PL][GEN] = nom_sg

            return noun_all

        else:
            # defaults
            noun_all[gender] = {}
            noun_all[gender][SG] = {}
            noun_all[gender][PL] = {}
            noun_all[gender][SG][NOM] = nom_sg
            noun_all[gender][SG][GEN] = gen_sg
            noun_all[gender][SG][VOC] = nom_sg
            noun_all[gender][PL][NOM] = nom_pl
            noun_all[gender][PL][ACC] = nom_pl
            noun_all[gender][PL][VOC] = nom_pl

            parisyllabic = count_syllables(nom_sg) == count_syllables(nom_pl)
            # it won't give a correct value if multiple plurals
            if multiple_plurals:
                parisyllabic = count_syllables(nom_sg) == count_syllables(nom_pl.split(',')[-1])

            if gender in [FEM, NEUT]:
                noun_all[gender][SG][ACC] = nom_sg

            elif gender == MASC and nom_sg[:-1] == gen_sg:
                noun_all[gender][SG][ACC] = gen_sg

            """MAIN PART"""

            if nom_sg[-2:] in ['ος', 'ός'] and gen_sg[-2:] in ['ου', 'ού']:
                # declension on os ou
                noun_all[gender][SG][ACC] = nom_sg[:-1]

                if nom_sg[:-1] + 'ν' in greek_corpus:
                    noun_all[gender][SG][ACC] = nom_sg[:-1] + ',' + nom_sg[:-1] + 'ν'
                masc_voc = put_accent(nom_sg[:-2] + 'ε', accent, true_syllabification=False)
                noun_all[gender][SG][VOC] = masc_voc

                if proper_name and count_syllables(nom_sg) < 3:
                    if accent != ULTIMATE:
                        properN_masc_voc = nom_sg[:-1]
                        noun_all[gender][SG][VOC] = properN_masc_voc
                        # but this rule is not always used (Παύλο και Παύλε) and sometimes voc on e is still in usage

                        if masc_voc.lower() in greek_corpus:
                            noun_all[gender][SG][VOC] = properN_masc_voc + ',' + masc_voc

                elif (nom_sg[-3] in ['ι'] and accent == ANTEPENULTIMATE) or nom_sg in noun_grammar_lists[VOCATIVE_MASC_SG_O]:
                    # i need to get a proper list
                    if masc_voc in greek_corpus:
                        noun_all[gender][SG][VOC] = masc_voc + ',' + nom_sg[:-1]
                    else:
                        noun_all[gender][SG][VOC] = nom_sg[:-1]

                if nom_pl:
                    g_pl = []
                    acc_pl = []

                    for n_pl in nom_pl.split(','):

                        accent_pl = where_is_accent(n_pl, true_syllabification=False)
                        sinizisi = where_is_accent(n_pl, true_syllabification=False) != where_is_accent(n_pl,
                                                                                                        true_syllabification=True)

                        if (accent_pl == PENULTIMATE or accent_pl == ULTIMATE or
                                nom_sg in noun_grammar_lists[PROPAROKSITONA_GEN_PL]):

                            g_pl.append(put_accent(n_pl[:-2] + 'ων', accent_pl, true_syllabification=False))

                            acc_pl.append(put_accent(n_pl[:-2] + 'ους', accent_pl, true_syllabification=False))

                        else:

                            gen_proparoksit = put_accent(n_pl[:-2] + 'ων', accent_pl, true_syllabification=False)
                            gen_paroksit = put_accent(n_pl[:-2] + 'ων', PENULTIMATE, true_syllabification=False)
                            acc_proparoksit = put_accent(n_pl[:-2] + 'ους', accent_pl, true_syllabification=False)
                            acc_paroksit = put_accent(n_pl[:-2] + 'ους', PENULTIMATE, true_syllabification=False)
                            if sinizisi or gen_proparoksit in greek_corpus:
                                g_pl.append(gen_proparoksit)
                                if nom_sg in noun_grammar_lists[PAROKSITONA_GEN_PL_MOVING]:
                                    g_pl.append(gen_paroksit)
                            else:
                                g_pl.append(gen_paroksit)

                            if sinizisi and gen_paroksit in greek_corpus:
                                g_pl.append(gen_paroksit)

                            if sinizisi or acc_proparoksit in greek_corpus:
                                acc_pl.append(acc_proparoksit)
                                if acc_paroksit in greek_corpus or nom_sg in noun_grammar_lists[PAROKSITONA_GEN_PL_MOVING]:
                                    acc_pl.append(acc_paroksit)

                            else:
                                acc_pl.append(acc_paroksit)

                    acc_pl = ','.join(acc_pl)
                    gen_pl = ','.join(g_pl)

                    noun_all[gender][PL][GEN] = gen_pl
                    noun_all[gender][PL][ACC] = acc_pl

            elif (nom_sg[-1:] == 'ς' and nom_pl and nom_pl[-2:] in ['ές', 'ες', 'οι'] and
                  gen_sg and gen_sg == nom_sg[:-1]):
                # both pari and imparisyllaba -s, -es

                if (accent == ANTEPENULTIMATE or accent == PENULTIMATE) and parisyllabic and nom_sg.endswith('ας'):
                    # old 3rd declension on ης, ας
                    # get archaic gen
                    logia_gen = nom_sg[:-2] + 'ος'

                    if number_of_syllables == 2:
                        logia_gen = put_accent(nom_sg[:-2] + 'ος', ULTIMATE)

                    if fem_masc:
                        if gender == FEM:
                            noun_all[gender][SG][GEN] = logia_gen
                        else:
                            noun_all[gender][SG][GEN] = ','.join([gen_sg, logia_gen])
                    elif logia_gen in greek_corpus:
                        noun_all[gender][SG][GEN] = ','.join([gen_sg, logia_gen])
                    else:
                        noun_all[gender][SG][GEN] = gen_sg

                elif nom_sg.endswith('ής') and parisyllabic:
                    logia_gen = nom_sg[:-2] + 'ού'
                    if fem_masc:

                        if gender == FEM:
                            noun_all[gender][SG][GEN] = logia_gen
                        else:
                            noun_all[gender][SG][GEN] = ','.join([gen_sg, logia_gen])
                    else:
                        if logia_gen in greek_corpus:
                            noun_all[gender][SG][GEN] = ','.join([gen_sg, logia_gen])

                elif nom_sg.endswith('ης') and parisyllabic and accent == PENULTIMATE:
                    noun_all[gender][PL][GEN] = put_accent(nom_sg[:-2] + 'ων', ULTIMATE)
                    if ',' in genders:
                        logia_gen = nom_sg[:-2] + 'ου'
                        if gender == FEM:
                            noun_all[gender][SG][GEN] = logia_gen
                        else:
                            noun_all[gender][SG][GEN] = ','.join([gen_sg, logia_gen])
                        noun_all[gender][SG][VOC] = nom_sg[:-2] + 'α' + ',' + nom_sg[:-1]
                    else:
                        noun_all[gender][SG][GEN] = gen_sg

                # gen_pl can move accent, take into account multiple plurals
                g_pl = []
                acc_pl = []

                for n_pl in nom_pl.split(','):

                    pl_accent = where_is_accent(n_pl, true_syllabification=False)
                    parisyllabic = count_syllables(nom_sg) == count_syllables(n_pl)
                    gen_pl = n_pl[:-2] + 'ων'

                    if n_pl[-2:] in ['ές', 'ες']:
                        acc_pl.append(n_pl)
                    elif n_pl.endswith('οι'):
                        acc_pl.append(n_pl[:-2] + 'ους')
                        # g_pl.append(n_pl[:-2] + 'ων')

                    if parisyllabic and (nom_sg[-2:] in ['ης', 'ής', 'ας', 'άς']):

                        if nom_sg in noun_grammar_lists[PROPAROKSITONA_GEN_PL]:
                            pass

                        elif ((nom_sg.endswith('ας') and
                               nom_sg not in noun_grammar_lists[OKSITONA_GEN_PL_MASC] and
                               count_syllables(nom_sg) > 2) and
                              not nom_sg.endswith('ίας')):
                            gen_pl = put_accent(gen_pl, PENULTIMATE, true_syllabification=False)

                        elif not n_pl.endswith('οι'):
                            gen_pl = put_accent(gen_pl, ULTIMATE)

                        g_pl.append(gen_pl)

                    else:
                        gen_pl = put_accent(gen_pl, pl_accent, true_syllabification=False)
                        g_pl.append(gen_pl)

                voc_on_a = False
                if nom_sg[-3:] in ['τής', 'χης']:
                    voc_a = put_accent(nom_sg[:-2] + 'ά', accent)
                    if voc_a in greek_corpus:
                        voc_on_a = voc_a

                noun_all[gender][SG][ACC] = nom_sg[:-1]
                noun_all[gender][SG][VOC] = nom_sg[:-1]
                if voc_on_a:
                    noun_all[gender][SG][VOC] = voc_on_a
                noun_all[gender][PL][GEN] = ','.join(g_pl)
                noun_all[gender][PL][ACC] = ','.join(acc_pl)

            elif nom_sg.endswith('ις') and gender in [FEM, MASC]:

                #  ancient Greek 3rd declension
                acc_n = nom_sg[:-1] + 'ν'
                if gen_sg.endswith('εως'):
                    noun_all[gender][PL][GEN] = nom_pl[:-2] + 'ων'
                    noun_all[gender][SG][ACC] = acc_n

                elif gen_sg.endswith('ος') or gen_sg.endswith('ός'):
                    if acc_n in greek_corpus:
                        noun_all[gender][SG][ACC] = acc_n
                    else:
                        noun_all[gender][SG][ACC] = put_accent(gen_sg[:-2] + 'α', ANTEPENULTIMATE)
                    if where_is_accent(gen_sg) == ULTIMATE and nom_sg != 'παις':
                        noun_all[gender][PL][GEN] = put_accent(nom_pl[:-2] + 'ων', ULTIMATE)
                    else:
                        noun_all[gender][PL][GEN] = put_accent(nom_pl[:-2] + 'ων', PENULTIMATE)

                noun_all[gender][SG][VOC] = nom_sg[:-1]

            elif nom_sg[-1:] in ['α', 'ά', 'ή', 'η'] and gen_sg[-1:] == 'ς' and gender != NEUT:

                if nom_sg + 'ν' in greek_corpus:
                    noun_all[gender][SG][ACC] = nom_sg + ',' + nom_sg + 'ν'
                else:
                    noun_all[gender][SG][ACC] = nom_sg
                gen_pl = []
                for n_pl in nom_pl.split(','):
                    parisyllabic = count_syllables(nom_sg) == count_syllables(n_pl)

                    """
                    the most difficult is of course to determine the accent of gen pl, 
                    fortunately we have compiled lists of the most difficult cases
                    """

                    if n_pl[-2:] in ['ες', 'ές'] and parisyllabic:

                        g_pl = n_pl[:-2] + 'ων'
                        if (nom_sg[-3:] in ['ίδα', 'άδα'] or
                                nom_sg in noun_grammar_lists[PROPAROKSITONA_GEN_PL] or
                                nom_sg in noun_grammar_lists[PAROKSITONA_GEN_PL]):

                            gen_pl.append(g_pl)

                        elif nom_sg.endswith('ητα') or nom_sg in noun_grammar_lists[PAROKSITONA_GEN_PL_MOVING]:
                            gen_pl.append(put_accent(g_pl, PENULTIMATE))

                        elif not (',' in nom_pl) and nom_sg not in noun_grammar_lists[WITHOUT_GEN_PL]:

                            gen_pl.append(put_accent(g_pl, ULTIMATE))

                    elif n_pl.endswith('εις'):
                        gen_pl.append(nom_pl[:-3] + 'εων')
                        if nom_sg in noun_grammar_lists[FEMININA_H_EIS]:
                            if nom_sg[:-1] + 'ις' in greek_corpus:
                                noun_all[gender][SG][NOM] = nom_sg + ',' +  nom_sg[:-1] + 'ις'
                            if nom_sg[:-1] + 'ιν' in greek_corpus:
                                noun_all[gender][SG][ACC] = nom_sg + ',' + nom_sg[:-1] + 'ιν'

                    elif n_pl:
                        pl_accent = where_is_accent(n_pl, true_syllabification=False)
                        gen_pl.append(put_accent(n_pl[:-2] + 'ων', pl_accent, true_syllabification=False))

                noun_all[gender][PL][GEN] = ','.join(gen_pl)


            elif nom_sg[-1:] == 'α' and gender == NEUT:
                noun_all[gender][SG][ACC] = nom_sg
                gen_pl = ''
                if nom_pl:
                    # there can be alternative roots like gala
                    gen_pl = ','.join([put_accent(n_pl[:-1] + 'ων', PENULTIMATE) for n_pl in nom_pl.split(',')])
                noun_all[gender][PL][GEN] = gen_pl

            elif nom_sg[-1:] in ['ς', 'ν'] and gen_sg != nom_sg and gender == NEUT:
                # to filter out aklita

                noun_all[gender][SG][ACC] = nom_sg

                gen_sg_accent = where_is_accent(gen_sg.split(',')[0])
                if gen_sg_accent == ANTEPENULTIMATE:
                    gen_sg_accent = PENULTIMATE

                # plural sometimes doesnt exist
                if nom_pl:
                    gen_pl = put_accent(nom_pl.split(',')[0][:-1] + 'ων', gen_sg_accent)

                    if nom_pl[-1] in ['η', 'ή']:
                        gen_pl = put_accent(gen_pl, ULTIMATE)
                        gen_pl_ewn = put_accent(nom_pl[:-1] + 'εων', PENULTIMATE)
                        if gen_pl_ewn in greek_corpus:
                            gen_pl = gen_pl_ewn

                    if gen_pl not in greek_corpus:
                        gen_pl_alt = put_accent(gen_pl, PENULTIMATE)
                        if gen_pl_alt in greek_corpus:
                            gen_pl = gen_pl_alt

                    if nom_sg not in noun_grammar_lists[WITHOUT_GEN_PL]:
                        noun_all[gender][PL][GEN] = gen_pl

            elif nom_sg[-1:] in ['ο', 'ό', 'ί', 'ι', 'ΐ', 'ύ', 'υ'] and gender == NEUT and nom_sg != gen_sg:

                noun_all[gender][SG][ACC] = nom_sg
                gs_pl = []
                if nom_pl and gen_sg:
                    for g_sg in gen_sg.split(','):
                        gen_accent = where_is_accent(g_sg, true_syllabification=False)
                        if g_sg[-1] == 'ς' and gen_accent == ANTEPENULTIMATE:
                            gs_pl.append(put_accent(g_sg[:-2] + 'ων', PENULTIMATE, true_syllabification=False))
                        else:
                            gs_pl.append(put_accent(g_sg[:-2] + 'ων', gen_accent, true_syllabification=False))
                noun_all[gender][PL][GEN] = ','.join(gs_pl)

            elif nom_sg[-2:] in ['ού', 'ου'] and gender == FEM:
                noun_all[gender][SG][ACC] = nom_sg
                gen_pl = ''
                if nom_pl:
                    pl_accent = where_is_accent(nom_pl, true_syllabification=False)
                    gen_pl = put_accent(nom_pl[:-2] + 'ων', pl_accent, true_syllabification=False)
                noun_all[gender][PL][GEN] = gen_pl

            elif nom_sg[-3:] == 'έας' and nom_pl[-3:] == 'είς':

                if gender == MASC:
                    noun_all[gender][SG][GEN] = gen_sg + ',' + nom_sg[:-2] + 'ως'
                else:
                    noun_all[gender][SG][GEN] = nom_sg[:-2] + 'ως'
                noun_all[gender][SG][ACC] = nom_sg[:-1]
                noun_all[gender][SG][VOC] = nom_sg[:-1]

                gen_pl = ''
                if nom_pl:
                    gen_pl = nom_sg[:-2] + 'ων'
                noun_all[gender][PL][GEN] = gen_pl

            elif (nom_sg.endswith('ής') and nom_pl.endswith('είς') and
                  gender == MASC and gen_sg.endswith('ούς')):
                noun_all[gender][SG][GEN] = gen_sg + ',' + nom_sg[:-1]
                noun_all[gender][SG][ACC] = nom_sg[:-1]
                noun_all[gender][SG][VOC] = nom_sg[:-1]
                noun_all[gender][PL][GEN] = nom_sg[:-2] + 'ών'

            elif gen_sg[-3:] == 'εως' and nom_sg[-1] == 'ς':
                noun_all[gender][SG][ACC] = nom_sg[:-1]
                acc_sg_arch = nom_sg[:-1] + 'ν'
                if nom_sg[-2:] == 'ις':
                    noun_all[gender][SG][GEN] = gen_sg
                    noun_all[gender][SG][ACC] = acc_sg_arch

                elif gender == MASC:
                    noun_all[gender][SG][GEN] = gen_sg
                    if nom_sg[-2] not in ['υ', 'ύ']:
                        noun_all[gender][SG][ACC] = nom_sg[:-1]
                        if gender == MASC:
                            noun_all[gender][SG][GEN] = gen_sg + ',' + nom_sg[:-1]
                    else:
                        noun_all[gender][SG][ACC] = acc_sg_arch
                    if nom_sg.endswith('υς') and nom_sg[:-1] in greek_corpus:
                        noun_all[gender][SG][GEN] = gen_sg + ',' + nom_sg[:-1]

                        noun_all[gender][SG][ACC] = acc_sg_arch + ',' + nom_sg[:-1]

                noun_all[gender][SG][VOC] = nom_sg[:-1]
                noun_all[gender][PL][GEN] = gen_sg[:-1] + 'ν'

            elif nom_sg[-2:] == 'ως' and gen_sg[-1] == 'ω':

                noun_all[gender][SG][ACC] = gen_sg
                noun_all[gender][SG][VOC] = nom_sg
                noun_all[gender][PL][GEN] = gen_sg + 'ν'

            elif nom_sg == nom_pl:
                # aklita
                noun_all[gender][SG][ACC] = nom_sg
                noun_all[gender][PL][GEN] = nom_pl

            elif gen_sg[-2:] in ['ος', 'ός'] and gen_sg[-3] not in vowels:
                # archaic gen on os after consonant
                noun_all[gender][SG][VOC] = nom_sg

                if gender != NEUT:

                    noun_all[gender][SG][ACC] = gen_sg[:-2] + 'α'
                    if not accent:
                        # it means a single syllable noun
                        noun_all[gender][SG][ACC] = put_accent(gen_sg[:-2] + 'α', PENULTIMATE)

                    if nom_sg.endswith('ωρ'):
                        noun_all[gender][SG][VOC] = nom_sg[:-2] + 'ορ'
                    elif nom_sg.endswith('ηρ'):
                        noun_all[gender][SG][VOC] = nom_sg[:-2] + 'ερ'

                if gender == NEUT:
                    noun_all[gender][PL][GEN] = put_accent(nom_pl[:-1] + 'ων', PENULTIMATE)
                    if not accent:
                        noun_all[gender][PL][GEN] = put_accent(nom_pl[:-1] + 'ων', ULTIMATE)
                else:
                    noun_all[gender][PL][GEN] = put_accent(nom_pl[:-2] + 'ων', PENULTIMATE)
                    if not accent:
                        noun_all[gender][PL][GEN] = put_accent(nom_pl[:-2] + 'ων', ULTIMATE)

            elif nom_sg[-1:] == 'ς' and gender != NEUT:

                # special cases:
                noun_all[gender][SG][ACC] = nom_sg[:-1]
                if nom_sg[:-1] + 'ν' in greek_corpus:
                    noun_all[gender][SG][ACC] = nom_sg[:-1] + ',' + nom_sg[:-1] + 'ν'
                noun_all[gender][SG][VOC] = nom_sg[:-1]

                gen_pl = ''
                if nom_pl:
                    gen_pl = nom_pl[:-2] + 'ων'
                    if not ',' in gen_sg:
                        accent_gen_sg = where_is_accent(gen_sg, true_syllabification=False)
                        gen_pl = put_accent(gen_pl, accent_gen_sg, true_syllabification=False)
                    else:
                        accent_nom_pl = where_is_accent(nom_pl, true_syllabification=False)
                        if accent_nom_pl != ANTEPENULTIMATE:
                            gen_pl = put_accent(gen_pl, accent_nom_pl, true_syllabification=False)
                        else:
                            gen_pl = put_accent(gen_pl, PENULTIMATE, true_syllabification=False)
                noun_all[gender][PL][GEN] = gen_pl

                if remove_all_diacritics(nom_pl[-3:]) in ['δες', 'τες']:
                    accs = []
                    vocs = [nom_sg]
                    acc_1 = nom_sg[:-1]
                    if acc_1 in greek_corpus:
                        accs.append(acc_1)
                    acc_2 = nom_pl[:-2] + 'α'
                    if acc_2 in greek_corpus:
                        accs.append(acc_2)
                    voc_2 = nom_sg[:-1]
                    if voc_2 in greek_corpus:
                        vocs.append(voc_2)
                    noun_all[gender][SG][ACC] = ','.join(accs)
                    noun_all[gender][SG][VOC] = ','.join(vocs)

                elif nom_sg[-3:] in ['εύς', 'ευς']:

                    noun_all[gender][SG][ACC] = gen_sg[:-2] + 'α'
                    if nom_sg == 'Ζευς':
                        noun_all[gender][SG][ACC] = 'Δία,Διά'
                    noun_all[gender][SG][VOC] = nom_sg[:-1]

                elif nom_sg[-2:] == 'ής' and nom_pl[-3:] == 'είς':
                    noun_all[gender][PL][GEN] = nom_pl[:-3] + 'ών'

            elif (nom_sg[-1:] in ['ρ', 'ν', 'ξ', 'ύ', 'υ']) and (gen_sg[-2:] in ['ος', 'ός']):
                if gender != NEUT:
                    if not nom_pl:
                        print(nom_sg, 'no nom_pl error')
                        raise ValueError
                    noun_all[gender][SG][ACC] = nom_pl[:-2] + 'α'
                    voc_sg = gen_sg[:-2]
                    if gen_sg[-4:] in ['ντος', 'κτος'] or count_syllables(nom_sg) == 1:
                        voc_sg = nom_sg
                    noun_all[gender][SG][VOC] = voc_sg

                    gen_pl = put_accent(nom_pl[:-2] + 'ων', PENULTIMATE)
                    if where_is_accent(gen_sg) == ULTIMATE:
                        gen_pl = put_accent(gen_pl, ULTIMATE)
                    noun_all[gender][PL][GEN] = gen_pl
                else:
                    noun_all[gender][SG][ACC] = nom_sg
                    gen_pl = put_accent(nom_pl[:-1] + 'ων', PENULTIMATE)
                    noun_all[gender][PL][GEN] = gen_pl

            elif not nom_sg and (nom_pl[-2:] in ['ες', 'οι', 'ές', 'οί', 'αι', 'αί'] or
                                 nom_pl[-1:] in ['α', 'η', 'ά', 'ή'] or
                                 nom_pl.endswith('εις')):
                accent = where_is_accent(nom_pl, true_syllabification=False)
                if nom_pl[-2:] in ['οι', 'οί']:

                    acc_pl = put_accent(nom_pl[:-2] + 'ους', accent, true_syllabification=False)

                    if accent == ANTEPENULTIMATE:
                        acc_pl_alt = put_accent(acc_pl, PENULTIMATE, true_syllabification=False)
                        if acc_pl in greek_corpus and acc_pl_alt in greek_corpus:
                            acc_pl = acc_pl + ',' + acc_pl_alt
                        elif acc_pl_alt in greek_corpus:
                            acc_pl = acc_pl_alt

                    noun_all[gender][PL][ACC] = acc_pl

                if nom_pl[-2:] in ['οι', 'οί'] or nom_pl[-1] in ['α', 'ά']:

                    if nom_pl.endswith('ι') or nom_pl.endswith('ί'):
                        gen_pl = nom_pl[:-2] + 'ων'
                    else:
                        gen_pl = nom_pl[:-1] + 'ων'

                    if nom_pl.endswith('ια'):
                        gen_pl = put_accent(gen_pl, ULTIMATE)
                    elif accent == ANTEPENULTIMATE:
                        gen_pl_alt = put_accent(gen_pl, PENULTIMATE, true_syllabification=False)
                        if gen_pl in greek_corpus and gen_pl_alt in greek_corpus:
                            gen_pl = gen_pl + ',' + gen_pl_alt
                        elif gen_pl not in greek_corpus:
                            gen_pl = gen_pl_alt
                    elif accent == ULTIMATE:
                        gen_pl = put_accent(gen_pl, ULTIMATE)

                    noun_all[gender][PL][GEN] = gen_pl
                elif nom_pl[-2:] in ['ες', 'ές', 'αι', 'αί']:
                    gen_pl = put_accent(nom_pl[:-2] + 'ων', ULTIMATE)

                    if accent != ULTIMATE and nom_pl[-4:-2] in ['άδ', 'ήτ']:
                        gen_pl = put_accent(gen_pl, PENULTIMATE)

                    noun_all[gender][PL][GEN] = gen_pl

                elif nom_pl[-1] in ['η', 'ή']:

                    gen_pl = put_accent(nom_pl[:-1] + 'ων', ULTIMATE)
                    noun_all[gender][PL][GEN] = gen_pl

                else:
                    gen_pl = nom_pl[:-2] + 'ων'
                    noun_all[gender][PL][GEN] = gen_pl

            """
            irregularities
            """
            if nom_sg == 'χρόνος':
                noun_all[gender][PL][GEN] = 'χρόνων,χρονών,χρόνω,χρονώ'

            # gen_sg
            if nom_sg in irregular_gen_sg.keys():
                noun_all[gender][SG][GEN] = irregular_gen_sg[nom_sg]
            if nom_sg in irregular_voc_sg:
                noun_all[gender][SG][VOC] = irregular_voc_sg[nom_sg]

    return noun_all
