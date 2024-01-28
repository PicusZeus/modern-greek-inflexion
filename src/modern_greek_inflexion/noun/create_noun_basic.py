from __future__ import annotations

from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate, \
    put_accent_on_the_antepenultimate, put_accent_on_the_ultimate, count_syllables, remove_all_diacritics, \
    put_accent, remove_diaer
from modern_greek_accentuation.resources import vowels, PENULTIMATE, ANTEPENULTIMATE, ULTIMATE
from ..resources.noun import irregular_nouns, aklita_gender, plur_tant_neut, irregular_3rd_decl_roots
from ..resources.variables import *
from ..resources.resources import greek_corpus

from ..resources.noun import noun_grammar_lists, nouns_masc_fem

from ..exceptions import NotInGreekException
from modern_greek_accentuation.accentuation import convert_to_monotonic
import re

greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)


def create_all_basic_noun_forms(noun: str, aklito: bool | str = False, gender: str | None = None,
                                proper_name: bool = False) -> dict:
    """
    :param noun:
    :param aklito:
    :param gender:
    :param proper_name:
    :return: dictionary with basic info
    """

    if not gender:
        if noun in nouns_masc_fem:
            gender = MASC_FEM
        elif noun in plur_tant_neut:
            gender = NEUT_PL
        elif noun.endswith('ικα') or noun.endswith('ικά'):
            gender = NEUT_PL

    elif noun.lower() in aklita_gender.keys():
        gender = aklita_gender[noun.lower()]
        aklito = True

    only_sg = False

    if gender == FEM_SG:
        gender = FEM
        only_sg = True
    elif gender == MASC_SG:
        gender = MASC
        only_sg = True
    elif gender == NEUT_SG:
        gender = NEUT
        only_sg = True
    """
    :param proper_name: Proper names behave differently from normal nouns, so if it is known, it should be flagged
    :param gender: In case of some nouns, gender should be given, where it cannot be correctly guessed on the basis
    of the ending
    :param aklito: Boolean (if false, inflection is found automatically, if true "aklito" (indeclinable)
    :param noun: must be nom sg
    :return: dictionary with keys: nom_sg, gen_sg, nom_pl and gender. Alternative forms are divided with coma
    """

    noun = convert_to_monotonic(noun, one_syllable_rule=False)
    if not greek_pattern.match(noun):
        raise NotInGreekException
    noun_temp = {NOM_SG: noun, GEN_SG: '', NOM_PL: '', GENDER: ''}
    number_of_syllables = count_syllables(noun, true_syllabification=False)
    accent = where_is_accent(noun, true_syllabification=False)
    ultimate_accent = accent == ULTIMATE

    # capital = noun[0].isupper()
    # noun = noun.lower()

    prefixes = ['νανο', 'μικρο', 'σκατο', 'παλιο']

    if noun in irregular_nouns.keys():
        noun_temp = irregular_nouns[noun]

    # on 'os'

    elif noun[-2:] in ['ός', 'ος']:

        stem = noun[:-2]
        plural_form = put_accent(stem + 'οι', accent, true_syllabification=False)
        gen_form = put_accent(stem + 'ου', accent, true_syllabification=False)
        if remove_diaer(plural_form) == put_accent(stem + 'οι', accent):
            plural_form = remove_diaer(plural_form)

        if remove_diaer(gen_form) == put_accent(stem + 'ου', accent):
            gen_form = remove_diaer(gen_form)

        gens_sg = []
        # gens_sg also used as flag that it is indeed os ou
        noun_temp[GENDER] = MASC
        if not gender:
            if noun in noun_grammar_lists[FEMININA_OS]:
                noun_temp[GENDER] = FEM
        # the problem is that many long words on -os that are part of some kind of jargon and do not have any other form
        # declined in the corpus, i will assume then that words above 4 syllables do exist, but only in singular, the
        # same should be the case for neuter long words on -o
        # also some proper names in greek_corpus are, as is proper, capitalized
        if gen_form in greek_corpus or gender == MASC or number_of_syllables > 4:
            gens_sg.append(gen_form)
        if accent == ANTEPENULTIMATE and noun not in noun_grammar_lists[PROPAROKSITONA_GEN_PL]:
            gen_form_alt = put_accent(gen_form, PENULTIMATE, true_syllabification=False)
            if gen_form_alt in greek_corpus:
                gens_sg.append(gen_form_alt)

        noun_temp[GEN_SG] = ','.join(gens_sg)

        if plural_form in greek_corpus or plural_form.capitalize() in greek_corpus or number_of_syllables > 3 or gender == MASC:
            noun_temp[NOM_PL] = plural_form
            if noun.endswith('ιος'):
                alt_pl = put_accent(noun[:-3] + 'αιοι', PENULTIMATE, true_syllabification=False)
                if alt_pl in greek_corpus:
                    noun_temp[NOM_PL] = plural_form + ',' + alt_pl
            if not gens_sg:
                noun_temp[GEN_SG] = gen_form

        neuter_os = False

        if noun.endswith('ος') and not gens_sg or gender == NEUT:
            # maybe its neuter like lathos
            neuter_os = False
            plural_form = stem + 'η'
            gen_form = stem + 'ους'

            if accent == ULTIMATE:
                plural_form = stem + 'ή'
                gen_form = stem + 'ούς'
            elif accent == ANTEPENULTIMATE:
                plural_form = put_accent_on_the_penultimate(plural_form)
                gen_form = put_accent_on_the_penultimate(gen_form)

            if plural_form in greek_corpus or gen_form in greek_corpus or gender == NEUT:
                noun_temp[NOM_PL] = plural_form

                if noun not in noun_grammar_lists[PAROKSITONA_GEN_NEUT_I]:
                    noun_temp[GEN_SG] = gen_form
                noun_temp[GENDER] = NEUT
                neuter_os = True

            # γεγονός και άλλες μετοχές τού παρακειμένου
            plural_form = noun[:-1] + 'τα'
            gen_form = noun[:-1] + 'τος'
            if plural_form in greek_corpus or gen_form in greek_corpus:
                noun_temp[NOM_PL] = plural_form
                noun_temp[GEN_SG] = gen_form
                noun_temp[GENDER] = NEUT
                neuter_os = True

        # in all other instances probably they are correct masculine words, but don't occur in the corpus, still for
        # proper name don't add plural if it doesn't exist in the corpus
        if not neuter_os and (not gens_sg or len(noun_temp[NOM_PL]) == 0):
            stem = noun[:-2]
            plural_form = stem + 'οι'
            if not gens_sg:
                gen_form = stem + 'ου'
                gen_form = put_accent(gen_form, PENULTIMATE, true_syllabification=False)
                if accent == ULTIMATE:
                    gen_form = stem + 'ού'
                noun_temp[GEN_SG] = gen_form

            if accent == ULTIMATE:
                plural_form = stem + 'οί'
            noun_temp[NOM_PL] = plural_form

            noun_temp[GENDER] = MASC

    elif noun.endswith('άκιας') or noun.endswith('άγιας'):
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        noun_temp[NOM_PL] = noun[:-3] + 'ηδες'
        if noun[:-2] + 'ες' in greek_corpus:
            noun_temp[NOM_PL] = f"{noun[:-3] + 'ηδες'},{noun[:-2] + 'ες'}"
        else:
            noun_temp[NOM_PL] = noun[:-3] + 'ηδες'

    elif gender != NEUT and noun.endswith('ας') and put_accent_on_the_penultimate(noun[:-1] + 'δες') in greek_corpus:

        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        if noun[:-2] + 'ες' in greek_corpus:
            noun_temp[NOM_PL] = f"{put_accent_on_the_penultimate(noun[:-1] + 'δες')},{noun[:-2] + 'ες'}"
        else:
            noun_temp[NOM_PL] = put_accent_on_the_penultimate(noun[:-1] + 'δες')

    elif gender != NEUT and noun.endswith('ας') and noun[:-2] + 'ηδες' in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        if noun[:-2] + 'ες' in greek_corpus:
            noun_temp[NOM_PL] = f"{noun[:-2] + 'ηδες'},{noun[:-2] + 'ες'}"
        else:
            noun_temp[NOM_PL] = noun[:-2] + 'ηδες'

    elif noun[-3:] in ['τής', 'της'] and put_accent_on_the_penultimate(noun[:-2] + 'άδες') in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        if put_accent(noun[:-2] + 'ες', accent) in greek_corpus:
            noun_temp[NOM_PL] = f"{put_accent_on_the_penultimate(noun[:-2] + 'άδες')},{put_accent(noun[:-2] + 'ές', accent)}"
        else:
            noun_temp[NOM_PL] = put_accent_on_the_penultimate(noun[:-2] + 'άδες')

    elif (accent == ANTEPENULTIMATE and noun.endswith('ης') and
          put_accent_on_the_penultimate(noun[:-2] + 'εις') in greek_corpus):
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = put_accent_on_the_antepenultimate(noun[:-2] + 'εως')
        noun_temp[NOM_PL] = put_accent_on_the_penultimate(noun[:-2] + 'εις')

    elif noun.endswith('ης') and noun[:-1] + 'δες' in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]

        if noun[:-2] + 'ες' in greek_corpus:
            noun_temp[NOM_PL] = f"{noun[:-1] + 'δες'},{noun[:-2] + 'ες'}"

        elif accent == PENULTIMATE and put_accent_on_the_penultimate(noun[:-2] + 'αιοι', true_syllabification=False) in greek_corpus:
            noun_temp[NOM_PL] = f"{noun[:-1] + 'δες'},{put_accent_on_the_penultimate(noun[:-2] + 'αιοι', true_syllabification=False)}"

        elif accent == PENULTIMATE and put_accent_on_the_penultimate(noun[:-2] + 'αραιοι',
                                                                     true_syllabification=False) in greek_corpus:
            noun_temp[NOM_PL] = f"{noun[:-1] + 'δες'},{put_accent_on_the_penultimate(noun[:-2] + 'αραιοι', true_syllabification=False)}"

        else:
            noun_temp[NOM_PL] = noun[:-1] + 'δες'

    elif accent == ANTEPENULTIMATE and noun.endswith('ης') and put_accent(noun[:-1] + 'δες', accent) in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        noun_temp[NOM_PL] = put_accent(noun[:-1] + 'δες', accent)
        if noun.endswith('ρης') and put_accent_on_the_penultimate(noun[:-2] + 'αιοι', False) in greek_corpus:
            noun_temp[NOM_PL] = put_accent(noun[:-1] + 'δες', accent) + ',' + put_accent_on_the_penultimate(noun[:-2] + 'αιοι', False)

    elif accent == ANTEPENULTIMATE and noun.endswith('ης') and noun[:-2] + 'ες' not in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        noun_temp[NOM_PL] = put_accent(noun[:-1] + 'δες', PENULTIMATE)

    elif noun.endswith('ούς') and noun[:-1] + 'δες' in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        # if noun[:-1] + 'δες' in greek_corpus:
        noun_temp[NOM_PL] = noun[:-1] + 'δες'

    elif noun.endswith('ους') and put_accent_on_the_penultimate(noun[:-1] + 'δες') in greek_corpus:
        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        # if noun[:-1] + 'δες' in greek_corpus:
        noun_temp[NOM_PL] = put_accent_on_the_penultimate(noun[:-1] + 'δες')

    elif gender != NEUT and noun[-1] == 'ς' and \
            ((noun[:-1] + 'δες' in greek_corpus) or (put_accent_on_the_antepenultimate(noun[:-1] + 'δες') in
                                                     greek_corpus)) and noun[-2:] != 'ις':
        # imparisyllaba on des, archaic and modern

        noun_temp[GENDER] = MASC
        noun_temp[GEN_SG] = noun[:-1]
        plurals = []
        plural_form = noun[:-1] + 'δες'

        # sometimes the accent has to be moved, and sometimes there are alternatives
        plural_form_a = put_accent_on_the_antepenultimate(plural_form)
        plural_form_b = put_accent_on_the_penultimate(plural_form)

        if plural_form in greek_corpus:
            plurals.append(plural_form)
        if plural_form_a in greek_corpus:
            plurals.append(plural_form_a)
        if plural_form_b in greek_corpus:
            plurals.append(plural_form_b)
        plurals = list(set(plurals))
        noun_temp[NOM_PL] = ','.join(plurals)
        gen_form = noun[:-1]
        gen_form_a = put_accent_on_the_penultimate(gen_form)
        gen_form_arch = noun[:-1] + 'δος'
        if count_syllables(noun) == 1:
            gen_form_arch = put_accent_on_the_ultimate(gen_form_arch)

        gens = []
        if gen_form in greek_corpus:
            gens.append(gen_form)
        if gen_form_a in greek_corpus:
            gens.append(gen_form_a)
        if gen_form_arch in greek_corpus:
            gens.append(gen_form_arch)
        gens = list(set(gens))
        noun_temp[GEN_SG] = ','.join(gens)
        if not noun_temp[GEN_SG]:
            noun_temp[GEN_SG] = gen_form_arch

    elif noun[-2:] in ['ές', 'ες']:

        # they can be either pluralia tantum or masc on es that do not have plur in the corpus or neuter on es or aklito
        if gender != NEUT and noun[:-1] in greek_corpus or noun[:-1].capitalize() in greek_corpus:
            # this means its a gen. of a masc form
            noun_temp[GENDER] = MASC
            noun_temp[GEN_SG] = noun[:-1]

            nom_pl = noun[:-1] + 'δες'
            if nom_pl not in greek_corpus:

                nom_pl_alt = put_accent(noun[:-2] + 'ηδες', ANTEPENULTIMATE)

                if nom_pl_alt in greek_corpus:
                    nom_pl = nom_pl_alt
            noun_temp[NOM_PL] = nom_pl

        elif put_accent(noun[:-2] + 'ους', accent) in greek_corpus or (gender == NEUT and not aklito):
            noun_temp[GEN_SG] = put_accent(noun[:-2] + 'ους', accent)
            noun_temp[NOM_PL] = put_accent(noun[:-2] + 'η', accent)
            noun_temp[GENDER] = NEUT

        elif (put_accent(noun[:-2] + 'ων', accent) in greek_corpus or put_accent(noun[:-2] + 'ών', ULTIMATE) in greek_corpus
              or put_accent(noun[:-2] + 'ων', accent).lower() in greek_corpus or noun in ['προάλλες', 'πρόποδες']):

            noun_temp[GENDER] = FEM
            if noun in ['πρόποδες', 'χοιράδες']:
                noun_temp[GENDER] = MASC
            noun_temp[GEN_SG] = ''
            noun_temp[NOM_PL] = noun
            noun_temp[NOM_SG] = ''

        else:
            # should be neuter aklita
            noun_temp[GENDER] = NEUT
            noun_temp[GEN_SG] = noun
            noun_temp[NOM_PL] = noun
            noun_temp[NOM_SG] = noun

    elif noun[-2:] in ['άς', 'ής', 'ας', 'ης'] and gender != NEUT:

        noun_temp[GENDER] = MASC
        # es
        plural_form_a = noun[:-2] + 'ες'
        gen_form_a = noun[:-1]
        if ultimate_accent:
            plural_form_a = noun[:-2] + 'ές'
        # eas - eis,
        plural_form_b = noun[:-3] + 'είς'
        gen_form_b = noun[:-1]
        # hs, eis
        plural_form_ba = noun[:-2] + 'είς'
        gen_form_ba = noun[:-2] + 'ούς'
        # hs, eis
        plural_form_bb = noun[:-2] + 'εις'
        gen_form_bb = noun[:-2] + 'εως'
        # ancient forms
        plural_form_c = noun[:-1] + 'τες'
        plural_form_d = noun[:-1] + 'δες'
        plural_form_c_neut = noun[:-1] + 'τα'
        gen_form_c = noun[:-1] + 'τος'
        gen_form_d = noun[:-1] + 'δος'
        if accent != ULTIMATE:
            plural_form_c = put_accent_on_the_antepenultimate(plural_form_c, true_syllabification=False)
            plural_form_c_neut = put_accent_on_the_antepenultimate(plural_form_c_neut, true_syllabification=False)
            gen_form_c = put_accent_on_the_antepenultimate(gen_form_c, true_syllabification=False)

        if plural_form_c in greek_corpus and gen_form_c in greek_corpus:
            nom_pl = plural_form_c
            gen_sg = gen_form_c
            # but there is possible, that there is also more dimotiki form of gen_sg
            if gen_form_a in greek_corpus:
                gen_sg = gen_form_c + ',' + gen_form_a

        elif gen_form_d in greek_corpus:
            nom_pl = plural_form_d
            gen_sg = gen_form_d

        elif noun.endswith('παπας'):
            nom_pl = put_accent_on_the_penultimate(noun[:-1] + 'δες')
            gen_sg = noun[:-1]

        elif (plural_form_b in greek_corpus and gen_form_b in greek_corpus) and noun[-3:] not in ['ίας']:
            # the last condition is to exclude possibility, that it is false positive because of some same sounding
            # fut aorist forms
            nom_pl = plural_form_b
            gen_sg = gen_form_b

        elif plural_form_ba in greek_corpus and gen_form_ba in greek_corpus:
            nom_pl = plural_form_ba
            gen_sg = gen_form_ba

        elif plural_form_bb in greek_corpus and gen_form_bb[:-1] + 'ν' in greek_corpus:
            nom_pl = plural_form_bb
            gen_sg = gen_form_bb

        elif plural_form_a in greek_corpus:

            nom_pl = plural_form_a
            if accent == ANTEPENULTIMATE:
                plural_form_oi = put_accent_on_the_penultimate(noun[:-2] + 'οι')
                if plural_form_oi in greek_corpus and plural_form_a in greek_corpus:
                    nom_pl = nom_pl + ',' + plural_form_oi
            gen_sg = gen_form_a

        elif plural_form_c_neut in greek_corpus and gen_form_c in greek_corpus:
            nom_pl = plural_form_c_neut
            gen_sg = gen_form_c
            noun_temp[GENDER] = NEUT

        elif noun[-2:] == 'άς':
            # if corpus doesnt help, more probable is that ending in as is imparisyllaba
            nom_pl = noun[:-1] + 'δες'
            gen_sg = gen_form_a

        elif noun.endswith('έας'):
            nom_pl = plural_form_b
            gen_sg = gen_form_a
            if gender == MASC_FEM:
                gen_sg = noun[:-3] + 'έως'
            if proper_name and nom_pl not in greek_corpus:
                nom_pl = ''


        else:
            nom_pl = plural_form_a
            gen_sg = gen_form_a

        # if nom_pl:
        noun_temp[NOM_PL] = nom_pl
        noun_temp[GEN_SG] = gen_sg

    elif noun[-3:] in ['εύς', 'ευς']:

        plural_form = noun[:-3] + 'είς'
        gen_form = noun[:-3] + 'έως'
        noun_temp[GENDER] = MASC
        if not aklito or plural_form in greek_corpus or gen_form in greek_corpus:
            if not proper_name:
                noun_temp[NOM_PL] = plural_form
            noun_temp[GEN_SG] = gen_form
        if noun == 'Ζευς':
            noun_temp[GEN_SG] = 'Διός,Δίος'
            noun_temp[NOM_PL] = ''

    elif noun.endswith('εις'):
        # pluralia tantum eis ewn
        noun_temp[GENDER] = FEM
        noun_temp[NOM_PL] = noun
        noun_temp[NOM_SG] = ''
        noun_temp[GEN_SG] = ''

    elif noun.endswith('είς'):
        # pluralia tantum eis ewn
        noun_temp[GENDER] = MASC
        noun_temp[NOM_PL] = noun
        noun_temp[NOM_SG] = ''
        noun_temp[GEN_SG] = ''

    elif noun[-3:] in ['ους', 'ούς'] and not aklito:
        if 'πλους' in noun or 'νους' in noun and noun != 'μπόνους':
            noun_temp[GENDER] = MASC
            noun_temp[GEN_SG] = noun[:-1]
            if noun[:-3] + 'οι' in greek_corpus:
                noun_temp[NOM_PL] = noun[:-3] + 'οι'
        elif 'πους' in noun:
            noun_temp[GENDER] = MASC
            noun_temp[GEN_SG] = noun[:-3] + 'οδος'
            noun_temp[NOM_PL] = noun[:-3] + 'οδες'
            if noun == 'πους':
                noun_temp[GEN_SG] = 'ποδός'
                noun_temp[NOM_PL] = 'πόδες'
        elif noun == 'ους':
            # το αυτί χρειάζεται να είναι μόνο του
            noun_temp[GENDER] = NEUT
            noun_temp[GEN_SG] = 'ωτός'
            noun_temp[NOM_PL] = 'ώτα'
        elif proper_name and gender == MASC:
            noun_temp[GEN_SG] = noun[:-1]

        else:
            # aklita
            noun_temp[GENDER] = NEUT
            noun_temp[GEN_SG] = noun
            noun_temp[NOM_PL] = noun

    elif noun[-2:] in ['υς', 'ύς'] and noun[-3] not in vowels:
        # archaic, either eis ews, or es, os

        pl_eis = put_accent_on_the_penultimate(noun[:-2] + 'εις')
        pl_es = noun[:-1] + 'ες'
        if pl_eis in greek_corpus:
            noun_temp[GEN_SG] = put_accent_on_the_antepenultimate(noun[:-2] + 'εως')
            noun_temp[NOM_PL] = pl_eis
        else:
            noun_temp[NOM_PL] = pl_es
            noun_temp[GEN_SG] = noun[:-1] + 'ος'
        if not gender:
            gender = MASC
    elif noun[-1] in ['α', 'η', 'ά', 'ή']:
        # feminina
        noun_temp[GENDER] = FEM
        gen_a = noun + 'ς'
        noun_temp[GEN_SG] = gen_a
        plural_form_a = put_accent(noun[:-1] + 'ες', accent, true_syllabification=False)

        plural_form_b = put_accent_on_the_penultimate(noun[:-1] + 'εις', true_syllabification=False)

        # imparisyllaba

        plural_form_c = noun + 'δες'
        plural_form_d = put_accent_on_the_penultimate(noun[:-1] + 'αδες')

        if plural_form_c in greek_corpus:

            if plural_form_a in greek_corpus and not noun.endswith('μά'):
                noun_temp[NOM_PL] = plural_form_c + ',' + plural_form_a
            else:
                noun_temp[NOM_PL] = plural_form_c

        elif plural_form_d in greek_corpus and not noun.endswith('α'):
            if plural_form_a in greek_corpus:
                noun_temp[NOM_PL] = plural_form_d + ',' + plural_form_a
            else:
                noun_temp[NOM_PL] = plural_form_d
        elif accent == PENULTIMATE and plural_form_a not in greek_corpus:
            plural_proparoxitona = put_accent_on_the_antepenultimate(plural_form_a)
            if plural_proparoxitona in greek_corpus:
                noun_temp[NOM_PL] = plural_proparoxitona
            else:
                noun_temp[NOM_PL] = plural_form_a
        elif plural_form_a not in ['γες']:
            # unfortunately for some very short words it can fail, ad hoc solution is to implement some kind of a list
            noun_temp[NOM_PL] = plural_form_a

        # special case for neuter on ma
        if noun[-2:] == 'μα' and (gender == NEUT or (plural_form_a not in greek_corpus and
                                  plural_form_b not in greek_corpus and
                                  plural_form_c not in greek_corpus) or
                                  put_accent_on_the_antepenultimate(noun + 'τα',
                                                                    true_syllabification=False) in greek_corpus):
            plural_form = put_accent_on_the_antepenultimate(noun + 'τα', true_syllabification=False)
            gen_form = put_accent_on_the_antepenultimate(noun + 'τος', true_syllabification=False)
            noun_temp[NOM_PL] = plural_form
            noun_temp[GEN_SG] = gen_form
            noun_temp[GENDER] = NEUT
        # elif noun[-1] == 'α' and (gender == NEUT or (noun + 'τος' in greek_corpus and noun + 'τα' in greek_corpus)):
        #     # gala, galatos
        #
        #     noun_temp[NOM_SG] = noun
        #     noun_temp[NOM_PL] = put_accent_on_the_antepenultimate(noun + 'τα')
        #     noun_temp[GEN_SG] = put_accent_on_the_antepenultimate(noun + 'τος')
        #     noun_temp[GENDER] = NEUT
        #     if 'γάλα' in noun:
        #         noun_temp[NOM_PL] = noun + 'τα' + ',' + noun + 'κτα'
        #         noun_temp[GEN_SG] = noun + 'τος' + ',' + noun + 'κτος'

        if (noun[-1] in ['α', 'ά'] and (gender == NEUT_PL or (gen_a not in greek_corpus and plural_form_a not in greek_corpus
            and put_accent(noun[:-1] + 'ων', accent) in greek_corpus))):
            # maybe pluralia tantum
            noun_temp[NOM_SG] = ''
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = ''
            noun_temp[GENDER] = NEUT

        if noun in noun_grammar_lists[FEMININA_H_EIS] or noun[-2:] in ['ση', 'ξη', 'ψη']:
            # it has to be if, because it can be earlier falsly recognized as a correct form on es, because of som aorists
            # in sec person sg
            noun_temp[NOM_PL] = plural_form_b
            noun_temp[GEN_SG] = gen_a + ',' + put_accent_on_the_antepenultimate(noun[:-1] + 'εως',
                                                                                true_syllabification=False)

    elif noun[-2:] == 'ού':
        noun_temp[GENDER] = FEM
        noun_temp[GEN_SG] = noun + 'ς'
        plural_form = noun + 'δες'
        if plural_form in greek_corpus:
            noun_temp[NOM_PL] = plural_form

    elif noun[-1] in ['ό', 'ο']:
        if noun[-3:] == 'ιμο':
            plural_form = noun[:-1] + 'ατα'
            gen_form = noun[:-1] + 'ατος'
            plural_form = put_accent_on_the_antepenultimate(plural_form)
            gen_form = put_accent_on_the_penultimate(gen_form)
            if plural_form in greek_corpus or gen_form in greek_corpus:
                noun_temp[NOM_PL] = plural_form
                noun_temp[GEN_SG] = gen_form
                noun_temp[GENDER] = NEUT

                return noun_temp

        noun_temp[GENDER] = NEUT
        plural_form = noun[:-1] + 'α'
        gen_form = noun[:-1] + 'ου'
        if ultimate_accent:
            plural_form = noun[:-1] + 'ά'
            gen_form = noun[:-1] + 'ού'
        if plural_form in greek_corpus or \
                plural_form.capitalize() in greek_corpus or \
                number_of_syllables > 4 or \
                (gender not in [FEM, MASC] and not aklito):
            noun_temp[NOM_PL] = plural_form

        gens = []
        if gen_form in greek_corpus or \
                gen_form.capitalize() in greek_corpus or \
                number_of_syllables > 4:
            gens.append(gen_form)

        if accent == ANTEPENULTIMATE:
            gen_a = put_accent(gen_form, PENULTIMATE, true_syllabification=False)
            if gen_a in greek_corpus:
                gens.append(gen_a)

        if gens:
            noun_temp[GEN_SG] = ','.join(gens)
        elif gender not in [FEM, MASC] and not aklito:
            noun_temp[GEN_SG] = gen_form
        else:
            # σ`αυτήν την περίπτωση υποθέτουμε πως είναι ουδέτερα άκλιτα
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = noun
            noun_temp[GENDER] = NEUT

    elif not aklito and noun[-1] in ['ι', 'ί', 'ΐ'] and noun[-2:] not in ['οι', 'οί', 'αι', 'αί']:
        noun_temp[GENDER] = NEUT
        plural_form = noun + 'α'
        if noun in noun_grammar_lists[PAROKSITONA_GEN_NEUT_I]:
            gen_form = put_accent(noun + 'ου', PENULTIMATE, true_syllabification=False)

        else:
            gen_form = put_accent_on_the_ultimate(noun + 'ου')
        if accent == ULTIMATE:
            plural_form = put_accent_on_the_ultimate(plural_form)

        if plural_form[-3] in vowels:
            # if gen_form not in greek_corpus:
            plural_form = plural_form[:-2] + 'γι' + plural_form[-1]

            gen_form = gen_form[:-3] + 'γι' + gen_form[-2:]


        # in greek corpus there are lacking some upokoristika
        # if not aklito or plural_form in greek_corpus or noun[-3:] in ['άκι', 'ίκι', 'άρι', 'έκι', 'ήρι', 'ίδι', 'ύρι']:
        noun_temp[NOM_PL] = plural_form
        if noun not in noun_grammar_lists[WITHOUT_GEN_NEUT_I]:
            noun_temp[GEN_SG] = gen_form


    elif noun[-2:] in ['οι', 'οί']:
        # pluralis tantum masc
        noun_temp[GENDER] = MASC
        noun_temp[NOM_PL] = noun
        noun_temp[NOM_SG] = ''
        noun_temp[GEN_SG] = ''

    elif noun[-2:] in ['αι', 'αί'] and not aklito:
        # pluralis tantum fem
        noun_temp[GENDER] = FEM
        noun_temp[NOM_PL] = noun
        noun_temp[NOM_SG] = ''
        noun_temp[GEN_SG] = ''

    elif noun.endswith('ώς') and gender == FEM:
        noun_temp[GEN_SG] = noun[:-2] + 'ούς'

    elif noun[-1] in ['ξ', 'ψ', 'τ', 'ρ', 'β', 'ν', 'δ', 'ε', 'έ', 'ζ', 'κ', 'λ', 'μ', 'ς'] and not aklito:

        # not very common but existing 3rd declension nouns
        # gender would be a wild guess

        stems = []

        if noun[-1] == 'ξ':

            stems.append(noun[:-1] + 'κ')
            stems.append(noun[:-1] + 'χ')
            stems.append(noun[:-1] + 'κτ')
            stems.append(noun[:-1] + 'χτ')
            stems.append(noun[:-1] + 'γ')
            if not gender:
                """sometimes this guess won't work, and recreating the modern forms would be too expensive,
                so it is advisable, as in so many other cases, to feed the program with all possible data 
                (that is genders and aklito flag)"""
                gender = FEM
        elif noun.endswith('ωψ'):
            stems.append(noun[:-2] + 'οπ')
        elif noun[-1] == 'ψ':

            stems.append(noun[:-1] + 'π')
            stems.append(noun[:-1] + 'φ')
            stems.append(noun[:-1] + 'πτ')
            stems.append(noun[:-1] + 'β')
            stems.append(noun[:-1] + 'φτ')
            if not gender:
                gender = FEM
        elif noun[-1] == 'ρ':
            if not gender:
                gender = MASC
            stems.append(noun)
            stems.append(noun[:-1] + 'τ')
            if noun[-2:] == 'ωρ':
                stems.append(noun[:-2] + 'ορ')
                if 'μήτωρ' in noun:
                    gender = FEM
            elif noun[-2:] == 'ώρ':
                stems.append(noun[:-2] + 'όρ')
            else:
                noun_temp[GENDER] = NEUT

        elif noun.endswith('ώς'):
            if not gender:
                gender = NEUT
            # ουσιαστικοποιημένες αρχαίες μετοχες
            stems.append(noun[:-1] + 'τ')
            stems.append(noun[:-2] + 'ότ')
        elif noun.endswith('ις'):
            if not gender:
                gender = FEM
            stems.append(noun[:-1] + 'τ')
            stems.append(noun[:-1] + 'δ')
            stems.append(noun[:-1] + 'θ')
        elif noun.endswith('ς'):
            if not gender:
                gender = NEUT

            stems.append(noun[:-1] + 'τ')

        elif noun.endswith('ων'):
            stems.append(noun[:-2] + 'οντ')
            stems.append(noun[:-2] + 'ον')
            stems.append(noun)
            if not gender:
                gender = MASC
        elif noun.endswith('ών'):
            stems.append(noun)
            stems.append(noun[:-2] + 'όν')
            stems.append(noun[:-2] + 'όντ')
            stems.append(noun[:-2] + 'ούντ')
            stems.append(noun[:-2] + 'ώντ')
            if not gender:
                gender = MASC
        elif noun[-1] == 'ν':
            stems.append(noun + 'τ')
            stems.append(noun)
            if not gender:
                gender = NEUT
        third_declesion_thema = ''

        if noun in irregular_3rd_decl_roots.keys():
            third_declesion_thema = irregular_3rd_decl_roots[noun]

        else:
            for stem in stems:

                plural_form = stem + 'ες'
                modern_form = stem + 'ας'
                plural_form_n = stem + 'α'
                gen_form = stem + 'ος'
                if number_of_syllables == 1:
                    plural_form = put_accent_on_the_penultimate(stem + 'ες')
                    modern_form = put_accent_on_the_penultimate(stem + 'ας')
                    plural_form_n = put_accent_on_the_penultimate(stem + 'α')
                    gen_form = put_accent_on_the_ultimate(stem + 'ος')
                if accent == ANTEPENULTIMATE:
                    plural_form = put_accent_on_the_antepenultimate(stem + 'ες')
                    modern_form = put_accent_on_the_antepenultimate(stem + 'ας')
                    plural_form_n = put_accent_on_the_antepenultimate(stem + 'α')
                    gen_form = put_accent_on_the_antepenultimate(stem + 'ος')
                if plural_form in greek_corpus or modern_form in greek_corpus or plural_form_n in greek_corpus or gen_form in greek_corpus:
                    third_declesion_thema = stem
                    break

        if third_declesion_thema:
            third_declesion_thema.replace('χτ', 'κτ')

            if number_of_syllables == 1:
                noun_temp[GEN_SG] = put_accent_on_the_ultimate(third_declesion_thema + 'ος')
                if gender == NEUT:
                    noun_temp[NOM_PL] = put_accent_on_the_penultimate(third_declesion_thema + 'α')
                else:
                    noun_temp[NOM_PL] = put_accent_on_the_penultimate(third_declesion_thema + 'ες')
            elif accent == ANTEPENULTIMATE:
                noun_temp[GEN_SG] = put_accent_on_the_antepenultimate(third_declesion_thema + 'ος')
                if gender == NEUT:
                    noun_temp[NOM_PL] = put_accent_on_the_antepenultimate(third_declesion_thema + 'α')
                else:
                    noun_temp[NOM_PL] = put_accent_on_the_antepenultimate(third_declesion_thema + 'ες')
            else:
                noun_temp[GEN_SG] = third_declesion_thema + 'ος'

                if gender == NEUT:
                    noun_temp[NOM_PL] = third_declesion_thema + 'α'
                else:
                    noun_temp[NOM_PL] = third_declesion_thema + 'ες'

        # elif noun.endswith('ων') and not aklito:
            #probably the best guess is still third declension
        elif noun.endswith('ις'):
            gen_form_ews = noun[:-2] + 'εως'
            plural_form_eis = put_accent_on_the_penultimate(noun[:-2] + 'εις', true_syllabification=False)
            # if gen_form_ews in greek_corpus or plural_form_eis in greek_corpus:
            noun_temp[NOM_PL] = plural_form_eis
            noun_temp[GEN_SG] = gen_form_ews

        elif noun.endswith('όν') or noun.endswith('ον'):

            # maybe 2nd declesion archaic
            plural_form = put_accent(noun[:-2] + 'α', accent)

            if accent == ANTEPENULTIMATE:
                gen_form = put_accent(noun[:-2] + 'ού', PENULTIMATE)
            else:
                gen_form = put_accent(noun[:-2] + 'ού', accent)
            if gen_form in greek_corpus:
                noun_temp[GENDER] = NEUT
                noun_temp[NOM_PL] = plural_form
                noun_temp[GEN_SG] = gen_form

        else:

            noun_temp[GENDER] = NEUT
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = noun

    elif noun[-1] in ['ώ', 'ω']:

        if noun in ['ηχώ', 'πειθώ', 'φειδώ', 'βάβω']:
            # ancient feminina
            noun_temp[GENDER] = FEM

            noun_temp[GEN_SG] = noun[:-1] + 'ούς,' + noun + 'ς'
            if noun in ['βάβω']:
                noun_temp[GEN_SG] = noun
        elif proper_name or gender == FEM:
            # feminine proper name
            noun_temp[GENDER] = FEM
            noun_temp[GEN_SG] = noun + 'ς'

            noun_temp[NOM_PL] = noun[:-1] + 'ες'

        else:
            noun_temp[GENDER] = NEUT
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = noun

    elif noun.endswith('υ') and gender == FEM:
        noun_temp[GEN_SG] = noun + 'ς'

    elif noun[-1] in ['υ', 'ύ']:
        # bradu braduou or ancient 3rd declension, oksy , asty
        noun_temp[GENDER] = NEUT
        if noun in irregular_3rd_decl_roots:
            root = irregular_3rd_decl_roots[noun]
            noun_temp[NOM_PL] = root + 'α'
            noun_temp[GEN_SG] = root + 'ος'
        elif noun[-2:] in ['ου', 'ού']:
            noun_temp[NOM_PL] = noun

            if gender == FEM:
                noun_temp[GEN_SG] = noun + 'ς'
            else:
                noun_temp[GEN_SG] = noun
        elif noun[-1] == 'υ':
            gen_1 = noun + 'ου'
            gen_1b = put_accent_on_the_penultimate(gen_1)
            gen_2 = noun + 'ος'
            plural = noun + 'α'

            if gen_1 in greek_corpus:
                noun_temp[GEN_SG] = gen_1
            elif gen_1b in greek_corpus:
                noun_temp[GEN_SG] = gen_1b
            elif gen_2 in greek_corpus:
                noun_temp[GEN_SG] = gen_2
            if plural in greek_corpus:
                noun_temp[NOM_PL] = plural

    if aklito:
        # aklita

        noun_temp[GENDER] = NEUT
        noun_temp[NOM_PL] = noun
        noun_temp[GEN_SG] = noun

    if gender:

        noun_temp[GENDER] = gender
        # for pluralia tantum
        if gender == FEM_PL:
            noun_temp[GENDER] = FEM
            noun_temp[NOM_SG] = ''
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = ''
        elif gender == MASC_PL:
            noun_temp[GENDER] = MASC
            noun_temp[NOM_SG] = ''
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = ''

        elif gender == NEUT_PL:
            noun_temp[GENDER] = NEUT
            noun_temp[NOM_SG] = ''
            noun_temp[NOM_PL] = noun
            noun_temp[GEN_SG] = ''

    """
    check one more time these, that do not have flag aklito, but are surmised to be, maybe removing a prefix we will
    # be able to find out the correct declension type
    """
    if not aklito and proper_name and gender != SURNAME and noun_temp[NOM_PL] == noun_temp[NOM_SG]:
        # maybe changing to lower case can help
        noun_temp = capitalize_basic_forms(create_all_basic_noun_forms(noun.lower()))

    if not aklito and noun_temp[NOM_PL] == noun_temp[NOM_SG]:
        for prefix in prefixes:
            pr_l = len(prefix)
            if prefix in noun and prefix == noun[:pr_l]:
                res = create_all_basic_noun_forms(noun[pr_l:])
                new_res = {}
                for key in res.keys():
                    if key != GENDER:
                        new_res[key] = prefix + res[key]
                new_res[GENDER] = res[GENDER]
                noun_temp = new_res
                break

    # if capital:
    #     noun_temp = capitalize_basic_forms(noun_temp)
    if only_sg:
        noun_temp[NOM_PL] = ''
    return noun_temp


def capitalize_basic_forms(noun_temp: dict) -> dict:
    for key in noun_temp:
        if key != GENDER:
            noun_temp[key] = ','.join([f.capitalize() for f in noun_temp[key].split(',')])
    return noun_temp
