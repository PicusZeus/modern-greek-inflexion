from modern_greek_accentuation.accentuation import where_is_accent, put_accent, count_syllables, remove_all_diacritics
from modern_greek_accentuation.resources import PENULTIMATE, ULTIMATE, ANTEPENULTIMATE
from ..resources import greek_corpus, SG, PL, NOM, GEN, ACC, VOC, MASC, FEM, NEUT


def put_accent_on_unaccented_forms(forms):
    # one syllable words
    for number in forms.keys():
        for case in forms[number].keys():
            f = forms[number][case]
            if not where_is_accent(f) and count_syllables(f) > 1:
                forms[number][case] = put_accent(f, PENULTIMATE)
    return forms


def create_all_noun_forms(nom_sg, gen_sg, nom_pl, genders, proper_name=False):
    """
    :param nom_sg: nominative singular
    :param gen_sg: genitive singular
    :param nom_pl: nominative plural
    :param genders: FEM or MASC or NEUT, if more than one, than separated with ','
    :param proper_name: flag useful for creation of vocatives in proper names
    :return: tuple with 3 elements: forms in all cases in dictionary, gender, and alternative forms in dictionary, if exist
    I want to include alternatives in a main dictionary of forms by adding them with a coma separator
    """
    accent = where_is_accent(nom_sg, true_syllabification=False)
    noun_all = {}

    if ',' in nom_pl:
        # irregular plural maybe
        plurals = nom_pl.split(',')
        if (plurals[0][-2:] in ['οι', 'οί'] or not plurals[0]) and plurals[1][-1] in ['α', 'ά', 'ή', 'η']:
            genders = genders + ',neut_irregular'
            nom_pl = plurals[0]
            irregular_nom_pl = plurals[1]
    for gender in genders.split(','):

        if gender == 'neut_irregular':
            # they lack gen pl
            noun_all[NEUT] = {}
            noun_all[NEUT][PL] = {}
            noun_all[NEUT][PL][NOM] = irregular_nom_pl
            noun_all[NEUT][PL][ACC] = irregular_nom_pl
            noun_all[NEUT][PL][VOC] = irregular_nom_pl

            accent = where_is_accent(irregular_nom_pl)
            gen_pl = irregular_nom_pl[:-1] + 'ων'
            if irregular_nom_pl[-1] == 'η':
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

            noun_all[gender] = {}
            noun_all[gender][SG] = {}
            noun_all[gender][PL] = {}
            noun_all[gender][SG][NOM] = nom_sg
            noun_all[gender][SG][GEN] = gen_sg
            noun_all[gender][SG][VOC] = nom_sg
            noun_all[gender][PL][NOM] = nom_pl
            noun_all[gender][PL][ACC] = nom_pl
            noun_all[gender][PL][VOC] = nom_pl

            if gender in [FEM, NEUT]:
                noun_all[gender][SG][ACC] = nom_sg
                noun_all[gender][PL][ACC] = nom_pl

            elif gender == MASC and nom_sg == gen_sg:
                noun_all[gender][SG][ACC] = nom_sg

            if nom_sg[-2:] in ['ος', 'ός'] and gen_sg[-2:] in ['ου', 'ού']:

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

                if nom_pl:
                    gens = gen_sg.split(',')
                    accent_pl = where_is_accent(nom_pl, true_syllabification=False)
                    if accent_pl == ANTEPENULTIMATE and (len(gens) > 1 or
                                                         where_is_accent(gen_sg,
                                                                         true_syllabification=False) == PENULTIMATE):
                        gen_pl = put_accent(nom_pl[:-2] + 'ων', PENULTIMATE, true_syllabification=False)
                    else:
                        gen_pl = put_accent(nom_pl[:-2] + 'ων', accent_pl, true_syllabification=False)

                    acc_pl = [put_accent(g[:-2] + 'ους', where_is_accent(g, true_syllabification=False),
                                         true_syllabification=False) for g in gens]
                    acc_pl = ','.join(acc_pl)

                    noun_all[gender][PL][GEN] = gen_pl
                    noun_all[gender][PL][ACC] = acc_pl

            elif nom_sg[-1:] == 'ς' and nom_pl and nom_pl[-2:] in ['ές', 'ες'] and gen_sg and \
                    gen_sg == nom_sg[:-1]:

                g_pl = []

                for n_pl in nom_pl.split(','):

                    pl_accent = where_is_accent(n_pl, true_syllabification=False)
                    gen_pl = nom_pl[:-2] + 'ων'
                    if count_syllables(nom_sg) == count_syllables(nom_pl) and (nom_sg[-2:] in ['ης', 'ής', 'ας', 'άς']):
                        gen_pl = put_accent(gen_pl, ULTIMATE)
                        if (nom_sg[-2:] == 'ας' and count_syllables(nom_sg) > 2) and nom_sg[-3:] != 'ίας':
                            gen_pl = put_accent(gen_pl, PENULTIMATE, true_syllabification=False)
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

            elif nom_sg[-1:] in ['α', 'ά', 'ή', 'η'] and gen_sg[-1:] == 'ς' and gender != NEUT:

                noun_all[gender][SG][ACC] = nom_sg

                gen_pl = ''
                if nom_pl:
                    if nom_pl[-2:] in ['ες', 'ές'] and count_syllables(nom_sg) == count_syllables(nom_pl):
                        gen_pl = nom_pl[:-2] + 'ων'
                        gen_pl = put_accent(gen_pl, ULTIMATE)
                        if nom_sg[-3:] in ['ίδα', 'άδα', 'ητα']:
                            gen_pl = put_accent(gen_pl, PENULTIMATE)
                        if gen_pl not in greek_corpus:
                            alt_gen_pl = put_accent(gen_pl, PENULTIMATE)
                            alt_gen_pl_b = put_accent(gen_pl, ANTEPENULTIMATE)
                            if alt_gen_pl in greek_corpus:
                                gen_pl = alt_gen_pl
                            elif alt_gen_pl_b in greek_corpus:
                                gen_pl = alt_gen_pl
                            else:
                                gen_pl = ''
                    elif nom_pl[-3:] == 'εις':
                        gen_pl = nom_pl[:-3] + 'εων'
                    else:
                        pl_accent = where_is_accent(nom_pl, true_syllabification=False)
                        gen_pl_alt = nom_pl[:-2] + 'ων'
                        gen_pl_alt = put_accent(gen_pl_alt, pl_accent, true_syllabification=False)
                        if gen_pl_alt in greek_corpus:
                            gen_pl = gen_pl_alt

                noun_all[gender][PL][GEN] = gen_pl

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

                    if gen_pl not in greek_corpus:
                        gen_pl_alt = put_accent(gen_pl, PENULTIMATE)
                        if gen_pl_alt in greek_corpus:
                            gen_pl = gen_pl_alt
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

                if gender == FEM:
                    noun_all[gender][SG][GEN] = gen_sg + ',' + nom_sg[:-2] + 'ως'
                noun_all[gender][SG][ACC] = nom_sg[:-1]
                noun_all[gender][SG][VOC] = nom_sg[:-1]

                gen_pl = ''
                if nom_pl:
                    gen_pl = nom_sg[:-2] + 'ων'
                noun_all[gender][PL][GEN] = gen_pl

            elif gen_sg[-3:] == 'εως' and nom_sg[-1] == 'ς':
                acc_sg_arch = nom_sg[:-1] + 'ν'
                if nom_sg[-2:] == 'ις':
                    noun_all[gender][SG][GEN] = gen_sg
                    noun_all[gender][SG][ACC] = acc_sg_arch
                else:
                    noun_all[gender][SG][GEN] = gen_sg + ',' + nom_sg[:-1]
                    if acc_sg_arch in greek_corpus:
                        noun_all[gender][SG][ACC] = acc_sg_arch + nom_sg[:-1]
                    else:
                        noun_all[gender][SG][ACC] = nom_sg[:-1]
                noun_all[gender][SG][VOC] = nom_sg[:-1]
                noun_all[gender][PL][GEN] = gen_sg[:-1] + 'ν'

            elif nom_sg == nom_pl:
                # aklita
                noun_all[gender][SG][ACC] = nom_sg
                noun_all[gender][PL][GEN] = nom_pl

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

            elif not nom_sg and (nom_pl[-2:] in ['ες', 'οι', 'ές', 'οί'] or nom_pl[-1:] in ['α', 'η', 'ά', 'ή']):

                if nom_pl[-2:] in ['οι', 'οί']:
                    accent = where_is_accent(nom_pl, true_syllabification=False)
                    acc_pl = put_accent(nom_pl[:-2] + 'ους', accent, true_syllabification=False)

                    if accent == ANTEPENULTIMATE:
                        acc_pl_alt = put_accent(acc_pl, PENULTIMATE, true_syllabification=False)
                        if acc_pl in greek_corpus and acc_pl_alt in greek_corpus:
                            acc_pl = acc_pl + ',' + acc_pl_alt
                        elif acc_pl_alt in greek_corpus:
                            acc_pl = acc_pl_alt

                    noun_all[gender][PL][ACC] = acc_pl

                thema = nom_pl[:-2]
                if nom_pl[-1] in ['α', 'η', 'ά', 'ή']:
                    thema = nom_pl[:-1]

                accent = where_is_accent(nom_pl, true_syllabification=False)
                gen_pl = put_accent(thema + 'ων', accent, true_syllabification=False)

                if nom_pl[-1] in ['η', 'ή']:
                    gen_pl = put_accent(gen_pl, ULTIMATE)

                if accent == ANTEPENULTIMATE:
                    gen_pl_alt = put_accent(gen_pl, PENULTIMATE, true_syllabification=False)
                    if gen_pl in greek_corpus and gen_pl_alt in greek_corpus:
                        gen_pl = gen_pl + ',' + gen_pl_alt
                    elif gen_pl not in greek_corpus:
                        gen_pl = gen_pl_alt

                if nom_pl[-2:] in ['ες', 'ές']:
                    if nom_pl[-4:-2] not in ['άδ', 'ήτ']:
                        gen_pl = put_accent(gen_pl, ULTIMATE)

                noun_all[gender][PL][GEN] = gen_pl

            """
            irregularities
            """
            if nom_sg == 'χρόνος':
                noun_all[gender][PL][GEN] = 'χρόνων,χρονών,χρόνω,χρονώ'

    return noun_all
