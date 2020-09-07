import pickle


from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_penultimate,\
    put_accent_on_the_antepenultimate, is_accented, put_accent_on_the_ultimate, count_syllables, remove_all_diacritics
from modern_greek_accentuation.resources import vowels
from resources import feminine_os, feminine_h_eis

try:
    file = open('modern_greek_stemmer/el_GR.pickle', 'br')
except FileNotFoundError:
    file = open('el_GR.pickle', 'br')
greek_corpus = pickle.load(file)
file.close()




def create_list_of_all_noun():
    file = open('modern_greek_stemmer/greek_nouns.pickle', 'rb')
    nouns = pickle.load(file)
    file.close()

    parsed_nouns = []
    unknown = []
    for noun in nouns:
        n = create_all_basic_noun_forms(noun)
        parsed_nouns.append(n)
    file = open('modern_greek_stemmer/all_greek_nouns.pickle', 'wb')
    pickle.dump(parsed_nouns, file)
    file.close()

def add_fem_and_neut():
    # there are nouns, which could be interpreted as adj, but which in our db are
    # nouns, that create feminine and neuter forms on ou and iko
    file = open('modern_greek_stemmer/all_greek_nouns.pickle', 'rb')
    nouns = pickle.load(file)
    file.close()
    for noun in nouns:
        if noun['nom_sg'] and noun['nom_sg'][-1] == 'ς' and noun['nom_pl'][-3:] == 'δες':
            masc = noun['nom_sg']
            fem = masc[:-2] + 'ού'
            if fem in greek_corpus:
                fem_noun_temp = {'nom_sg': fem, 'gen_sg': fem + 'ς', 'nom_pl': fem + 'δες', 'gender': 'fem'}
                neut_noun_temp = {'nom_sg': masc[:-1] + 'δικο', 'gen_sg': masc[:-1] + 'δικου' , 'nom_pl': masc[:-1] + 'δικα', 'gender': 'neut'}
                nouns.append(fem_noun_temp)
                nouns.append(neut_noun_temp)


    file = open('modern_greek_stemmer/all_greek_nouns.pickle', 'wb')
    pickle.dump(nouns, file)
    file.close()


def create_all_basic_noun_forms(noun):
    # I need nom sg, nom. pl. gender
    noun_temp ={'nom_sg': noun, 'gen_sg': '', 'nom_pl': '', 'gender': ''}
    print(noun[-3:])
    number_of_syllables = count_syllables(noun, true_syllabification=False)
    accent = where_is_accent(noun, true_syllabification=False)
    ultimate_accent = accent == 'ultimate'

    # problem - among nouns there are many one syllable names as for example letter names. These are for the most
    # part indeclinable and neuter but below logic is not helpful in their case as they can end on whatever they
    # want,

    """
    if count_syllables(noun, true_syllabification=False) == 1:
        is_a_normal_noun = input('is ' + noun + ' normal noun')

        if is_a_normal_noun and is_a_normal_noun.lower()[0] == 'y':
            pass
        else:
            return {'nom_sg': noun, 'gen_sg': noun, 'nom_pl': noun, 'gender': 'neut'}
    
    
    """


    # on 'os'
    if noun[-2:] in ['ός', 'ος']:
        stem = noun[:-2]
        plural_form = stem + 'οι'
        gen_form = put_accent_on_the_penultimate(stem + 'ου', true_syllabification=False)
        noun_temp['gender'] = 'masc'
        if accent == 'ultimate':
            plural_form = stem + 'οί'
            gen_form = stem + 'ού'

        # the problem is that many long words on -os that are part of some kind of jargon do not have any other form
        # declined in the lexicon, i will assume then that words above 4 syllabes do exist, but only in singular, the
        # same should be the case for neuter long words on -o
        # also some proper names in greek_corpus are, as is proper, capitalized
        if gen_form in greek_corpus or gen_form.capitalize() in greek_corpus or number_of_syllables >4:
            noun_temp['gen_sg'] = gen_form

        elif accent == 'antepenultimate':
            # sometimes in compounds accent does not move (μεγαλέμπορος μεγαλέμπορου)
            gen_form = put_accent_on_the_antepenultimate(gen_form)
            if gen_form in greek_corpus or gen_form.capitalize() in greek_corpus:
                noun_temp['gen_sg'] = gen_form

        if plural_form in greek_corpus or plural_form.capitalize() in greek_corpus or number_of_syllables > 4:
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form

        if noun in feminine_os:
            # create this list manually
            noun_temp['gender'] = 'fem'


        if not (noun_temp['nom_pl'] or noun_temp['gen_sg']):
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
    # on 'hs', 'as', 'es', 'ous' etc


        # in all other instances probably they are correct masculin words, but dont occur in the corpus
        if not (noun_temp['nom_pl'] or noun_temp['gen_sg']):
            stem = noun[:-2]
            plural_form = stem + 'οι'
            gen_form = put_accent_on_the_penultimate(stem + 'ου', true_syllabification=False)
            noun_temp['gender'] = 'masc'
            if accent == 'ultimate':
                plural_form = stem + 'οί'
                gen_form = stem + 'ού'

            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
            noun_temp['gender'] = 'masc'

    elif noun[-1] == 'ς' and \
            ((noun[:-1] + 'δες' in greek_corpus) or (put_accent_on_the_antepenultimate(noun[:-1] + 'δες') in greek_corpus)
             or (put_accent_on_the_penultimate(noun[:-1] + 'δες') in greek_corpus)) and noun[-2:] != 'ις':
        #imparisyllaba on des, archaic and modern

        noun_temp['gender'] = 'masc'
        noun_temp['gen_sg'] = noun[:-1]
        plural_form = noun[:-1] + 'δες'
        # sometimes the accent has to be moved
        plural_form_a = put_accent_on_the_antepenultimate(plural_form)
        plural_form_b = put_accent_on_the_penultimate(plural_form)
        noun_temp['nom_pl'] = plural_form
        if plural_form not in greek_corpus and plural_form_a in greek_corpus:
            noun_temp['nom_pl'] = plural_form_a
        else:
            noun_temp['nom_pl'] = plural_form_b
        gen_form = noun[:-1]
        gen_form_a = put_accent_on_the_penultimate(gen_form)
        gen_form_arch = noun[:-1] + 'δος'
        if count_syllables(noun) == 1:
            gen_form_arch = put_accent_on_the_ultimate(gen_form_arch)

        if gen_form_arch in greek_corpus and gen_form not in greek_corpus and gen_form_a not in greek_corpus:
            noun_temp['gen_sg'] = gen_form_arch

        elif gen_form in greek_corpus:
            noun_temp['gen_sg'] = gen_form
        elif gen_form_a in greek_corpus:
            noun_temp['gen_sg'] = gen_form_a

    elif noun[-2:] in ['ές', 'ες']:

        # they can be either plur tantum or masc on es that do not have plur in the corpus
        if noun[:-1] in greek_corpus or noun[:-1].capitalize() in greek_corpus or noun in ['τρολές']:
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

    elif noun[-3:] in ['εύς', 'ευς']:
        print('zeus')
        plural_form = noun[:-3] + 'είς'
        gen_form = noun[:-3] + 'έως'
        noun_temp['gender'] = 'masc'
        if plural_form in greek_corpus and gen_form in greek_corpus:
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
        if noun == 'Ζευς':
            noun_temp['gen_sg'] = 'Διός'
            noun_temp['nom_pl'] = ''

    elif noun[-2:] in ['ώς', 'ως']:
        noun_temp['gender'] = 'neut'
        plural_form = noun[:-1] + 'τα'
        gen_form = noun[:-1] + 'τος'
        if count_syllables(noun) == 1:
            gen_form = put_accent_on_the_ultimate(gen_form)
            plural_form = put_accent_on_the_antepenultimate(plural_form)
        if plural_form in greek_corpus or gen_form in greek_corpus:
            noun_temp['nom_pl'] = plural_form
            noun_temp['gen_sg'] = gen_form
        elif noun in ['υπεζωκώς'] or 'φυκώς' in noun:
            noun_temp['gender'] = 'neut'
            gen_form = noun[:-2] + 'ότος'
            noun_temp['nom_pl'] = ''
            noun_temp['gen_sg'] = gen_form
        elif noun in ['αιδώς', 'άλως']:
            gen_form = noun[:-2] + 'ους'
            if where_is_accent(noun) == 'ultimate':
                gen_form = put_accent_on_the_ultimate(gen_form)
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
        if noun[-1] == 'α' and noun + 'τος' in greek_corpus:
            # gala, galatos

            noun_temp['nom_sg'] = noun
            noun_temp['nom_pl'] = noun + 'τα'
            noun_temp['gen_sg'] = noun + 'τος'
            noun_temp['gender'] = 'neut'

        if noun in ['Χριστούγεννα', 'χριστούγεννα', 'νιάτα', 'βαλκάνια']:
            # maybe pluralia tantum
            noun_temp['nom_sg'] = ''
            noun_temp['nom_pl'] = noun
            noun_temp['gen_sg'] = ''
            noun_temp['gender'] = 'neut'

        if (noun[-2:] in ['ση', 'ξη', 'ψη'] or noun in feminine_h_eis) and put_accent_on_the_ultimate(noun[:-1] + 'ων') not in greek_corpus:
            # it has to be if, because it can be earlier falsly recognized as a correct form on es, because of som aorists
            # in sec person sg
            noun_temp['nom_pl'] = plural_form_b

        if noun_temp['nom_pl'] == '':
            print('BRAK', noun)

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
            gen_form = put_accent_on_the_antepenultimate(gen_form)
            if plural_form in greek_corpus or gen_form in greek_corpus:
                noun_temp['nom_pl'] = plural_form
                noun_temp['gen_sg'] = gen_form
                noun_temp['gender'] = 'neut'
                return noun_temp


        noun_temp['gender'] = 'neut'
        plural_form = noun[:-1] + 'α'
        gen_form = noun[:-1] + 'ου'
        gen_form_a = put_accent_on_the_penultimate(gen_form, true_syllabification=False)
        if ultimate_accent:
            plural_form = noun[:-1] + 'ά'
            gen_form = noun[:-1] + 'ού'
        if plural_form in greek_corpus or plural_form.capitalize() in greek_corpus or number_of_syllables>4:
            noun_temp['nom_pl']=plural_form

        if gen_form_a in greek_corpus or gen_form_a.capitalize() in greek_corpus or number_of_syllables>4:
            noun_temp['gen_sg']= gen_form_a
        elif gen_form in greek_corpus:
            noun_temp['gen_sg'] = gen_form
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
            # we conclude these are aklita, but I am sure there will be some uncovered words that do decline, I have no idea though how to sieve them out
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
        plural_form_a = 'XXXXX'
        gen_form_a = 'XXXXX'

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
        ir_stem = ''
        if noun in irregular_3.keys():
            ir_stem = irregular_3[noun]

        plural_form_a = stem_a + 'ες'
        gen_form_a = stem_a + 'ος'
        plural_form_b = stem_b + 'ες'
        gen_form_b = stem_b + 'ος'
        plural_form_c = stem_c + 'ες'
        gen_form_c = stem_c + 'ος'
        plural_form_d = stem_d + 'ες'
        gen_form_d = stem_d + 'ος'
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



    elif noun[-1] in ['ξ', 'ψ', 'τ', 'ρ',  'β', 'ν', 'δ', 'ε', 'έ', 'ζ', 'κ', 'λ', 'μ'] and noun not in ['σεξ', 'σερ', 'φαξ', 'μπορ', 'μπαρ', 'μποξ']:
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
            if noun[-2:] == 'ωρ':
                stems.append(noun[:-2] + 'ορ')
                noun_temp['gender'] = 'masc'

                if 'μήτωρ' in noun:
                    noun_temp['gender'] = 'fem'
            elif noun[-2:] == 'ώρ':
                stems.append(noun[:-2] + 'όρ')
                noun_temp['gender'] = 'masc'


        for stem in stems:
            plural_form = stem + 'ες'
            gen_form = stem + 'ος'
            if count_syllables(stem) == 1:
                plural_form = put_accent_on_the_antepenultimate(plural_form)
                gen_form = put_accent_on_the_antepenultimate(gen_form)
                if gen_form not in greek_corpus:
                    gen_form = put_accent_on_the_ultimate(gen_form)
            if plural_form in greek_corpus:
                noun_temp['nom_pl'] = plural_form
                if gen_form in greek_corpus:
                    noun_temp['gen_sg'] = gen_form
                else:
                    noun_temp['gen_sg'] = '-'
                noun_temp['gender'] = 'masc'
                # it's a bit crude way to correct gender but i cannot find better
                gen_pl = remove_all_diacritics(plural_form[:-2]) + 'ών'
                if gen_pl in greek_corpus:
                    noun_temp['gender'] = 'feminine'
                return noun_temp
            else:
                plural_form = stem + 'α'
                if plural_form in greek_corpus or noun in ['έαρ']:
                    noun_temp['gender'] = 'neut'
                    noun_temp['gen_sg'] = gen_form
                    return noun_temp

        # else it is assumed it's either borrowing or some substantiated other things

        noun_temp['gender'] = 'neut'
        noun_temp['nom_pl'] = noun
        noun_temp['gen_sg'] = noun
        if noun in ['σπεσιαλιτέ', 'ρεσεψιόν']:
            noun_temp['gender'] = 'fem'
        if noun in ['σερ']:
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



    if noun_temp['nom_pl'] or noun_temp['gen_sg']:

        return noun_temp
    else:
        # aklita
        noun_temp['gender'] = 'neut'
        noun_temp['nom_pl'] = noun
        noun_temp['gen_sg'] = noun
        if noun in ['μαδιάμ']:
            noun_temp['gender'] = 'fem'
        if noun in ['μωάμεθ']:
            noun_temp['gender'] = 'masc'
        return noun_temp

if __name__ == "__main__":

    #add_fem_and_neut()
    words = ('άνθρωπος', 'αρχαιολόγος', 'ψήφος', 'νηπιαγογός', 'υπολογιστής', 'ταξιτζής', 'δάσος', 'σκέλος', 'αναπτήρας', 'βασιλιάς',
             'βασιλεύς', 'συγγραφέας', 'μηχανή', 'πόλη', 'κατάσταση', 'λέξη', 'βραδιά', 'δολάριο', 'θέατρο', 'ευρώ', 'βιβλίο', 'παιδί',
             'τραπέζι', 'μάθημα', 'ρήμα', 'γράψιμο', 'άστυ', 'Κυριακή', 'Χριστούγεννα', 'προπόδες', 'αλεπού', 'αγώνας', 'ταμίας', 'φύλακας',
             'ψαράς', 'ρήγας', 'ναύτης', 'μαθητής', 'φούρναρης', 'μανάβης', 'παπουτσής', 'δουλευτής', 'συγγενής',
             'καφές', 'αντίλαλος', 'άνεμος', 'διάμετρος', 'Φρόσω', 'κυρά', 'κρέας', 'φως', 'γάλα', 'φωνήεν', 'καθήκον',
             'καθεστώς', 'δάκρυ', 'γεγονός', 'οξύ', 'ον', 'Ζευς', 'βρώμα')
    for word in words:
        res = create_all_basic_noun_forms(word)
        print(res)


