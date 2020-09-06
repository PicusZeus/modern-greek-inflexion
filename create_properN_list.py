import pickle
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_ultimate,\
    put_accent_on_the_penultimate, remove_all_diacritics, put_accent_on_the_antepenultimate

file = open('modern_greek_stemmer/el_GR.pickle', 'br')
greek_corpus = pickle.load(file)

file.close()




def check_in_greek_corpus(nom, gen, gender):
    noun_temp = {'nom_sg': nom, 'gen_sg': gen, 'gender': gender}
    if gen in greek_corpus:
        noun_temp['nom_sg'] = nom
        noun_temp['gen_sg'] = gen
        noun_temp['gender'] = gender
    elif gen.lower() in greek_corpus:

        noun_temp['nom_sg'] = nom.lower()

        noun_temp['gen_sg'] = gen.lower()
        noun_temp['gender'] = gender
    return noun_temp


def create_basic_forms(properN):

    accent = where_is_accent(properN, true_syllabification=False)
    properN_un = remove_all_diacritics(properN)
    if properN_un[-2:] in ['ος']:

        gen = properN[:-2] + 'ου'
        if accent == 'ultimate':
            gen = put_accent_on_the_ultimate(gen)
        elif accent in ['penultimate', 'antepenultimate']:

            gen = put_accent_on_the_penultimate(gen, true_syllabification=False)
        gender = 'masc'

    elif properN_un[-2:] in ['ης', 'ας']:
        gen = properN[:-1]

        gender = 'masc'

    elif properN_un[-2:] == 'ις':
        gen = properN[:-1] + 'δος'
        if accent == 'antepenultimate':
            gen = put_accent_on_the_antepenultimate(gen)

        gender = 'fem'

    elif properN.lower() in ['μωάμεθ', 'τζορτζ', 'αδάμ', 'σεραφείμ', 'νόμπελ']:
        #masc aklita
        gen = properN
        gender = 'masc'
    elif properN.lower() in ['μαριάμ', 'μαδιάμ']:
        #fem aklita
        gen = properN
        gender = 'fem'
    elif properN_un[-1] in ['α', 'η', 'ω']:
        gen = properN + 'ς'
        gender = 'fem'

    elif properN_un[-1] == 'ο':
        gen = properN[:-1] + 'ού'
        if accent in ['penultimate', 'antepenultimate']:
            gen = put_accent_on_the_penultimate(gen, true_syllabification=False)
        gender = 'neut'
    elif properN_un[-1] == 'ι':
        gen = properN_un + 'ού'
        gender = 'neut'

    else:
        gen = properN
        gender = 'neut'

    noun_temp = check_in_greek_corpus(properN, gen, gender)

    return noun_temp