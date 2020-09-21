import copy
import pickle
from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, where_is_accent, put_accent_on_the_ultimate

from adjective.create_adj_decl import create_all_adj_forms
from adjective.create_adj_decl import adj_basic

aklita_quant_alternatives = {'εφτά': 'επτά', 'οχτώ': 'οκτώ', 'εννιά': 'εννέα', 'δεκαέξι': 'δεκάξι',
                                     'δεκαοχτώ': 'δεκαοκτώ', 'δεκαεννιά': 'δεκαεννέα', 'δεκαεφτά': 'δεκαεπτά'}

with open('el_GR.pickle') as file:
    greek_corpus = pickle.load(file)


def creat_all_quant_adj_forms(quant_base_forms, ordinal=False):
    """
    :param quant_base_forms:
    :return:
    """
    if ordinal:
        all_forms = create_all_adj_forms(quant_base_forms)

        return all_forms
    else:
        masc, fem, neut = quant_base_forms.split('/')
        forms = copy.deepcopy(adj_basic)

        if masc[-2:] in ['οι', 'οί'] and fem[-2:] in ['ες', 'ές'] and neut[-1] in ['α', 'ά']:
            # exclusively for quantifiers, as there are for obvious reasons only in plural
            accent = where_is_accent(masc, true_syllabification=False)
            acc_masc = masc[:-2] + 'ους'
            gen_pl = masc[:-2] + 'ων'
            if accent == 'ultimate':
                acc_masc = put_accent_on_the_ultimate(acc_masc)
                gen_pl = put_accent_on_the_ultimate(gen_pl)
            elif accent == 'antepenultimate':
                accs_masc = [acc_masc, put_accent_on_the_penultimate(acc_masc, true_syllabification=False)]
                gens_pl = [gen_pl, put_accent_on_the_penultimate(gen_pl, true_syllabification=False)]
                print(accs_masc, gens_pl)
                gen_pl = ','.join([g for g in gens_pl if g in greek_corpus])
                acc_masc = ','.join([a for a in accs_masc if a in greek_corpus])

        elif neut[-4:] == 'τρία':
            gen_pl = neut[:-4] + 'τριών'
            acc_masc = masc

        elif neut[-7:] == 'τέσσερα':
            gen_pl = 'τεσσάρων'
            acc_masc = masc
        elif neut in aklita_quant_alternatives:
            masc, fem, neut, acc_masc, gen_pl = neut + ',' + aklita_quant_alternatives[neut]

        elif neut == 'ένα':

            forms['sg']['masc']['nom'] = masc
            forms['sg']['masc']['acc'] = 'ένα,έναν'
            forms['sg']['masc']['voc'] = 'ένα'
            forms['sg']['masc']['gen'] = 'ενός'

            forms['sg']['fem']['nom'] = 'μια,μία'
            forms['sg']['fem']['acc'] = 'μια,μιαν,μία,μίαν'
            forms['sg']['fem']['gen'] = 'μίας,μιας'
            forms['sg']['fem']['voc'] = 'μία,μια'

            forms['sg']['neut']['gen'] = 'ενός'
            forms['sg']['neut']['nom'] = neut
            forms['sg']['neut']['acc'] = neut
            forms['sg']['neut']['voc'] = neut

            return forms, None

        elif masc == 'ενάμισης':

            forms['sg']['masc']['nom'] = masc
            forms['sg']['masc']['acc'] = masc[:-1]
            forms['sg']['masc']['voc'] = masc[:-1]
            forms['sg']['masc']['gen'] = masc[:-1]

            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = fem
            forms['sg']['fem']['gen'] = fem + 'ς'
            forms['sg']['fem']['voc'] = fem

            forms['sg']['neut']['gen'] = neut
            forms['sg']['neut']['nom'] = neut
            forms['sg']['neut']['acc'] = neut
            forms['sg']['neut']['voc'] = neut

            return forms, None
        else:
            masc, fem, neut, acc_masc, gen_pl = neut

        forms['pl']['masc']['nom'] = masc
        forms['pl']['masc']['acc'] = acc_masc
        forms['pl']['masc']['gen'] = gen_pl
        forms['pl']['masc']['voc'] = masc

        forms['pl']['fem']['nom'] = fem
        forms['pl']['fem']['acc'] = fem
        forms['pl']['fem']['gen'] = gen_pl
        forms['pl']['fem']['voc'] = fem

        forms['pl']['neut']['nom'] = neut
        forms['pl']['neut']['acc'] = neut
        forms['pl']['neut']['gen'] = gen_pl
        forms['pl']['neut']['voc'] = neut

        return forms, None



#     elif neut == 'μηδέν':
#
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#
#     elif neut == 'δεκαέξι':
#         alt = 'δεκάξι'
#         forms['masc']['nom'] = masc + ',' + alt
#         forms['masc']['gen'] = masc + ',' + alt
#         forms['masc']['acc'] = masc + ',' + alt
#         forms['masc']['voc'] = masc + ',' + alt
#         forms['fem']['nom'] = masc + ',' + alt
#         forms['fem']['gen'] = masc + ',' + alt
#         forms['fem']['acc'] = masc + ',' + alt
#         forms['fem']['voc'] = masc + ',' + alt
#         forms['neut']['nom'] = masc + ',' + alt
#         forms['neut']['gen'] = masc + ',' + alt
#         forms['neut']['acc'] = masc + ',' + alt
#         forms['neut']['voc'] = masc + ',' + alt
#
#     elif masc[-2:] == 'οι':
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = masc[:-2] + 'ων' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ων', true_syllabification=False)
#         forms['masc']['acc'] = masc[:-2] + 'ους' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ους', true_syllabification=False)
#         forms['masc']['voc'] = masc
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = masc[:-2] + 'ων' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ων', true_syllabification=False)
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = masc[:-2] + 'ων' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ων', true_syllabification=False)
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#
#         if masc[:4] == 'οχτα':
#             alt = 'οκτα'
#             for gender in forms:
#                 for case in forms[gender]:
#                     forms[gender][case] += ',' + forms[gender][case].replace(masc[:4], alt)
#         elif masc[:4] == 'εφτα':
#             alt = 'επτα'
#             for gender in forms:
#                 for case in forms[gender]:
#                     forms[gender][case] += ',' + forms[gender][case].replace(masc[:4], alt)
#         elif masc[:5] == 'εννια':
#             alt = 'εννεα'
#             for gender in forms:
#                 for case in forms[gender]:
#                     forms[gender][case] += ',' + forms[gender][case].replace(masc[:5], alt)
#
#     else:
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = masc
#         forms['masc']['acc'] = masc
#         forms['masc']['voc'] = masc
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = fem
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#
#     return forms