import pickle


from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate,\
    put_accent_on_the_antepenultimate, is_accented, put_accent_on_the_ultimate, count_syllables, remove_all_diacritics, \
    put_accent, remove_diaer, modern_greek_syllabify
from modern_greek_accentuation.resources import vowels
from resources import feminine_os, feminine_h_eis, feminine_or_masc, plur_tant_neut



file = open('el_GR.pickle', 'br')
greek_corpus = pickle.load(file)
file.close()


def create_all_basic_noun_forms(noun, proper_name=False, proper_name_gender=False):
    """

    :param noun: must be nom sg
    :return: dictionary with keys: nom_sg, gen_sg, nom_pl and gender. Alternative forms are divided with coma
    """
    # I need nom sg, nom. pl. gender
    noun_temp ={'nom_sg': noun, 'gen_sg': '', 'nom_pl': '', 'gender': ''}
    number_of_syllables = count_syllables(noun, true_syllabification=False)
    accent = where_is_accent(noun, true_syllabification=False)
    ultimate_accent = accent == 'ultimate'

    capital = noun[0].isupper()
    noun = noun.lower()
    # on 'os'

    if noun[-2:] in ['ός', 'ος']:
        stem = noun[:-2]
        plural_form = put_accent(stem + 'οι', accent, true_syllabification=False)
        gen_form = put_accent(stem + 'ου', accent, true_syllabification=False)
        if remove_diaer(plural_form) == put_accent(stem + 'οι', accent):
            plural_form = remove_diaer(plural_form)
        print(remove_diaer(gen_form),  stem + 'ου', modern_greek_syllabify(stem + 'ου'), put_accent(stem + 'ου', accent), accent, stem, 'ηερε')
        if remove_diaer(gen_form) == put_accent(stem + 'ου', accent):
            print('baiou')

            gen_form = remove_diaer(gen_form)

        gens_sg = []

        noun_temp['gender'] = 'masc'

        # the problem is that many long words on -os that are part of some kind of jargon do not have any other form
        # declined in the lexicon, i will assume then that words above 4 syllabes do exist, but only in singular, the
        # same should be the case for neuter long words on -o
        # also some proper names in greek_corpus are, as is proper, capitalized
        if gen_form in greek_corpus or gen_form.capitalize() in greek_corpus or number_of_syllables >4:
            gens_sg.append(gen_form)

        if accent == 'antepenultimate':
            gen_form_alt = put_accent(gen_form, 'penultimate', true_syllabification=False)
            if gen_form_alt in greek_corpus:
                gens_sg.append(gen_form_alt)

        noun_temp['gen_sg'] = ','.join(gens_sg)

        if plural_form in greek_corpus or plural_form.capitalize() in greek_corpus or number_of_syllables > 4:
            noun_temp['nom_pl'] = plural_form
            if not gens_sg:
                noun_temp['gen_sg'] = gen_form

        if noun in feminine_os:
            noun_temp['gender'] = 'fem'

        if noun in feminine_or_masc or (noun[-5:] == 'λόγος' and number_of_syllables > 3):
            # especially all kinds of professionals
            noun_temp['gender'] = 'fem,masc'

        if not noun_temp['nom_pl'] and not gens_sg:
            # maybe its neuter like lathos
            plural_form = stem + 'η'
            gen_form = stem + 'ους'

            if accent == 'ultimate':
                plural_form = stem + 'ή'
                gen_form = stem + 'ούς'
            elif accent == 'antepenultimate':
                plural_form = put_accent_on_the_penultimate(plural_form)
                gen_form = put_accent_on_the_penultimate(gen_form)

            if plural_form in greek_corpus or gen_form in greek_corpus:
                noun_temp['nom_pl'] = plural_form
                noun_temp['gen_sg'] = gen_form
                noun_temp['gender'] = 'neut'

            else:
                # γεγονός και άλλες μετοχές τού παρακειμένου
                plural_form = noun[:-1] + 'τα'
                gen_form = noun[:-1] + 'τος'
                if plural_form in greek_corpus or gen_form in greek_corpus:
                    noun_temp['nom_pl'] = plural_form
                    noun_temp['gen_sg'] = gen_form
                    noun_temp['gender'] = 'neut'

        # in all other instances probably they are correct masculin words, but dont occur in the corpus
        if not (noun_temp['nom_pl'] or noun_temp['gen_sg']):
            stem = noun[:-2]
            plural_form = stem + 'οι'
            gen_form = put_accent(stem + 'ου', accent, true_syllabification=False)
            noun_temp['gender'] = 'masc'
            if accent == 'ultimate':
                plural_form = stem + 'οί'
                gen_form = stem + 'ού'
            if not proper_name:
                noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
            noun_temp['gender'] = 'masc'

    elif noun[-1] == 'ς' and \
            ((noun[:-1] + 'δες' in greek_corpus) or (put_accent_on_the_antepenultimate(noun[:-1] + 'δες') in greek_corpus)
             or (put_accent_on_the_penultimate(noun[:-1] + 'δες') in greek_corpus)) and noun[-2:] != 'ις':
        #imparisyllaba on des, archaic and modern
        print('giannides')

        noun_temp['gender'] = 'masc'
        noun_temp['gen_sg'] = noun[:-1]
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
        noun_temp['nom_pl'] = ','.join(plurals)
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
        print(gens, 'GENS')
        noun_temp['gen_sg'] = ','.join(gens)

    elif noun[-2:] in ['ές', 'ες']:

        # they can be either plur tantum or masc on es that do not have plur in the corpus
        if noun[:-1] in greek_corpus or noun[:-1].capitalize() in greek_corpus:
            # this means its a gen. of a masc form
            noun_temp['gender'] = 'masc'
            noun_temp['gen_sg'] = noun[:-1]
            noun_temp['nom_pl'] = noun[:-1] + 'δες'

        elif (noun[:-2] + 'ων') in greek_corpus or (remove_all_diacritics(noun[:-2]) + 'ών') in greek_corpus or \
                (noun[:-2] + 'ων').capitalize() in greek_corpus or (remove_all_diacritics(noun[:-2]) + 'ών').capitalize() in greek_corpus or noun in ['προάλλες', 'πρόποδες']:

            noun_temp['gender'] = 'fem'
            if noun in ['πρόποδες', 'χοιράδες']:
                noun_temp['gender'] = 'masc'
            noun_temp['gen_sg'] = ''
            noun_temp['nom_pl'] = noun
            noun_temp['nom_sg'] = ''

        else:
            # should be neuter aklita
            noun_temp['gender'] = 'neut'
            noun_temp['gen_sg'] = noun
            noun_temp['nom_pl'] = noun
            noun_temp['nom_sg'] = noun

    elif noun[-2:] in ['άς', 'ής', 'ας', 'ης']:

        noun_temp['gender'] = 'masc'
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
        gen_form_ba = noun[:-1]
        # ancient forms
        plural_form_c = noun[:-1] + 'τες'
        plural_form_c_neut = noun[:-1] + 'τα'
        gen_form_c = noun[:-1] + 'τος'
        if not ultimate_accent:
            plural_form_c = put_accent_on_the_antepenultimate(plural_form_c, true_syllabification=False)
            plural_form_c_neut = put_accent_on_the_antepenultimate(plural_form_c_neut, true_syllabification=False)
            gen_form_c = put_accent_on_the_antepenultimate(gen_form_c, true_syllabification=False)

        if plural_form_c in greek_corpus and gen_form_c in greek_corpus:
            noun_temp['nom_pl'] = plural_form_c
            noun_temp['gen_sg'] = gen_form_c
            # but there is possible, that there is also more dimotiki form of gen_sg
            if gen_form_a in greek_corpus:
                noun_temp['gen_sg'] = gen_form_c + ',' + gen_form_a

        elif (plural_form_b in greek_corpus and gen_form_b in greek_corpus) and noun[-3:] not in ['ίας']:
            # the last condition is to exclude possibility, that it is false positive because of some same sounding
            # fut aorist forms
            noun_temp['nom_pl'] = plural_form_b
            noun_temp['gen_sg'] = gen_form_b

        elif plural_form_ba in greek_corpus and gen_form_ba in greek_corpus and (gen_form_b[:-1] + 'ούν' not in greek_corpus):
            noun_temp['nom_pl'] = plural_form_ba
            noun_temp['gen_sg'] = gen_form_ba

        elif plural_form_a in greek_corpus or gen_form_a in greek_corpus:

            noun_temp['nom_pl'] = plural_form_a
            noun_temp['gen_sg'] = gen_form_a

        elif plural_form_c_neut in greek_corpus and gen_form_c in greek_corpus:
            noun_temp['nom_pl'] = plural_form_c_neut
            noun_temp['gen_sg'] = gen_form_c
            noun_temp['gender'] = 'neut'

            # there are many professions that are rarely in plural, but which do have gen, and almost all of them
            # create gen by subtracting s
        else:
            noun_temp['nom_pl'] = plural_form_a
            noun_temp['gen_sg'] = gen_form_a

        # lastly check maybe there are professions which can be feminine
        if noun in feminine_or_masc:
            noun_temp['gender'] = 'masc,fem'
        # and again a better test for all -eas, if there is gen sg on ews, this  has certainly femine form, this gen
        # form cannot be added as an alternative, as it occures only for feminines and has to be added in create_all
        # function
        fem_gen = noun[:-3] + 'έως'

        if noun[-3:] == 'έας' and fem_gen in greek_corpus:
            noun_temp['gender'] = 'masc,fem'

    elif noun[-3:] in ['εύς', 'ευς']:

        plural_form = noun[:-3] + 'είς'
        gen_form = noun[:-3] + 'έως'
        noun_temp['gender'] = 'masc'
        if plural_form in greek_corpus and gen_form in greek_corpus:
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
        if noun == 'Ζευς':


            noun_temp['gen_sg'] = 'Διός,Δίος'
            noun_temp['nom_pl'] = ''

        if noun in feminine_or_masc:
            noun_temp['gender'] = 'fem,masc'
        # return noun_temp

    elif noun[-2:] in ['ώς', 'ως']:
        noun_temp['gender'] = 'neut'
        plural_form = noun[:-1] + 'τα'
        gen_form = noun[:-1] + 'τος'
        thema_ot = put_accent(noun[:-2] + 'οτ', accent)
        if count_syllables(noun) == 1:
            gen_form = put_accent_on_the_ultimate(gen_form)
            plural_form = put_accent_on_the_antepenultimate(plural_form)
        if plural_form in greek_corpus or gen_form in greek_corpus:
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
        # there is possibility, thατ the thema is on 'οτ'
        elif thema_ot + 'ος' in greek_corpus:
            noun_temp['gender'] = 'neut'
            gen_form = thema_ot + 'ος'
            plural_form = thema_ot + 'α'
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
        # there are also rare femine on ως with gen on υος eg 'αιδώς'
        elif put_accent(noun[:-2] + 'ους', accent) in greek_corpus:
            gen_form = put_accent(noun[:-2] + 'ους', accent)
            noun_temp['gen_sg'] = gen_form
            noun_temp['gender'] = 'fem'
        elif noun == 'άλως':
            # its kind of exception
            gen_form = 'άλω'
            noun_temp['gen_sg'] = gen_form
            noun_temp['gender'] = 'fem'

    elif noun[-2:] == 'ις':
        noun_temp['gender'] = 'fem'
        plural_form = put_accent_on_the_penultimate(noun[:-2] + 'εις', true_syllabification=False)

        gen_form = noun[:-2] + 'εως'
        if noun == 'μις':
            # special case
            plural_form = noun
            gen_form = noun


        if gen_form in greek_corpus or plural_form in greek_corpus:
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form

        else:
            # maybe gen on idos
            gen_form = noun[:-1] + 'δος'
            plural_form = noun[:-1] + 'δες'

            if gen_form in greek_corpus or plural_form in greek_corpus:
                noun_temp['nom_pl'] = plural_form
                noun_temp['gen_sg'] = gen_form

    elif noun[-3:] in ['ους', 'ούς']:
        if 'πλους' in noun or 'νους' in noun and noun != 'μπόνους':
            noun_temp['gender'] = 'masc'
            noun_temp['gen_sg'] = noun[:-1]
        elif noun == 'ους':
            # το αυτί χρειάζεται να είναι μόνο του
            noun_temp['gender'] = 'neut'
            noun_temp['gen_sg'] = 'ωτός'
            noun_temp['nom_pl'] = 'ώτα'
        else:
            # aklita
            noun_temp['gender'] = 'neut'
            noun_temp['gen_sg'] = noun
            noun_temp['nom_pl'] = noun

    elif noun[-2:] in ['υς', 'ύς']:
        noun_temp['gender'] = 'fem'
        gen_form = noun[:-1] + 'ος'
        if count_syllables(noun) == 1:
            gen_form = put_accent_on_the_ultimate(gen_form)
            thema = put_accent_on_the_ultimate(noun)
        plur_form = thema[:-1] + 'ες'
        if noun in ['βοτρύς','ιχθύς','πέλεκυς', 'μυς']:
            noun_temp['gender'] = 'masc'
        if noun == 'πέλεκυς':
            gen_form = 'πελέκεως'
            plur_form = 'πελέκεις'

        noun_temp['gen_sg'] = gen_form
        noun_temp['nom_pl'] = plur_form


    elif noun[-1] in ['α', 'η', 'ά', 'ή']:
        # feminina
        noun_temp['gender'] = 'fem'
        gen_a = noun + 'ς'
        noun_temp['gen_sg'] = gen_a
        plural_form_a = noun[:-1] + 'ες'
        if ultimate_accent:
            plural_form_a = noun[:-1] + 'ές'
        plural_form_b = put_accent_on_the_penultimate(noun[:-1] + 'εις', true_syllabification=False)
        plural_form_c = noun + 'δες'

        if plural_form_c in greek_corpus:
            noun_temp['nom_pl'] = plural_form_c

        else:
            noun_temp['nom_pl'] = plural_form_a

        # special case for neuter on ma
        if noun[-2:] == 'μα' and (plural_form_a not in greek_corpus or plural_form_b not in greek_corpus or plural_form_c not in greek_corpus or put_accent_on_the_antepenultimate(noun + 'τα', true_syllabification=False) in greek_corpus):
            plural_form = put_accent_on_the_antepenultimate(noun + 'τα', true_syllabification=False)
            gen_form = put_accent_on_the_antepenultimate(noun + 'τος', true_syllabification=False)
            if plural_form in greek_corpus or gen_form in greek_corpus:
                noun_temp['nom_pl'] = plural_form
                noun_temp['gen_sg'] = gen_form
                noun_temp['gender'] = 'neut'
        if noun[-1] == 'α' and noun + 'τος' in greek_corpus and noun + 'τα' in greek_corpus:
            # gala, galatos

            noun_temp['nom_sg'] = noun
            noun_temp['nom_pl'] = noun + 'τα'
            noun_temp['gen_sg'] = noun + 'τος'
            noun_temp['gender'] = 'neut'
            if 'γάλα' in noun:
                noun_temp['nom_pl'] = noun + 'τα' + ',' + noun + 'κτα'
                noun_temp['gen_sg'] = noun + 'τος' + ',' + noun + 'κτος'

        if noun in plur_tant_neut:
            # maybe pluralia tantum
            noun_temp['nom_sg'] = ''
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = ''
            noun_temp['gender'] = 'neut'

        if (noun[-2:] in ['ση', 'ξη', 'ψη'] or noun in feminine_h_eis) and put_accent_on_the_ultimate(noun[:-1] + 'ων') not in greek_corpus:
            # it has to be if, because it can be earlier falsly recognized as a correct form on es, because of som aorists
            # in sec person sg
            noun_temp['nom_pl'] = plural_form_b
            noun_temp['gen_sg'] = gen_a + ',' + put_accent_on_the_antepenultimate(noun[:-1] + 'εως', true_syllabification=False)

    elif noun[-2:] == 'ού':
        noun_temp['gender'] = 'fem'
        noun_temp['gen_sg'] = noun + 'ς'
        plural_form = noun + 'δες'
        if plural_form in greek_corpus:
            noun_temp['nom_pl'] = plural_form

    elif noun[-1] in ['ό', 'ο']:
        if noun[-3:] == 'ιμο':
            plural_form = noun[:-1] + 'ατα'
            gen_form = noun[:-1] + 'ατος'
            plural_form = put_accent_on_the_antepenultimate(plural_form)
            gen_form = put_accent_on_the_penultimate(gen_form)
            if plural_form in greek_corpus or gen_form in greek_corpus:
                noun_temp['nom_pl'] = plural_form
                noun_temp['gen_sg'] = gen_form
                noun_temp['gender'] = 'neut'

                return noun_temp

        noun_temp['gender'] = 'neut'
        plural_form = noun[:-1] + 'α'
        gen_form = noun[:-1] + 'ου'
        if ultimate_accent:
            plural_form = noun[:-1] + 'ά'
            gen_form = noun[:-1] + 'ού'
        if plural_form in greek_corpus or plural_form.capitalize() in greek_corpus or number_of_syllables>4:
            noun_temp['nom_pl']=plural_form

        gens = []
        if gen_form in greek_corpus or gen_form.capitalize() in greek_corpus or number_of_syllables>4:
            gens.append(gen_form)

        if accent == 'antepenultimate':
            gen_a = put_accent(gen_form, 'penultimate', true_syllabification=False)
            if gen_a in greek_corpus:
                gens.append(gen_a)

        if gens:
            noun_temp['gen_sg'] = ','.join(gens)
        else:
            # σ`αυτήν την περίπτωση υποθετούμε πως είναι ουδέτερα άκλιτα
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = noun
            noun_temp['gender'] = 'neut'

    elif noun[-1] in ['ι', 'ί', 'ΐ'] and noun[-2:] not in ['οι', 'οί']:
        noun_temp['gender'] = 'neut'
        plural_form = noun + 'α'
        gen_form = put_accent_on_the_ultimate(noun + 'ου')
        if ultimate_accent:
            plural_form = put_accent_on_the_ultimate(plural_form)

        if plural_form[-3] in vowels:

            plural_form = plural_form[:-2] + 'γι' + plural_form[-1]
            gen_form = gen_form[:-3] + 'γι' + gen_form[-2:]

        # in greek corpus there are lacking some upokoristika
        if plural_form in greek_corpus or noun[-3:] in ['άκι', 'ίκι', 'άρι', 'έκι', 'ήρι', 'ίδι', 'ύρι']:
            noun_temp['nom_pl'] = plural_form

            noun_temp['gen_sg'] = gen_form

        if noun_temp['nom_pl'] == '' and noun_temp['gen_sg'] == '':
            # we conclude these are aklita, but I am sure there will be some uncovered words that do decline,
            # I have no idea though how to sort them out
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = noun

    elif noun[-2:] in ['οι', 'οί']:
        # pluralis tantum masc
        noun_temp['gender'] = 'masc'
        noun_temp['nom_pl'] = noun
        noun_temp['nom_sg'] = ''
        noun_temp['gen_sg'] = ''

    # ending n is a bit tricky, so we will work it out separatly

    elif noun[-2:] in ['ον', 'όν', 'έν', 'εν', 'άν', 'αν']:
        # ουδετερα ουσιαστικά με θέμα σε -ντ, παιρνει ύποψη και τα αρχαία ουδέτερα Β' κλίσης σε -ον

        noun_temp['gender'] = 'neut'
        plural_form = noun + 'τα'

        gen_form = noun + 'τος'
        # αρχαίες λέξεις με ον
        plural_form_a = ''
        gen_form_a = ''

        if noun[-2:] in ['ον', 'όν']:

            plural_form_a = noun[:-2] + 'ά'
            gen_form_a = noun[:-2] + 'ού'

            if not ultimate_accent:
                plural_form_a = noun[:-2] + 'α'
                gen_form_a = put_accent_on_the_penultimate(gen_form_a,
                                                       true_syllabification=False)
        if not is_accented(noun):
            # μονοσύλλαβα τονίζονται στην γενική στην ληγούσα
            plural_form = put_accent_on_the_penultimate(plural_form, true_syllabification=False)
            gen_form = put_accent_on_the_ultimate(gen_form)
            if noun == 'ον': gen_form = put_accent_on_the_penultimate(gen_form)

        if plural_form in greek_corpus and gen_form in greek_corpus:

            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form

        elif plural_form_a in greek_corpus and gen_form_a in greek_corpus:
            noun_temp['nom_pl'] = plural_form_a
            noun_temp['gen_sg'] = gen_form_a
        else:
            # it is assumed it's a borrowing from french

            if noun in ['ρεσεψιόν', 'σπορτσγούμαν']:
                # there are certainly more
                noun_temp['gender'] = 'fem'
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = noun

    elif noun[-2:] in ['ων', 'ών']:
        noun_temp['gender']= 'masc'

        irregular_3 = {'κύων':'κυν', 'είρων': 'είρων', 'ινδικτιών':'ινδικτιών'}

        # 2 possibilities
        stem_a = noun[:-2] + 'όν'
        stem_b = noun[:-2] + 'όντ'
        stem_c = noun[:-2] + 'ούντ'
        stem_d = noun[:-2] + 'ώντ'

        plural_form_a = stem_a + 'ες'
        gen_form_a = stem_a + 'ος'
        plural_form_b = stem_b + 'ες'
        gen_form_b = stem_b + 'ος'
        plural_form_c = stem_c + 'ες'
        gen_form_c = stem_c + 'ος'
        plural_form_d = stem_d + 'ες'
        gen_form_d = stem_d + 'ος'

        ir_stem = False
        if noun in irregular_3.keys():
            ir_stem = irregular_3[noun]

        if ir_stem:

            ir_pl = ir_stem + 'ες'
            ir_gen = ir_stem + 'ος'
            if count_syllables(ir_stem) == 1 and ir_gen not in greek_corpus:
                ir_pl = put_accent_on_the_antepenultimate(ir_pl)
                ir_gen = put_accent_on_the_antepenultimate(ir_gen)
                if ir_gen not in greek_corpus:
                    ir_gen = put_accent_on_the_ultimate(ir_gen)

            if ir_pl in greek_corpus and ir_gen in greek_corpus:
                noun_temp['nom_pl'] = ir_pl
                noun_temp['gen_sg'] = ir_gen

                return noun_temp

        if not ultimate_accent:
            plural_form_a = put_accent_on_the_antepenultimate(plural_form_a, true_syllabification=False)
            gen_form_a = put_accent_on_the_antepenultimate(gen_form_a, true_syllabification=False)
            plural_form_b = put_accent_on_the_antepenultimate(plural_form_b, true_syllabification=False)
            gen_form_b = put_accent_on_the_antepenultimate(gen_form_b, true_syllabification=False)

        if plural_form_a in greek_corpus and gen_form_a in greek_corpus:
            noun_temp['nom_pl'] = plural_form_a
            noun_temp['gen_sg'] = gen_form_a
        elif plural_form_b in greek_corpus and gen_form_b in greek_corpus:
            noun_temp['nom_pl'] = plural_form_b
            noun_temp['gen_sg'] = gen_form_b
        elif plural_form_c in greek_corpus and gen_form_c in greek_corpus:
            noun_temp['nom_pl'] = plural_form_c
            noun_temp['gen_sg'] = gen_form_c
        elif plural_form_d in greek_corpus and gen_form_d in greek_corpus:
            noun_temp['nom_pl'] = plural_form_d
            noun_temp['gen_sg'] = gen_form_d


    elif noun[-1] in ['ξ', 'ψ', 'τ', 'ρ',  'β', 'ν', 'δ', 'ε', 'έ', 'ζ', 'κ', 'λ', 'μ'] and \
            noun not in ['σεξ', 'σερ', 'φαξ', 'μπορ', 'μπαρ', 'μποξ']:
        # not very common but existing 3rd declension nouns

        stems = []

        if noun[-1] == 'ξ':

            stems.append(noun[:-1] + 'κ')
            stems.append(noun[:-1] + 'χ')
            stems.append(noun[:-1] + 'κτ')
        elif noun[-1] == 'ψ':

            stems.append(noun[:-1] + 'π')
            stems.append(noun[:-1] + 'φ')
            stems.append(noun[:-1] + 'πτ')
            stems.append(noun[:-1] + 'β')

        elif noun[-1] == 'ρ':

            stems.append(noun)
            stems.append(noun[:-1] + 'τ')
            if noun[-2:] == 'ωρ':
                stems.append(noun[:-2] + 'ορ')
                noun_temp['gender'] = 'masc'

                if 'μήτωρ' in noun:
                    noun_temp['gender'] = 'fem'
            elif noun[-2:] == 'ώρ':
                stems.append(noun[:-2] + 'όρ')
                noun_temp['gender'] = 'masc'
            else:
                noun_temp['gender'] = 'neut'


        for stem in stems:
            plural_form = stem + 'ες'
            plural_form_n = stem + 'α'
            gen_form = stem + 'ος'
            if count_syllables(stem) == 1:
                plural_form = put_accent_on_the_antepenultimate(plural_form)
                plural_form_n = put_accent_on_the_antepenultimate(plural_form_n)
                gen_form = put_accent_on_the_antepenultimate(gen_form)
                if gen_form not in greek_corpus:
                    gen_form = put_accent_on_the_ultimate(gen_form)
            elif where_is_accent(stem) == 'antepenultimate':
                gen_form = put_accent_on_the_antepenultimate(gen_form)
                plural_form = put_accent_on_the_antepenultimate(plural_form)
                plural_form_n = put_accent_on_the_antepenultimate(plural_form_n)


            if plural_form in greek_corpus and noun not in ['πυρ']:
                noun_temp['nom_pl'] = plural_form
                if gen_form in greek_corpus:
                    noun_temp['gen_sg'] = gen_form
                noun_temp['gender'] = 'masc'
                # it's a bit crude way to correct gender but i cannot find a better way without a comprehensive list
                gen_pl = remove_all_diacritics(plural_form[:-2]) + 'ών'
                if gen_pl in greek_corpus:
                    noun_temp['gender'] = 'fem'
            else:
                if plural_form_n in greek_corpus or noun in ['έαρ']:
                    noun_temp['gender'] = 'neut'
                    noun_temp['gen_sg'] = gen_form
                    if noun not in ['έαρ']:
                        noun_temp['nom_pl'] = plural_form_n
                    return noun_temp

        # else it is assumed it's either borrowing or some substantiated other things

        noun_temp['gender'] = 'neut'
        noun_temp['nom_pl'] = noun
        noun_temp['gen_sg'] = noun
        if noun in ['σπεσιαλιτέ', 'ρεσεψιόν']:
            # there are probably more such cases
            noun_temp['gender'] = 'fem'
        if noun in ['σερ']:
            # there should be added probably a lot of proper names, but I will deal with it by using a flag proper_name_gender
            noun_temp['gender'] = 'masc'

    elif noun[-1] in ['ώ', 'ω']:

        if noun in ['ηχώ','πειθώ','φειδώ', 'βάβω']:
            # ancient feminin
            noun_temp['gender'] = 'fem'

            noun_temp['gen_sg'] = noun[:-1] + 'ούς'
            if noun in ['βάβω']:
                noun_temp['gen_sg'] = noun
        elif noun.capitalize() == noun:
            # feminine proper name
            noun_temp['gender'] = 'fem'
            noun_temp['gen_sg'] = noun + 'ς'

        else:
            noun_temp['gender'] = 'neut'
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = noun

    elif noun[-1] in ['υ', 'ύ']:
        # ancient 3 declesion, oksy , asty
        noun_temp['gender'] = 'neut'
        if noun[-2:] in ['ου', 'ού']:
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = noun
        elif noun[-1] == 'υ':
            gen_1 = noun + 'ου'
            gen_1b = put_accent_on_the_penultimate(gen_1)
            plural = noun + 'α'

            if gen_1 in greek_corpus:
                noun_temp['gen_sg'] = gen_1
            elif gen_1b in greek_corpus:
                noun_temp['gen_sg'] = gen_1b
            if plural in greek_corpus:
                noun_temp['nom_pl'] = plural

            if noun in ['άστυ', 'δόρυ']:
                noun_temp['nom_pl'] = noun[:-1] + 'η'
                noun_temp['gen_sg'] = noun[:-1] + 'εως'
            if noun in ['βράδυ']:
                noun_temp['nom_pl'] = noun[:-1] + 'ια'
                noun_temp['gen_sg'] = put_accent_on_the_ultimate(noun[:-1] + 'ιου')
            if noun in ['στάχυ', 'δίχτυ']:
                noun_temp['nom_pl'] = noun + 'α'
                noun_temp['gen_sg'] = put_accent_on_the_ultimate(noun + 'ου')
            if noun in ['δάκρυ']:
                noun_temp['nom_pl'] = noun + 'α'
                noun_temp['gen_sg'] = put_accent_on_the_penultimate(noun + 'ου', true_syllabification=False)
        elif noun[-1] in ['ύ']:
            thema = noun[:-1] + 'έ'
            gen = thema + 'ος'
            plur = thema + 'α'
            if gen in greek_corpus:
                noun_temp['gen_sg'] = gen
            if plur in greek_corpus:
                noun_temp['nom_pl'] = plur

    if not noun_temp['nom_pl'] and not noun_temp['gen_sg']:

        # aklita
        noun_temp['gender'] = 'neut'
        noun_temp['nom_pl'] = noun
        noun_temp['gen_sg'] = noun
        aklita_gender = {'μαδιάμ': 'fem', 'μωάμεθ': 'masc', 'μάνατζερ': 'masc', 'σερ': 'masc', 'σεφ': 'masc',
                            'ντετέκτιβ': 'masc', 'ντεντέκτιβ': 'masc', 'ρεπόρτερ': 'masc', 'πλαζ': 'fem',
                         'σεζόν': 'fem', 'σπεσιαλιτέ': 'fem', 'ρεσεψιόν': 'fem'}

        if noun.lower() in aklita_gender.keys():
            noun_temp['gender'] = aklita_gender[noun.lower()]

    if proper_name_gender:
        noun_temp['gender'] = proper_name_gender

    irregularities = {'σέβας':{'nom_sg': 'σέβας', 'nom_pl': 'σέβη', 'gen_sg': '', 'gender': 'neut'},
                      'σέλας':{'nom_sg': 'σέλας', 'nom_pl': 'σέλατα,σέλαα', 'gen_sg': 'σέλατος,σέλαος', 'gender': 'neut'},
                      'δείλι': {'nom_sg': 'δείλι', 'nom_pl': '', 'gen_sg': '', 'gender': 'neut'},
                      'Πάσχα': {'nom_sg': 'Πάσχα', 'nom_pl': '', 'gen_sg': '', 'gender': 'neut'},
                      'δόρυ': {'nom_sg': 'δόρυ', 'nom_pl': 'δόρατα', 'gen_sg': 'δόρατος', 'gender': 'neut'},
                      'ήμισυ': {'nom_sg': 'ήμισυ', 'nom_pl': '', 'gen_sg': 'ημίσεος', 'gender': 'neut'},

                      }


    if noun in irregularities.keys():
        noun_temp = irregularities[noun]

    diploklita = {'βράχος': 'βράχοι,βράχια', 'λαιμός': 'λαιμοί,λαιμά',
                  'λόγος': 'λόγοι,λόγια', 'πλούτος': ',πλούτη',
                  'σανός': ',σανά', 'χρόνος': 'χρόνοι,χρόνια',
                  'καπνός': 'καπνοί,καπνά', 'νιότη': ',νιάτα'}

    if noun in diploklita.keys():
        noun_temp['nom_pl'] = diploklita[noun]

    if capital:
        noun_temp = capitalize_basic_forms(noun_temp)

    return noun_temp


def capitalize_basic_forms(noun_temp):
    for key in noun_temp:
        if key != 'gender':
            noun_temp[key] = noun_temp[key].capitalize()
    return noun_temp
