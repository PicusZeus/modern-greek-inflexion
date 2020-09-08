
import pickle
from modern_greek_accentuation.accentuation import where_is_accent, put_accent, count_syllables, remove_all_diacritics

with open('../el_GR.pickle', 'rb') as file:
    greek_corpus = pickle.load(file)

noun = {'nom_sg': '', 'gen_sg': '', 'nom_pl': '', 'gender': ''}

noun_basic = {'sg':{
                        'nom': '',
                        'gen': '',
                        'acc': '',
                        'voc': ''
                    },
              'pl': {
                      'nom': '',
                      'gen': '',
                      'acc': '',
                      'voc': ''
                  }
              }


def put_accent_on_unaccented_forms(forms):

    for number in forms.keys():
        for case in forms[number].keys():
            f = forms[number][case]
            if not where_is_accent(f) and count_syllables(f) > 1:
                forms[number][case] = put_accent(f, 'penultimate')
    return forms


def all_noun_forms(nom_sg, gen_sg, nom_pl, gender):
    """
    :param nom_sg:
    :param gen_sg:
    :param nom_pl:
    :param gender: 'fem' or 'masc' or 'neut'
    :return: tuple with 3 elements: forms in all cases in dictionary, gender, and alternative forms in dictionary, if exist
    """

    accent = where_is_accent(nom_sg, true_syllabification=False)
    # check which type of accent I need (true_syl false or true)

    if nom_sg[-2:] in ['ος', 'ός'] and gen_sg[-2:] in ['ου', 'ού']:
        gen_accent = where_is_accent(gen_sg, true_syllabification=False)
        thema = nom_sg[:-2]
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg[:-1]
        noun_basic['sg']['voc'] = put_accent(nom_sg[:-2] + 'ε', accent, true_syllabification=False)
        noun_basic['pl']['nom'] = put_accent(thema + 'οι', accent, true_syllabification=False)
        noun_basic['pl']['gen'] = put_accent(thema + 'ων', gen_accent, true_syllabification=False)
        noun_basic['pl']['acc'] = put_accent(thema + 'ους', gen_accent, true_syllabification=False)
        noun_basic['pl']['voc'] = noun_basic['pl']['nom']

        return noun_basic, gender, None

    elif nom_sg[-1:] == 'ς' and nom_pl and nom_pl[-2:] in ['ές', 'ες'] and gen_sg and remove_all_diacritics(gen_sg) == remove_all_diacritics(nom_sg[:-1]):

        pl_accent = where_is_accent(nom_pl, true_syllabification=False)
        gen_pl = nom_pl[:-2] + 'ων'
        if count_syllables(nom_sg) == count_syllables(nom_pl) and (nom_sg[-2:] in ['ης','ής', 'ας', 'άς']):
            gen_pl = put_accent(gen_pl, 'ultimate')
            if (nom_sg[-2:] == 'ας' and count_syllables(nom_sg) > 2) and nom_sg[-3:] != 'ίας':
                gen_pl = put_accent(gen_pl, 'penultimate', true_syllabification=False)
        else:
            gen_pl = put_accent(gen_pl, pl_accent, true_syllabification=False)

        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = nom_sg[:-1]
        noun_basic['sg']['acc'] = nom_sg[:-1]
        noun_basic['sg']['voc'] = gen_sg[:-1]
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = gen_pl
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif nom_sg[-1:] in ['α', 'ά', 'ή', 'η'] and gen_sg[-1:] == 'ς' and gender != 'neut':

        alternatives = None
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        if nom_pl:
            if nom_pl[-2:] in ['ες', 'ές'] and count_syllables(nom_sg) == count_syllables(nom_pl):
                gen_pl = nom_pl[:-2] + 'ων'
                gen_pl = put_accent(gen_pl, 'ultimate')
                if nom_sg[-3:] in ['ίδα', 'άδα', 'ητα']:
                    gen_pl = put_accent(gen_pl, 'penultimate')
                if gen_pl not in greek_corpus:
                    alt_gen_pl = put_accent(gen_pl, 'penultimate')
                    alt_gen_pl_b = put_accent(gen_pl, 'antepenultimate')
                    if alt_gen_pl in greek_corpus:
                        gen_pl = alt_gen_pl
                    elif alt_gen_pl_b in greek_corpus:
                        gen_pl = alt_gen_pl
            elif nom_pl[-3:] == 'εις':
                gen_pl = nom_pl[:-3] + 'εων'
                alternatives = {'sg': {'gen': ''}}
                alternatives['sg']['gen'] = put_accent(nom_sg[:-1] + 'εως', 'antepenultimate')
            else:
                pl_accent = where_is_accent(nom_pl, true_syllabification=False)
                gen_pl = nom_pl[:-2] + 'ων'
                gen_pl = put_accent(gen_pl, pl_accent, true_syllabification=False)

            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = gen_pl
            noun_basic['pl']['acc'] = nom_pl
            noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, alternatives

    elif nom_sg[-1:] == 'α' and gender == 'neut':
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = put_accent(nom_pl[:-1] + 'ων', 'penultimate')
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif nom_sg[-1:] in ['ς', 'ν'] and gen_sg != nom_sg and gender == 'neut':
        # to filter out aklita
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        gen_pl = put_accent(nom_pl[:-1] + 'ων', 'ultimate')
        if gen_sg[-2:] in ['ος']:
            gen_pl = put_accent(gen_pl, 'penultimate')
        if gen_pl not in greek_corpus:
            gen_pl_alt = put_accent(gen_pl, 'penultimate')
            if gen_pl_alt in greek_corpus:
                gen_pl = gen_pl_alt
        noun_basic['pl']['gen'] = gen_pl

        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif (nom_sg[-1:] in ['ο', 'ό'] or nom_sg == 'δάκρυ') and gender == 'neut':
        gen_accent = where_is_accent(gen_sg, true_syllabification=False)
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = put_accent(nom_pl[:-1] + 'ων', gen_accent, true_syllabification=False)
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif nom_sg[-2:] in ['ού'] and gender == 'fem':
        pl_accent = where_is_accent(nom_pl, true_syllabification=False)

        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = put_accent(nom_pl[:-2] + 'ων', pl_accent, true_syllabification=False)
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif nom_sg[-3:] == 'έας' and nom_pl[-3:] == 'είς':

        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg[:-1]
        noun_basic['sg']['voc'] = nom_sg[:-1]
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = put_accent(nom_pl[:-2] + 'ων', 'penultimate', true_syllabification=False)
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        # but only for feminine! so add gender differentiation
        alternative = {'sg': {'gen': nom_sg[:-2] + 'ως'}}

        return noun_basic, gender, alternative

    elif nom_sg[-1:] in ['ί', 'ι', 'ΐ', 'υ'] and gen_sg[-2:] == 'ού':

        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = put_accent(nom_pl[:-1] + 'ων', 'ultimate')
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return  noun_basic, gender, None

    elif nom_sg == nom_pl:
        #aklita
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = nom_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = nom_pl
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif nom_sg[-1:] == 'ς':
        # special cases:
        if nom_sg in ['μυς', 'δρυς']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = nom_sg[:-1]
            noun_basic['sg']['voc'] = nom_sg[:-1]
            noun_basic['pl']['nom'] = put_accent(nom_pl, 'penultimate', true_syllabification=False)
            noun_basic['pl']['gen'] = put_accent(nom_pl[:-2] + 'ών', 'ultimate')
            noun_basic['pl']['acc'] = nom_sg
            noun_basic['pl']['voc'] = put_accent(nom_pl, 'penultimate', true_syllabification=False)

        elif nom_sg in ['ιλύς', 'ισχύς', 'ιχθύς', 'οσφύς']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = nom_sg[:-1]
            noun_basic['sg']['voc'] = nom_sg[:-1]
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = nom_pl[:-2] + 'ων'
            noun_basic['pl']['acc'] = nom_sg
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg in ['άλως']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = nom_sg[:-1]
            noun_basic['sg']['acc'] = nom_sg[:-1]
            noun_basic['sg']['voc'] = nom_sg
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = nom_pl
            noun_basic['pl']['acc'] = nom_pl
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg in ['αιδώς']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = nom_sg[:-1]
            noun_basic['sg']['voc'] = nom_sg
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = nom_pl
            noun_basic['pl']['acc'] = nom_pl
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg in ['έρπης', 'πατρίς', 'δράστις', 'δεσποινίς', 'καλλιτέχνις']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = gen_sg[:-2] + 'α'
            noun_basic['sg']['voc'] = nom_sg
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = put_accent(nom_pl[:-2] + 'ων', 'penultimate')
            noun_basic['pl']['acc'] = nom_pl
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg in ['βασιλεύς']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = gen_sg[:-2] + 'α'
            noun_basic['sg']['voc'] = nom_sg[:-1]
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = gen_sg[:-2] + 'ων'
            noun_basic['pl']['acc'] = gen_sg[:-2] + 'ας'
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg[-3:] == 'ους':
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = gen_sg
            noun_basic['sg']['voc'] = gen_sg
            noun_basic['pl']['nom'] = nom_sg[:-3] + 'οι'
            noun_basic['pl']['gen'] = nom_sg[:-3] + 'ων'
            noun_basic['pl']['acc'] = nom_sg
            noun_basic['pl']['voc'] = nom_sg[:-3] + 'οι'

            if nom_sg == 'νους':
                noun_basic['pl']['nom'] = ''
                noun_basic['pl']['gen'] = ''
                noun_basic['pl']['acc'] = ''
                noun_basic['pl']['voc'] = ''

        elif nom_sg in ['όφις', 'όρχις']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = nom_sg[:-1] + 'ν'
            noun_basic['sg']['voc'] = nom_sg[:-1]
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = nom_pl[:-3] + 'εων'
            noun_basic['pl']['acc'] = nom_pl
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg in ['βότρυς', 'πέλεκυς']:
            gen_pl =put_accent(nom_pl[:-3] + 'ων', 'penultimate')
            if nom_sg in ['πέλεκυς']:
                gen_pl = nom_pl[:-3] + 'εων'
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = nom_sg[:-1] + 'ν'
            noun_basic['sg']['voc'] = nom_sg[:-1]
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = gen_pl
            noun_basic['pl']['acc'] = nom_sg
            noun_basic['pl']['voc'] = nom_pl

        elif nom_sg in ['ιθαγενής', 'εκατονταετής']:
            noun_basic['sg']['nom'] = nom_sg
            noun_basic['sg']['gen'] = gen_sg
            noun_basic['sg']['acc'] = gen_sg
            noun_basic['sg']['voc'] = gen_sg
            noun_basic['pl']['nom'] = nom_pl
            noun_basic['pl']['gen'] = nom_pl[:-3] + 'ών'
            noun_basic['pl']['acc'] = nom_pl
            noun_basic['pl']['voc'] = nom_pl

        else:
            print(noun)

        return noun_basic, gender, None

    elif nom_sg[-1:] in ['ρ', 'ν', 'ξ', 'ύ'] and gen_sg[-2:] in ['ος', 'ός']:

        voc_sg = gen_sg[:-2]
        if gen_sg[-4:] in ['ντος', 'κτος'] or count_syllables(nom_sg) == 1:
            voc_sg = nom_sg

        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_pl[:-2] + 'α'
        noun_basic['sg']['voc'] = voc_sg
        gen_pl = put_accent(nom_pl[:-2] + 'ων', 'penultimate')
        if where_is_accent(gen_sg) == 'ultimate':
            gen_pl = put_accent(gen_pl, 'ultimate')
        if not nom_pl:
            gen_pl = ''
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = gen_pl
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif nom_sg in ['ηχώ', 'πειθώ', 'φειδώ', 'βάβω']:
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = nom_pl
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl


        return noun_basic, gender, None


    elif gen_sg[-3:] == 'εως':
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = nom_pl[:-1] + 'εων'
        noun_basic['pl']['acc'] = nom_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

    elif not nom_sg and (nom_pl[-2:] in ['ες', 'οι'] or nom_pl[-1:] == 'α'):
        acc_pl = nom_pl
        if nom_pl[-2:] == 'οι':
            acc_pl = put_accent(nom_pl[:-2] + 'ους', 'penultimate')
        noun_basic['sg']['nom'] = nom_sg
        noun_basic['sg']['gen'] = gen_sg
        noun_basic['sg']['acc'] = nom_sg
        noun_basic['sg']['voc'] = nom_sg
        noun_basic['pl']['nom'] = nom_pl
        noun_basic['pl']['gen'] = put_accent(nom_pl[:-2] + 'ων', 'penultimate')
        noun_basic['pl']['acc'] = acc_pl
        noun_basic['pl']['voc'] = nom_pl

        return noun_basic, gender, None

"""
TODO:
not correctly recognized
{'sg': {'nom': 'ους', 'gen': 'ωτός', 'acc': 'ους', 'voc': 'ους'}, 'pl': {'nom': 'ώτα', 'gen': 'ωτών', 'acc': 'ώτα', 'voc': 'ώτα'}}
{'sg': {'nom': 'ημίφως', 'gen': 'ημίφωτος', 'acc': 'ημίφως', 'voc': 'ημίφως'}, 'pl': {'nom': 'ημίφωτα', 'gen': 'ημιφωτών', 'acc': 'ημίφωτα', 'voc': 'ημίφωτα'}}
{'sg': {'nom': 'ντορός', 'gen': 'ντορούς', 'acc': 'ντορός', 'voc': 'ντορός'}, 'pl': {'nom': 'ντορή', 'gen': 'ντορών', 'acc': 'ντορή', 'voc': 'ντορή'}}
{'sg': {'nom': 'σύμπαν', 'gen': 'σύμπαντος', 'acc': 'σύμπαν', 'voc': 'σύμπαν'}, 'pl': {'nom': 'σύμπαντα', 'gen': 'συμπαντών', 'acc': 'σύμπαντα', 'voc': 'σύμπαντα'}}
{'sg': {'nom': 'λυκόφως', 'gen': 'λυκόφωτος', 'acc': 'λυκόφως', 'voc': 'λυκόφως'}, 'pl': {'nom': 'λυκόφωτα', 'gen': 'λυκοφωτών', 'acc': 'λυκόφωτα', 'voc': 'λυκόφωτα'}}
{'sg': {'nom': 'σκιόφως', 'gen': 'σκιόφωτος', 'acc': 'σκιόφως', 'voc': 'σκιόφως'}, 'pl': {'nom': 'σκιόφωτα', 'gen': 'σκιοφωτών', 'acc': 'σκιόφωτα', 'voc': 'σκιόφωτα'}}
{'sg': {'nom': 'αρειανός', 'gen': 'αρειανούς', 'acc': 'αρειανός', 'voc': 'αρειανός'}, 'pl': {'nom': 'αρειανή', 'gen': 'αρειανών', 'acc': 'αρειανή', 'voc': 'αρειανή'}}
{'sg': {'nom': 'υπεζωκώς', 'gen': 'υπεζωκότος', 'acc': 'υπεζωκώς', 'voc': 'υπεζωκώς'}, 'pl': {'nom': 'υπεζωκότα', 'gen': 'υπεζωκοτών', 'acc': 'υπεζωκότα', 'voc': 'υπεζωκότα'}}
{'sg': {'nom': 'σεληνόφως', 'gen': 'σεληνόφωτος', 'acc': 'σεληνόφως', 'voc': 'σεληνόφως'}, 'pl': {'nom': 'σεληνόφωτα', 'gen': 'σεληνοφωτών', 'acc': 'σεληνόφωτα', 'voc': 'σεληνόφωτα'}}
{'sg': {'nom': 'επιπεφυκώς', 'gen': 'επιπεφυκότος', 'acc': 'επιπεφυκώς', 'voc': 'επιπεφυκώς'}, 'pl': {'nom': 'επιπεφυκότα', 'gen': 'επιπεφυκοτών', 'acc': 'επιπεφυκότα', 'voc': 'επιπεφυκότα'}}

"""

if __name__ == '__main__':



    for noun in nouns:
        res = all_noun_forms(noun['nom_sg'], noun['gen_sg'], noun['nom_pl'], noun['gender'])
        if res:
            if res[0]['sg']['nom'][-3:] == 'έας':
                #print(res)
                pass




